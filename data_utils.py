import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)

    filtered_df = df[df['type'] == 'Rodent Activity'].copy()

    filtered_df['month'] = pd.to_datetime(filtered_df['open_dt'])

    filtered_df["month"] = filtered_df["month"].dt.month

    filtered_df = filtered_df.sort_values("month")

    return filtered_df
