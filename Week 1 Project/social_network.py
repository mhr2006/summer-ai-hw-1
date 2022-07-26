#Various import Statements can go here
from tkinter import Y
from tkinter.messagebox import YES
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    name = input('What is your name')
                    username = name
                    age = input('What is your age')
                    years = age
                    p1 = Person(name, age)
                    print("Your account is ready")
                else: 
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                
                if inner_menu_choice == "2":
                    name = input('Username')
                    username = name
                    add_friend = print ("friend added")
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                if inner_menu_choice == "3":
                    name = input('Username')
                    username = name
                    block_friend = print("friend blocked")
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                if inner_menu_choice == "4":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                if inner_menu_choice == "6":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()