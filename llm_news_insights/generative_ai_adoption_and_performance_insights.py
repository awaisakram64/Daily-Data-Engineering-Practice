import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
labels = ['Organizations Using GenAI', 'Organizations Planning to Increase GenAI Usage', 'Organizations Reporting SLMs Outperform LLMs', 'Organizations Underutilizing Data for AI Training']
values = [79, 97, 75, 77]

# Create a bar plot
sns.set_theme(style='whitegrid', palette='rocket_r')
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(labels, values, color=sns.color_palette('rocket_r', len(values)))

# Formatting
ax.set_xlim(0, 100)
ax.set_xlabel('Percentage (%)')
ax.set_title('Generative AI Adoption and Performance Insights')
plt.tight_layout()
plt.show()