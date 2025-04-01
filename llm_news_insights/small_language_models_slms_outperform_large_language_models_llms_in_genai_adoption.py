import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
categories = ['Organizations Adopting GenAI', 'Organizations Not Fully Utilizing Data Estate', 'Organizations Expressing Ethical Concerns', 'Organizations Continuing GenAI Implementation']
values = [79, 60, 83, 80]

# Plot
sns.set_theme(style='whitegrid', palette='rocket_r')
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(categories, values, color=sns.color_palette('rocket_r', len(values)))
ax.set_xlim(0, 100)
ax.set_xlabel('Percentage (%)')
ax.set_title('Key Insights from Hyperscience GenAI Adoption Report')
plt.tight_layout()
plt.show()