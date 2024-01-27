import requests
from datetime import datetime


def get_upcoming_launches():
    url = "https://11.thespacedevs.com/2.2.0/launch/upcoming/"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        launches = data.get("results", [])
        return launches
    else:
        return None

def display_launches(launches):
    print("\nUpcoming Space Launches:")

    for launch in launches:
        name = launch.get("name", "Unnamed Launch")
        net_date = launch.get("net", "")
        window_start = launch.get("window_start", "")
        rocket_name = launch.get("rocket", {}).get("configuration", {}).get("name", "Unknown Rocket")

        print(f"\nLaunch Name: {name}")
        print(f"Rocket: {rocket_name}")
        print(f"Net Launch Date: {net_date}")
        print(f"Launch Window Start: {window_start}")

def main():
    print("welcome to the Upcoming Space Launches Tracker!")

    while True:
        user_input = input ("\nEnter 'track' to get upcoming space launches or 'exit' to quit: ").lower()



