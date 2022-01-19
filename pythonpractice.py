#pandas practice
import pandas as pd
import numpy as np
import csv
df = pd.read_csv("/Users/winniecheng/Downloads/heart.csv")
df.head(5)
to_drop = ['cp','fbs','restecg','thalach','exang','oldpeak','slope','thal','target','ca']
df.drop(to_drop, inplace = True, axis = 1)
df.head(5)
new_name = {'age': 'Age','sex': 'Sex','trestbps': 'Bps','chol': 'Cholesterol'}
df.rename(columns = new_name, inplace = True)
df.head()
replace_values = {0: 'F', 1: 'M'}
df = df.replace({"Sex": replace_values})
df.head()
