from datetime import datetime


def decorator_write(func):
	def inner(*args, **kwargs):
		time = datetime.now()
		now = time.strftime("%d/%m/%Y %H:%M:%S")
		name = func.__name__
		result = func(*args, **kwargs)
		res = f" Дата: {now}, название: {name}, args: {args}, kwargs: {kwargs}, Результат: {result}"
		with open("date.txt", 'w', encoding = 'utf-8') as f:
			f.write(res)
			f.close()
		return result
	return inner

if __name__ == '__main__':
	@decorator_write
	def calculator(a, b):
		return a + b


	print(calculator(a=7, b=5))