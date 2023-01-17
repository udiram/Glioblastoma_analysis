import pandas as pd

excel = pd.read_excel('data/X_trainGBM.xlsx')
excel.to_csv('data/X_trainGBM.csv')