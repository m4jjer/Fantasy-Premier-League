# %%
import requests
import pandas as pd
from pathlib import Path

# %%
base_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
returned_data = requests.get(base_url)
data = returned_data.json()
players = data['elements']
folder = Path(r"C:\Users\mjord\OneDrive\FPL\FPL Extracts\25-26")
folder2 = folder / "player_data"

# %%
teams = data['teams']
teams_df = pd.DataFrame(teams)[['id', 'short_name']]
teams_df.rename(columns={"short_name" : "team"}, inplace=True)
teams_df.to_csv(folder / "teams.csv", index=False)

# %%
positions = data['element_types']
pos_df = pd.DataFrame(positions)[['id', 'plural_name_short']]
pos_df.rename(columns={"plural_name_short" : "position"}, inplace=True)
pos_df.to_csv(folder / "positions.csv", index=False)

# %%
events = data['events']
events_df = pd.DataFrame(events)[['id', 'name', 'deadline_time']]
events_df.rename(columns={"name" : "gameweek", "deadline_time" : "deadline"}, inplace=True)
events_df.to_csv(folder / "events.csv", index=False)

# %%
player_url = 'https://fantasy.premierleague.com/api/element-summary/'
id_list = [player["id"] for player in players]
for x in id_list:
    url = player_url + str(x)
    filename = folder2 / f"{x}.csv"
    individual_players = requests.get(url)
    player_data = individual_players.json()
    use_this = player_data['history']
    player_df = pd.DataFrame(use_this)
    player_df.to_csv(filename, index=False)


