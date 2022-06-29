# IMPORTING LIBRARIES
import sys
import create_user
import create_graph
import post_pixel
import update_pixel
import delete_pixel

input_text = """
Hi, Welcome to Sleep Tracker.
What do you want to do?
(1) Create User
(2) Create a Sleep Graph
(3) Post Sleep Data
(4) Update Sleep Data
(5) Delete Sleep Data
Make a choice (1/2/3/4/5): 
"""
try:
    user_choice = int(input(input_text))
except:
    print("Your input is in incorrect format.")
    print("Exiting...")

if not (0 < user_choice < 6):
    print("Your choice must be between 1 and 5.")
    print("Exiting...")
    sys.exit(1)

user_name = input("Enter username: ")
password = input("Enter password: ")

if user_choice == 1:
    create_user.create_user(user_name, password)
elif user_choice == 2:
    create_graph.create_graph(user_name, password)
elif user_choice == 3:
    post_pixel.post_pixel(user_name, password)
elif user_choice == 4:
    update_pixel.update_pixel(user_name, password)
else:
    delete_pixel.delete_pixel(user_name, password)

print("Exiting...")
