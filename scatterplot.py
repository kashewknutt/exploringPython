import matplotlib.pyplot as plt

# Data for the scatterplot
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sales = [100000, 150000, 160000, 280000]

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(quarters, sales, color='blue')
plt.title('Quarterly Sales Data')
plt.xlabel('Quarters')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.xticks(quarters)
plt.show()
