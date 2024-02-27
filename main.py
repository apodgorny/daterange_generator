from pre_processor  import PreProcessor
from post_processor import PostProcessor
from mapping        import MAPPING

FILE_NAME = 'data/raw_dates.txt'

def main():
	dates = PreProcessor.get_dates(FILE_NAME)

	print('date'.ljust(15), '|', 'pre_formula'.ljust(15), '|', 'variables'.ljust(15), '|', 'post_formula'.ljust(15), '|', 'dt_from', ' - ', 'dt_to')

	for date in dates:
		pre_formula, variables = PreProcessor.process_date(date)
		post_formula           = MAPPING.get(pre_formula)
		if not post_formula:
			print(f'Mapping not found for pre_formula: {date}, {pre_formula}')
			continue
		dt_from, dt_to = PostProcessor.generate_dates(post_formula, variables)
		dt_from = dt_from.strftime('%d/%m/%Y')
		dt_to   = dt_to.strftime('%d/%m/%Y') if dt_to else 'null'
		print(date.ljust(15), '|', pre_formula.ljust(15), '|', str(variables).ljust(15), '|', post_formula.ljust(15), '|', dt_from, ' - ', dt_to)

if __name__ == '__main__':
	main()