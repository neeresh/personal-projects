import numpy as np
import pandas as pd

dataset = pd.read_csv('GlassdoorData_USA.csv')

# Checking for null values.
print(dataset.isnull().any())

# Salary Parsing
dataset.fillna("-1", inplace=True)

# 1. Salary Parsing
dataset_salary = dataset[dataset['Salary Estimate'] != "-1"]

print(dataset_salary['Salary Estimate'])

