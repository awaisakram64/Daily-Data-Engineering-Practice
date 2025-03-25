import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
years = np.array([2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
revenue = np.array([0, 0, 0, 0, 0, 0, 0, 280])  # Projected revenue in billions

# Create a seaborn style plot
sns.set_theme(style='whitegrid', palette='rocket_r')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(years, revenue, marker='o', color='b', linewidth=2)
plt.title('Projected Generative AI Revenue Growth (2023-2030)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Revenue (Billions USD)', fontsize=12)
plt.xticks(years)
plt.yticks(np.arange(0, 301, 50))
plt.grid(True)
plt.show()