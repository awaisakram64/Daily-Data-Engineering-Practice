from prefect import Flow, task

@task
def extract_data():
    print('Extracting data...')
    return [42, 84, 126]

@task
def transform_data(data):
    print('Transforming data...')
    return [x / 2 for x in data]

@task
def load_data(transformed_data):
    print(f'Loading data: {transformed_data}')

with Flow('ETL_Pipeline') as flow:
    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)

# Run the flow
evaluation_result = flow.run()