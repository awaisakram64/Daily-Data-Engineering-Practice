from airflow.models import Variable

def get_api_key():
    api_key = Variable.get("my_api_key", default_var="NoKeyFound")
    return api_key

print(get_api_key())  # This will print the value of 'my_api_key' variable from Airflow