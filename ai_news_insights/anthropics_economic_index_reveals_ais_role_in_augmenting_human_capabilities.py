import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
categories = ['Augmentation', 'Automation']
values = [57, 43]

# Set the color palette
sns.set_palette('rocket_r')

# Create the bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=values, palette='rocket_r')

# Add titles and labels
plt.title('AI Usage: Augmentation vs. Automation', fontsize=16)
plt.xlabel('Usage Type', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)

# Despine the plot
sns.despine()

# Show the plot
plt.show()