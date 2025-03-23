import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
years = np.array([2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028])
market_size = np.array([4.93, 10.5, 20.0, 35.0, 50.0, 75.0, 100.0, 227.99])

# Calculate CAGR
cagr = (market_size[-1] / market_size[0]) ** (1 / (years[-1] - years[0])) - 1

# Plot
sns.set_theme(style="whitegrid", palette="rocket_r")
plt.figure(figsize=(10, 6))
plt.plot(years, market_size, marker='o', color='b', label=f'CAGR: {cagr*100:.2f}%')
plt.title('Global Blockchain Market Growth (2021-2028)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Size (Billion USD)', fontsize=12)
plt.xticks(years)
plt.yticks(np.arange(0, 250, 25))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()