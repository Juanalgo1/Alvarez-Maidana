import pandas as pd
import matplotlib.pyplot as plt

path_file = "students.csv"
dataframe = pd.read_csv(path_file) 
dataframe.dropna(subset = "Avg_Study_time_per_day", inplace = True)
dataframe.drop(columns = ["Timestamp", "Username"], inplace = True)
##print(dataframe)
print(dataframe.describe())