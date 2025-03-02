import pandas as pd

df = pd.read_csv('data/311_reports_22-24.csv')

filtered_df = df[df['type'] == 'Rodent Activity'].copy()

filtered_df['month'] = pd.to_datetime(filtered_df['open_dt'])

filtered_df["year"] = filtered_df["month"].dt.year
filtered_df["month"] = filtered_df["month"].dt.month

filtered_df = filtered_df.sort_values(["year", "month"])

filtered_df.to_csv('data/311_rodent_reports_22-24.csv')

print(filtered_df)