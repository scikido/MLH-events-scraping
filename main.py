import requests
from bs4 import BeautifulSoup
import json

url = "https://mlh.io/seasons/2023/events"

response = requests.get(url)

hackathons = {}

soup = BeautifulSoup(response.content, 'html.parser')

event_list = soup.find_all('div', class_='event-wrapper')

for event in event_list:
    name = event.find('h3', class_='event-name').text.strip()
    date = event.find('p', class_='event-date').text.strip()
    event_type = event.find('div', class_='event-hybrid-notes').text.strip()
    event_loc = event.find('div', class_='event-location').text.strip()
    event_loc = " " + " ".join(event_loc.replace("\n", "").split()).strip()

    # Add the event data to the dictionary
    hackathons[name] = {
        "date": date,
        "type": event_type,
        "location": event_loc
    }

hackathons_json = json.dumps(hackathons)

print(hackathons_json)