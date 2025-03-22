import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
regions = ['United States', 'Europe', 'Asia']
values = [74, 10.9, 8.8]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Set color palette
sns.set_palette('rocket_r')

# Create bar plot
ax.bar(regions, values, color=sns.color_palette('rocket_r', len(values)))

# Add title and labels
ax.set_title('AI Investment by Region in 2024 (in Billion USD)', fontsize=16)
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Investment (Billion USD)', fontsize=12)

# Add gridlines
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Remove top and right spines
sns.despine()

# Show plot
plt.tight_layout()
plt.show()