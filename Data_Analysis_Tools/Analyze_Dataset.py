import pandas as pd
from xlwings import view

# Load a dataset (for example, Iris dataset)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, names=columns)

# Display the first 5 rows of the dataset
print(df.head())

# Basic statistics of the dataset
print(df.describe())

# Count of each class
print(df['class'].value_counts())

# Display first 10 rows of dataset in Excel spreadsheet
view(df[:10])