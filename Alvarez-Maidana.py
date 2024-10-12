import pandas as pd
import matplotlib.pyplot as plt

path_file = "students.csv"
dataframe = pd.read_csv(path_file) 
##print(dataframe)
print(dataframe.describe())
print(dataframe.corr())