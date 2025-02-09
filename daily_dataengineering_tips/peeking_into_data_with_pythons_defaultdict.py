from collections import defaultdict

# Creating a defaultdict with int as default factory
visit_counts = defaultdict(int)

# List of web page visits
pages = ['home', 'about', 'home', 'contact', 'home', 'about']

# Counting visits per page
for page in pages:
    visit_counts[page] += 1

print(dict(visit_counts))