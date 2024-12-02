import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns  

np.random.seed(42)

data_size = 10

data = {
    'x': np.random.rand(data_size) * 100,  
    'y': np.random.rand(data_size) * 100,  
    'label': [f'Point {i}' for i in range(data_size)]  
}

df = pd.DataFrame(data)

# First scatter plot
plt.figure(figsize=(10, 7))  
plt.scatter(df['x'], df['y'], alpha=0.6, color='blue', edgecolor='black')  

for i in range(len(df)):
    plt.annotate(df['label'][i], (df['x'][i], df['y'][i]), fontsize=8, alpha=0.7)

plt.title('Scatter Plot with Labeled Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True) 
plt.show()  

# Second scatter plot with regression line
plt.figure(figsize=(10, 7))  
sns.scatterplot(x='x', y='y', data=df, color='blue', alpha=0.6)  
sns.regplot(x='x', y='y', data=df, scatter=False, color='red')  

for i in range(len(df)):
    plt.annotate(df['label'][i], (df['x'][i], df['y'][i]), fontsize=8, alpha=0.7)

plt.title('Scatter Plot with Regression Line and Labeled Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  
plt.show()  

# Customized scatter plot with regression line
plt.figure(figsize=(10, 7))  
plt.scatter(df['x'], df['y'], c='dodgerblue', marker='o', s=100, alpha=0.6, edgecolor='black')  
sns.regplot(x='x', y='y', data=df, scatter=False, color='darkorange', line_kws={'linewidth': 2})  

for i in range(len(df)):
    plt.annotate(df['label'][i], (df['x'][i], df['y'][i]), fontsize=8, alpha=0.7)

plt.title('Customized Scatter Plot with Regression Line and Labeled Points', fontsize=10)
plt.xlabel('X-axis', fontsize=10)
plt.ylabel('Y-axis', fontsize=10)
plt.grid(True)  
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('customized_scatter_plot_with_regression.png', dpi=300, bbox_inches='tight')  
plt.close()  