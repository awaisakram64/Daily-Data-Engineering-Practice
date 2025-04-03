from airflow.decorators import task

# This is your decorator function
def my_custom_decorator(func):
    def wrapper(*args, **kwargs):
        print('Preprocessing step...')
        result = func(*args, **kwargs)
        print('Postprocessing step...')
        return result
    return wrapper

@task
@my_custom_decorator
def process_data(data):
    print(f'Processing {data}')
    return data.upper()

# Example of how to call your decorated task
data = 'hello airflow'
process_data(data)