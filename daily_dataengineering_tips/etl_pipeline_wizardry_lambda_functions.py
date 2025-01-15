# Let's say we have a list of records with first and last names combined.
data = ['jane_doe', 'john_smith', 'alice_jones']

# We want to split them into proper name components using a lambda function!
split_names = list(map(lambda name: name.split('_'), data))

print(split_names)