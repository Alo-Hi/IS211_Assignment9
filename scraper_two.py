
import requests
from bs4 import BeautifulSoup

# https://en.wikipedia.org/wiki/List_of_World_Series_champions

url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"

headers = {
    "User-Agent": "IS211Assignment9/1.0 (https://github.com/Alo-Hi/IS211_Assignment9)"
}

page = requests.get(url, headers=headers)
page.raise_for_status()

soup = BeautifulSoup(page.text, "html.parser")

table = None

for item in soup.find_all("table", class_="wikitable"):
    if "Winning team" in item.get_text() and "Losing team" in item.get_text():
        table = item
        break

if table:
    rows = table.find_all("tr")

    for row in rows:
        columns = row.find_all(["th", "td"])
        row_data = []

        for column in columns:
            row_data.append(column.get_text(" ", strip=True))

        if row_data:
            print(" | ".join(row_data))
else:
    print("Could not find the table.")

