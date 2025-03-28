import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
adoption_areas = ['RPA', 'Computer Vision', 'Natural Language Understanding']
adoption_rates = [39, 34, 33]

# Set the color palette
sns.set_palette('rocket_r')

# Create the bar plot
plt.figure(figsize=(8, 6))
plt.barh(adoption_areas, adoption_rates, color=sns.color_palette('rocket_r')[0])

# Add labels and title
plt.xlabel('Adoption Rate (%)')
plt.title('AI Adoption Rates in Different Areas')

# Remove top and right spines
sns.despine()

# Show the plot
plt.show()