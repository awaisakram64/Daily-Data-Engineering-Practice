def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Logging: '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger
def process_data(data):
    return [d.upper() for d in data]

result = process_data(['plane', 'runway', 'tower'])
print(result)