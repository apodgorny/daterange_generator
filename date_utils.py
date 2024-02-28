import numpy             as np
import keras.backend     as K
import matplotlib.pyplot as plt

from keras.utils             import to_categorical


CHAR_PAD      = '@'
CHAR_UNK      = '^'

LOCALES  = ['en_US']
EXAMPLES = ['3 May 1979', '5 Apr 09', '20th February 2016', 'Wed 10 Jul 2007']

def create_vocabs(ds):
	human_vocab   = set()
	machine_vocab = set()

	for i in range(len(ds)):
		h, m = ds[i]
		if h is not None:
			human_vocab.update(tuple(h))
			machine_vocab.update(tuple(m))
	
	human = dict(zip(
		sorted(human_vocab) + [CHAR_UNK, CHAR_PAD],
		list(range(len(human_vocab) + 2))
	))

	inv_machine = dict(enumerate(sorted(machine_vocab) + [CHAR_UNK, CHAR_PAD]))
	machine = {v:k for k,v in inv_machine.items()}
	return  human, machine, inv_machine


def preprocess_data(ds, human_vocab, machine_vocab, Tx, Ty):
	X, Y = zip(*ds)
	print(X[0], Y[0])
	X = pad_to(X, Tx, CHAR_PAD)
	Y = pad_to(Y, Ty, CHAR_PAD)

	X = vector_encode(X, human_vocab,   human_vocab[CHAR_UNK])
	Y = vector_encode(Y, machine_vocab, machine_vocab[CHAR_UNK])

	Xoh = np.array(categorize(X, len(human_vocab)))
	Yoh = np.array(categorize(Y, len(machine_vocab)))
	
	return X, Y, Xoh, Yoh

def vector_encode(X, vocab, char_idx):
	vector = []
	for s in X:
		vector.append([vocab.get(c, char_idx) for c in tuple(s)])
	return vector

def categorize(X, vocab_length):
	return [to_categorical(x, num_classes=vocab_length) for x in X]

def pad_to(X, length, char):

	def _pad(s, length, char):
		if len(s) > length:
			s = s[:length]
		elif len(s) < length:
			s += char * (length - len(s))
		return s
	
	return [_pad(s, length, char) for s in X]
		

def vector_decode(Y, inv_vocab):
	res = []
	for enc_word in Y:
		res.append(''.join(inv_vocab[char_idx] for char_idx in enc_word))
	return res

def predict(model, human_vocab, inv_machine_vocab, texts):
	encoded = vector_encode(texts, human_vocab)
	prediction = model.predict(np.array([encoded]))
	prediction = np.argmax(prediction[0], axis=-1)
	return vector_decode(prediction, inv_machine_vocab)

def softmax(x, axis=1):
	"""Softmax activation function.
	# Arguments
		x : Tensor.
		axis: Integer, axis along which the softmax normalization is applied.
	# Returns
		Tensor, output of softmax transformation.
	# Raises
		ValueError: In case `dim(x) == 1`.
	"""
	ndim = K.ndim(x)
	if ndim == 2:
		return K.softmax(x)
	elif ndim > 2:
		e = K.exp(x - K.max(x, axis=axis, keepdims=True))
		s = K.sum(e, axis=axis, keepdims=True)
		return e / s
	else:
		raise ValueError('Cannot apply softmax to a tensor that is 1D')

def plot_attention_map(model, input_vocabulary, inv_output_vocabulary, text, n_s = 128, num = 6, Tx = 30, Ty = 8):
	"""
	Plot the attention map.

	"""
	attention_map = np.zeros((Ty, Tx))
	Ty, Tx = attention_map.shape

	s0 = np.zeros((1, n_s))
	c0 = np.zeros((1, n_s))
	layer = model.layers[num]

	encoded = np.array(vector_encode(text, Tx, input_vocabulary)).reshape((1, Tx))
	encoded = np.array(list(map(lambda x: to_categorical(x, num_classes=len(input_vocabulary)), encoded)))

	f = K.function(model.inputs, [layer.get_output_at(t) for t in range(Ty)])
	r = f([encoded, s0, c0])

	for t in range(Ty):
		for t_prime in range(Tx):
			attention_map[t][t_prime] = r[t][0,t_prime,0]

	# Normalize attention map
#     row_max = attention_map.max(axis=1)
#     attention_map = attention_map / row_max[:, None]

	prediction = model.predict([encoded, s0, c0])

	predicted_text = []
	for i in range(len(prediction)):
		predicted_text.append(int(np.argmax(prediction[i], axis=1)))

	predicted_text = list(predicted_text)
	predicted_text = vector_decode(predicted_text, inv_output_vocabulary)
	text_ = list(text)

	# get the lengths of the string
	input_length = len(text)
	output_length = Ty

	# Plot the attention_map
	plt.clf()
	f = plt.figure(figsize=(8, 8.5))
	ax = f.add_subplot(1, 1, 1)

	# add image
	i = ax.imshow(attention_map, interpolation='nearest', cmap='Blues')

	# add colorbar
	cbaxes = f.add_axes([0.2, 0, 0.6, 0.03])
	cbar = f.colorbar(i, cax=cbaxes, orientation='horizontal')
	cbar.ax.set_xlabel('Alpha value (Probability output of the "softmax")', labelpad=2)

	# add labels
	ax.set_yticks(range(output_length))
	ax.set_yticklabels(predicted_text[:output_length])

	ax.set_xticks(range(input_length))
	ax.set_xticklabels(text_[:input_length], rotation=45)

	ax.set_xlabel('Input Sequence')
	ax.set_ylabel('Output Sequence')

	# add grid and legend
	ax.grid()

	#f.show()

	return attention_map
