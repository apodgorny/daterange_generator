from pre_processor  import PreProcessor
from post_processor import PostProcessor
from mapping        import MAPPING

FILE_NAME = 'data/raw_dates.txt'

def main():
	dates = PreProcessor.get_dates(FILE_NAME)
	success_counter = 0

	print('date'.ljust(30), '|', 'pre_formula'.ljust(10), '|', 'dt_from', ' - ', 'dt_to')

	for date in dates:
		pre_formula, variables = PreProcessor.process_date(date)
		post_formula           = MAPPING.get(pre_formula)

		if post_formula:
			dt_from, dt_to = PostProcessor()(post_formula, variables)
			dt_from        = dt_from.strftime('%d/%m/%Y')
			dt_to          = dt_to.strftime('%d/%m/%Y') if dt_to else 'null'

			success_counter += 1
			# print(date.ljust(30), '|', pre_formula.ljust(10), '|', dt_from, ' - ', dt_to)
		else:
			# print(f'---> {pre_formula}----{date}')
			print(date, pre_formula)
			pass
		
	print('Success:', success_counter, '/', len(dates))

if __name__ == '__main__':
	main()