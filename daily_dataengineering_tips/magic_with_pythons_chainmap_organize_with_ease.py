from collections import ChainMap

# Imagine managing user settings across multiple dictionaries
defaults = {'theme': 'dark', 'show_logs': False}
user_settings = {'show_logs': True, 'email_notifications': False}

# Create a ChainMap
settings = ChainMap(user_settings, defaults)

# Accessing settings without missing any key
print('Theme:', settings['theme'])           # Outputs: dark
print('Show Logs:', settings['show_logs'])   # Outputs: True
print('Email Notifications:', settings['email_notifications']) # Outputs: False