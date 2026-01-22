import re, random
from colorama import Fore, init
autoreset=True

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains" : ["Rocky mountains", "Himilayas", "Swiss alps"],
    "cities" : ["Toykyo", "Paris", "New York"],
}

jokes = [
    "Why do Java developers wear glasses? Because they don't C#",
    "Unfortunately these jokes only work if you git them.",
    "I wanted to make a joke about time travel, but you guys didn’t like it",
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travelbot: beaches, mountains or cities?")
    preference = input(Fore.Yellow + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}? ")
        print(Fore.CYAN + "TravelBot: Do you like it (yes/no) ")
        answer = input(Fore.YELLOW + "You: ").lower()
    
    if answer == "yes":
        print(Fore.GREEN + f"Travelbot : Awesome! Enjoy {suggestion}")
    elif answer == "no":
        print(Fore.RED+ "Travelbot : I'll suggest another.")
        recommend()
    else:
        print(Fore.GREEN + "Travelbot : Sorry, I don't know another")
    
    show_help()

def packing_trips():
    print(Fore.CYAN + "Travelbot : Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBOT: how many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Travelbot : Packing tips for {days} days in {location}: ")
    print(Fore.GREEN + "- Pack versitile clothes")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check weather forecast")

def tell_joke():
     print(Fore.YELLOW + f"Travelbot : {random.choice(jokes)}")

def show_help():
     print(Fore.MAGENTA + "\nI can:") 
     print(Fore.GREEN + "-suggest travel options(recommendations)")
     print(Fore.GREEN + "-offer packing tips(packing)")
     print(Fore.GREEN + "- Tell joke(joke)")
     print(Fore.CYAN + "Type exit or bye to end.\n")

def chat():
    print(Fore.CYAN+ "TravelBOT: Hello! I am travelbot")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you {name}")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_trips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBOT: Safe travels!")
            break
        else:
            print(Fore.RED + "could you rephrase?")

if __name__ == "__main__":
    chat()

        

