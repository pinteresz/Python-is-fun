# AMUSEMENT PARK
# Dictionary with ride names and prices
ride_prices = {
    "Rollercoaster": 5.0,
    "Ferris Wheel": 3.5,
    "Carousel": 2.0,
}

# Function to get user's name
def get_user_name():
    return input("Welcome to the park! Please enter your name: ")

# Function to ask the user for a ride choice and validate it
def get_ride_choice(ride_name):
    while True:
        try:
            choice = input(f"Do you want to ride the {ride_name}? (yes/no): ")
            if choice.lower() == 'yes':
                return True
            elif choice.lower() == 'no':
                return False
            elif not choice.isalpha():
                raise ValueError("Input should contain alphabetic characters only.")
            else:
                print("Please enter 'yes' or 'no'.") 
        # Trying different errors and how they work        
        except ValueError as ve:
            print(ve)
        except KeyboardInterrupt:
            print("You interrupted the input. Please try again.")
        except EOFError:
            print("You reached the end of the input.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        

# Initialize the total cost
total_cost = 0

# Get user's name using the get_user_name function
user_name = get_user_name()

# Ask the user which rides they want to choose
print(f"Hello {user_name}! Here are the rides to choose from:")
for ride, price in ride_prices.items():
    if get_ride_choice(ride):
        total_cost += price

# Calculate and display the total cost
print(f"Awesome! {user_name}, your total cost for the selected rides is: ${total_cost:.2f}")

# Say goodbye
print(f"Thank you for visiting our park, {user_name}! Enjoy your rides!")
