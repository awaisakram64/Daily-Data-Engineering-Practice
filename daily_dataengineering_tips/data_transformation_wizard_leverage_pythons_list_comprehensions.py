# Here is a sample dataset representing ages:
ages = [22, 17, 34, 25, 30, 15, 18]

# Use list comprehension to filter out ages below 18:
adults = [age for age in ages if age >= 18]

# Transform the filtered ages by adding 1 to simulate a year passing:
adults_plus_one_year = [age + 1 for age in adults]

# Print the transformed list
print(adults_plus_one_year)