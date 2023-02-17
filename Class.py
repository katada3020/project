class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("gusto", "French")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#next
class User:
    def __init__(self, first_name, last_name, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.location = location
    
    def describe_user(self):
        print(f"User's name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! How are you doing today?")
user1 = User("John", "yusuf", "johnyusufe@gmaile.com", 25, "kaduna")
user2 = User("nasir", "sarki", "nasir@gmaule.com", 30, "kano")
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
    
restaurant = Restaurant("Tasty Treats", "Italian")
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 10
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.set_number_served(20)
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.increment_number_served(5)
print(f"The restaurant has served {restaurant.number_served} customers.")

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a user with username '{self.username}' and email address '{self.email}'.")
        print(f"They are located in {self.location}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("nasir", "muh'd", "nasire", "nasirmuh'd@example.com", "kogi")
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Number of login attempts after reset: {user.login_attempts}")
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")
        
    def open_restaurant(self):
        print(f"{self.name} is now open!")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, increment):
        self.number_served += increment
        
restaurant = Restaurant("gusto", "kano")
print(f"the Number of customers served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Number of customers served: {restaurant.number_served}")

#
class User:
    def __init__(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old, from {self.city}, {self.country}.")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = User("nasir", "mohd", 30, "kd", "9ja,,")
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
#adding an attribute
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
        
    def show_flavors(self):
        print("We have the following flavors of ice cream:")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
ice_cream_stand = IceCreamStand("Ice Cream Palace", "Desserts")
ice_cream_stand.flavors = ["Chocolate", "Vanilla", "Strawberry", "Mint Chocolate Chip"]
ice_cream_stand.show_flavors()
# exercise 9-7
class Admin(User):
    def __init__(self, first_name, last_name, age, city, country):
        super().__init__(first_name, last_name, age, city, country)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"{self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
admin = Admin("Jane", "Doe", 35, "Los Angeles", "USA")
admin.show_privileges()
#exercise 9-8
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
class Admin(User):
    def __init__(self, first_name, last_name, age, city, country):
        super().__init__(first_name, last_name, age, city, country)
        self.privileges = Privileges()
        
admin = Admin("John", "Smith", 40, "London", "UK")
admin.privileges.show_privileges()

from restaurant import Restaurant
restaurant = Restaurant("gusto Kitchen", "nigerian")


restaurant.describe_restaurant()
#exercise 9-10
from user_admin import Admin

# Create an Admin instance
admin = Admin("nasir", "muhd", "jdoe", "katada3020@gmail.com")


admin.privileges.show_privileges()

import random

class Die:
   

    def __init__(self, sides=5):
        """Initialize die attributes."""
        self.sides = sides

    def roll_die(self):
        
        print(random.randint(1, self.sides))

# Make a 6-sided die and roll it 10 times
d6 = Die()
for i in range(10):
    d6.roll_die()

# Make a 10-sided die and roll it 10 times
d10 = Die(10)
for i in range(10):
    d10.roll_die()

# Make a 20-sided die and roll it 10 times
d20 = Die(20)
for i in range(10):
    d20.roll_die()
#9-14
import random

# Make a list of 10 numbers and 5 letters
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select four numbers or letters from the list
winning_numbers = random.sample(lottery, 4)

# Print a message saying that any ticket matching these four numbers or letters wins a prize
print(f"Any ticket matching these four numbers or letters wins a prize: {winning_numbers}")

#9-15
import random

# Define my_ticket and set the winning_ticket to None
my_ticket = [1, 2, 3, 4]
winning_ticket = None

# Keep pulling numbers until your ticket wins
attempts = 0
while my_ticket != winning_ticket:
    winning_ticket = random.sample(range(1, 11), 4)
    attempts += 1

# Print a message reporting how many times the loop had to run to give you a winning ticket
print(f"It took {attempts} attempts to win the lottery with the ticket {my_ticket}. The winning ticket was {winning_ticket}.")





