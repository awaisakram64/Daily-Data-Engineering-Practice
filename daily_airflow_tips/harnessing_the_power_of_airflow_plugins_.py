from airflow.plugins_manager import AirflowPlugin

class MyPlugin(AirflowPlugin):
    name = "my_custom_plugin"
    operators = []  # Add your custom operators here
    hooks = []      # Add your custom hooks here
    executors = []  # Add your custom executors here
    macros = []     # Add your custom macros here
    admin_views = []
    flask_blueprints = []
    menu_links = []