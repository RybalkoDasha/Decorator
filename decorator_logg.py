from datetime import datetime
import os
from main import decorator_write


def decorator_write(directory, file_name):
	file = os.path.join(directory, file_name)
	def wrap(some_func):
		def inner(*args, **kwargs):
			time = datetime.now()
			now = time.strftime("%d/%m/%Y %H:%M:%S")
			name = some_func.__name__
			result = some_func(*args, **kwargs)
			res = f" Дата: {now}, название: {name}, args: {args}, kwargs: {kwargs}, Результат: {result}"
			with open(file, 'w', encoding = 'utf-8') as f:
				f.write(res)
				f.close()
			return result
		return inner
	return wrap

if __name__ == '__main__':

	# f_dir = r"C:\"
	f_name = "date_new.txt"


	@decorator_write(f_dir, f_name)
	def calculator(a, b):
		return a + b


	print(calculator(a=76, b=14))