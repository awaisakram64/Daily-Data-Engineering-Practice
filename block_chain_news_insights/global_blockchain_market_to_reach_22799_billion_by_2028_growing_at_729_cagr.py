import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
years = np.array([2021, 2028])
market_values = np.array([4.93, 227.99])

# Calculate CAGR
cagr = (market_values[1] / market_values[0]) ** (1 / (years[1] - years[0])) - 1
cagr_percentage = cagr * 100

# Set up the plot
sns.set_theme(style='whitegrid', palette='rocket_r')
fig, ax = plt.subplots(figsize=(8, 6))

# Plot data
ax.plot(years, market_values, marker='o', color='b', label=f'CAGR: {cagr_percentage:.2f}%')

# Annotate CAGR
ax.annotate(f'CAGR: {cagr_percentage:.2f}%',
            xy=(0.5, 0.5),
            xycoords='axes fraction',
            ha='center',
            va='center',
            fontsize=12, color='black',
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))

# Labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Value (Billion USD)', fontsize=12)
ax.set_title('Global Blockchain Market Growth (2021-2028)', fontsize=14)

# Show plot
plt.tight_layout()
plt.show()