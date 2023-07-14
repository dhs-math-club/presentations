from bs4 import BeautifulSoup
from requests import Session

session = Session()
episodes = [
    "Rebirth",
    "Confrontation",
    "Dealings",
    "Pursuit",
    "Tactics",
    "Unraveling",
    "Overcast",
    "Glare",
]

for number, episode in enumerate(episodes):
    response = session.get(f"https://deathnote.fandom.com/wiki/{episode}/Transcript")
    soupy = BeautifulSoup(response.text)
    script_table = soupy.find("table", class_="wikitable")
    print(script_table.text)
    with open(f"{number + 1}-{episode}.txt", "w") as f:
        f.write(script_table.text)
