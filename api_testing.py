import pandas as pd

df = pd.read_csv('reports_2024.csv')

filtered_df = df[df['type'] == 'Rodent Activity']

print(filtered_df)