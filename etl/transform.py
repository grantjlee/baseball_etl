import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Captures only relevant data per player
    df = df[['Name', 'Team', 'PA', 'HR', 'AVG', 'OBP', 'SLG']]

    # Renames columns for better readability
    df = df.rename(columns={
        'Name': 'player_name',
        'Team': 'team',
        'PA': 'plate_appearances',
        'HR': 'home_runs',
        'AVG': 'batting_average',
        'OBP': 'on_base_percentage',
        'SLG': 'slugging_percentage'
    })

    # Filter out any player with less than 50 plate appearances
    df = df[df['plate_appearances'] >= 50]

    return df
