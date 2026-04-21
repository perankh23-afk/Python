import requests

API_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_technology_request():
    response = requests.get(API_URL)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know?{fact_data['text']}")
    else:
        print("Failed to get fact")


while True:
    user_input = input("Enter: random fact, q:quit")
    if user_input.lower() == 'q':
        break
    get_technology_request()
