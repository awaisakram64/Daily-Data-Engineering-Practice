import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
funding = [24.2, 16.9, 15.5, 43.8]

# Set the color palette
sns.set_palette('rocket_r')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(quarters, funding, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.title('AI Funding by Quarter in 2024 (in Billion USD)', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Funding (Billion USD)', fontsize=12)

# Enhance the plot
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()