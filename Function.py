#creating a functions that tells what i am learnig

def display_message ():
	print("i am learning function")
display_message()
# writing a function about my favourite book

def favourite_book(title):
	print(f"one of my favourite book is, {title.lower()} in wonderland")
favourite_book("alice")
def make_shirt(size, message):
    print(f"A {size} shirt will be printed with the message: '{message}'")

# Calling  the function using positional arguments
make_shirt("medium", "I  love Python")

# Calling the function using keyword arguments
make_shirt(size="medium", message="be a scientist")
def make_shirt(message="I love Python", size="large"):
    print(f"A {size} shirt will be printed with the message: '{message}'")

# Call the function to make a large shirt with the default message
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt(size="medium")

# Call the function to make a shirt of any size with a custom message
make_shirt("Python is awesome!", "small")

#Writing a function that describe a country and city
def describe_city(city,country):
	print(f"{city} is in {country}")
describe_city("kaduna","nigeria")

def describe_city(city, country='nigeria'):
    print(f"{city} is in {country}.")

describe_city('kano')
describe_city('lagos')
describe_city('Paris', 'France')

def city_country(city, country):
    return f"{city.title()}, {country.title()}"
print(city_country("kaduna", "nigeria")) 
print(city_country("kani", "nigeria")) 
print(city_country("tokyo", "japan"))

def make_album(artist_name, album_title, num_songs=None):
    album = {"artist": artist_name, "title": album_title}
    if num_songs:
        album["num_songs"] = num_songs
    return album
album1 = make_album("ado gwanjat", "chass")
album2 = make_album("Ed Sheeran", "me", num_songs=16)
album3 = make_album("Beyonce", "africa", num_songs=12)

print(album1)
print(album2)
print(album3)
#using while loop and function
def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter album information:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    tracks = input("Number of tracks (optional): ")
    if tracks == 'q':
        break

    album = make_album(artist, title, tracks)
    print(album)
def show_messages(messages):
    
    for message in messages:
        print(message)

messages = [
    "Hello!",
    "How are you?",
    "What are you up to?"
]
show_messages(messages)
def send_messages(messages):
    
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages

messages = [
    "Hello!",
    "How are you?",
    "What are you up to?"
]
sent_messages = send_messages(messages)

print("Original list of messages:")
print(messages)
print("List of sent messages:")
print(sent_messages)

def send_messages(messages, sent_messages):
    
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = [
    "Hello!",
    "How are you?",
    "What are you up to?"
]
sent_messages = []
send_messages(messages[:], sent_messages) # Make a copy of the original list

print("Original list of messages:")
print(messages)
print("List of sent messages:")
print(sent_messages)

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
make_sandwich('egg')
make_sandwich('meat','fish')
make_sandwich('flower','meqy','potatoes')

def make_car(manufacturer, model, **car_info):
    
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


import pizza
from pizza import function
from pizza import function as f
import module_name as pz
