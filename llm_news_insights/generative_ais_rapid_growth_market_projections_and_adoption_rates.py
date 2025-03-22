import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Middle East & Africa']
revenue_share = [40.2, 25.0, 20.0, 10.0, 4.8]

# Set the color palette
sns.set_palette('rocket_r')

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.barh(regions, revenue_share, color=sns.color_palette('rocket_r', len(regions)))

# Add labels and title
plt.xlabel('Revenue Share (%)')
plt.title('Generative AI Revenue Share by Region')

# Despine and add gridlines
sns.despine()
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()