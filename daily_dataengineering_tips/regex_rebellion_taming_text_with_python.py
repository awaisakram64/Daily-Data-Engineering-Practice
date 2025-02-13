import re

def extract_emails(text):
    email_pattern = r'[\w.-]+@[\w.-]+\.\w+'
    return re.findall(email_pattern, text)

# Example usage
sample_text = "Here are some emails: test@example.com, hello@world.com."
emails = extract_emails(sample_text)
print(emails)