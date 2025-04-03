from pybaseball import batting_stats
import pandas as pd

# Extracts batting stats from a given year
def extract_data(year: int) -> pd.DataFrame:
    print(f"Extracting batting stats for {year}")
    df = batting_stats(year) # uses built in batting_stats function to extract data
    print("Data extraction complete.")
    return df

