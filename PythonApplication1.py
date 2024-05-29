# Python Project 1
# Programmer:         Roman Archer 
# Date Of Completion: 19th May 2024
# Description:        Chatbot Responsive to User Input 

print ("Hi! My Name Is Lineux, Your ChatBot For Today.")

user_name = input("What Is Your Name?")
print(f"Nice To Meet You {user_name}!")

user_age = input(f"What Age Are You {user_name}?")
print(f"Good To Know {user_name}, I'll Remember You Are {user_age} Years Old")
user_job = input(f"What Do You Work As?")
print(f"{user_job} Is A Very Extensive Career Although I Doubt It Is For Someone Like You {user_name}")

lineux_colour = "Green"
user_colour = input(f"What Is Your Favourite Colour?")
print(f"{user_colour} Is A Cool Colour")
print(f"{lineux_colour} Is My Favourite Colour, Although I Do Love {user_colour} It Suits You")

user_final = input("Will That Be All Today?")
print(f"Alright {user_name}, Just So I Have A Full Recall Of The Information You Provided You Are {user_age} Years Old. You Work In The {user_job} Industry And Your Favourite Colour Is {user_colour}")

checker = input("Was That All Correct?")
print(f"Great, It Was Nice Chatting {user_name}. Lineux Will See You Next Time")
