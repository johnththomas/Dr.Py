#Importing the required modules
import time, sys

#Menu of dieases using nested dictionaries
Diseases = {
            1: "Headache",
            2: "Fever",
            3: "Cold & Sore throat",
            4: "Lethargy",
            5: {"name":"Bodypain",
                "subissues":{
                                1:'chestpain',
                                2:'backpain',
                                3:'legpain'
                            }},
            6: {"name":"Digestion_issues",
                "subissues":  {
                                1:'indigestion',
                                2:'constipation',
                                3:'irritable_bowel'
                                    }},
            7: "Muscle soreness",
            8: "Depression",
            9: "Overeating",
            10: "Laziness"
    }

#Menu of Medicines using Lists
Meds = ["Laughitol", "Freezepam", "Chuckle acid Drops", "Grinergy Drink", "Massage",
        "Idukkigold", "Jollygum", "Malanacream", "Coke", "Fireup",
        "Little smoke","Yellow sunshine", "African salad","Vit.K","The Spirit Molecule"
        ]

# Making some textarea colorful (optional)
colors = "\033[92m"  # green
colors_end = "\033[0m"
colors_2 = "\033[95m"  # purple
colors_end_2 = "\033[0m"
colors_3 = "\033[91m"  # red
colors_end_3 = "\033[0m"
colors_4 = "\033[94m"  # blue
colors_end_4 = "\033[0m"
colors_5 = "\033[93m"  # yellow
colors_end_5 = "\033[0m"
colors_bold = "\033[1m"  # BOLD
colors_end_bold = "\033[0m"

#Function to display initial Menu
def print_menu():
    print(colors_bold +"\n\n---Welcome to the 'Dr.Py'!---" + colors_end_bold)
    print(colors +"---We aim to help you overcome your troubles---\n" + colors_end)
    for key, value in Diseases.items():
        if isinstance(value, dict):
            print(f'{key}: {value["name"]}')
        else:
            print(f"{key}: {value}")
    print("---------------------")

#function to get choice given by the user
def get_user_choice():
    while True:
        try:
            choice = int(input(colors + "Please enter the number corresponding to your health issue: " + colors_end))
            if choice in Diseases:
                return choice
            else:
                print(colors_3 + "Invalid choice. Please enter a valid number." + colors_end_3)
        except ValueError:
            print(colors_3 +"Invalid input. Please enter a number." + colors_end_3)

#subfunction to take user input of subissues within disease choice
def digest():
    while True:
        try:
                option = int(input(colors + "Please enter the number corresponding to your more specific issue: " + colors_end))
                if option in Diseases:
                    return option
                else:
                    print(colors_3 + "Invalid choice. Please enter a valid number." + colors_end_3)
        except ValueError:
                print(colors_3 +"Invalid input" + colors_end_3)

#function to give medical prescription
def give_med_choice(choice):
    try:
        if isinstance(Diseases[choice], dict):#check if the choice is a dictionary
            print(Diseases[choice].get('subissues'))
            option = digest()
            if choice== 5:
                try:
                    if option == 1:
                        pc = colors_2 + f"Stop fooling around!\nTry calling 112 now\nGet to an Hospital asap" + colors_end_2
                    elif option == 2:
                        pc = colors_2 + f"You should apply {Meds[10]} and maybe try to get a nice {Meds[4]}" + colors_end_2
                    elif option == 3:
                        pc = colors_2 + f"You should try {Meds[11]} get a nice {Meds[4]}" + colors_end_2
                except ValueError:
                    print(colors_3 +"Invalid input" + colors_end_3)
            else:
                try:
                    if option == 1:
                        pc = colors_2 + f"Give your body a break. Smoke up some {Meds[5]}." + colors_end_2
                    elif option == 2:
                        pc = colors_2 + f"Drink more fluids and stop screwing up your system\n Also maybe try having {Meds[12]}" + colors_end_2
                    elif option == 3:
                        pc = colors_2 + f"You can try having 1 tab of {Meds[8]} twice a day" + colors_end_2
                except ValueError:
                    print(colors_3 +"Invalid input" + colors_end_3)
        elif choice == 1:
            pc = colors_2 + f"You should be having 2 shots of {Meds[0]} thrice a day" + colors_end_2
        elif choice == 2:
            pc = colors_2 + f"You can try having 1 tablet of {Meds[1]} thrice a day" + colors_end_2
        elif choice == 3:
            pc = colors_2 + f"You just have a few drops of {Meds[2]} every 4 hours" + colors_end_2
        elif choice == 4:
            pc = colors_2 + f"Try having {Meds[3]} and {Meds[13]} once a day" + colors_end_2
        elif choice == 7:
            pc = colors_2 + f"You can try chewing {Meds[6]} few times a day" + colors_end_2
        elif choice == 8:
            pc = colors_2 + f"Try {Meds[7]} and have a cold shower. If that didn't help...try {Meds[14]}" + colors_end_2
        elif choice == 9:
            pc = colors_2 + f"Smoke up {Meds[5]}.\nNow try eating something and you never wanna eat anything too much" + colors_end_2
        else:
            pc = colors_2 + f"You should be having 1 tablet of {Meds[9]} once a day, in addition try getting a Whack on your head" + colors_end_2
        return pc
    except IndexError:
        return colors_3 + "Invalid choice." + colors_end_3

# function to ask if user want to give feedback
def choice_feedback():
    while True:
        try:
            cf = input ("Do you want to give your feedback?   y/n\n")
            if cf =="y":
                return cf  
            elif cf =="n":
                print("\U0001F910", "Ok! You want to continue without feedback!")
                break
                             
        except ValueError:
                print(colors_3 +"Invalid option. Please enter 'y' or 'n'" + colors_end_3)

 # function to ask if user want to use reminder for the medicines              
def choice_reminder():
    while True:
        try:
            cr = input ("Do you want to get reminders for your medication?     y/n\n")
            if cr =="y":
                return cr
              
            elif cr=="n":
                print("\U0001F44B", "Exit without utilising reminders\nTschüs! see you next time")
                sys.exit()
        except IndexError: 
            print (colors_3 + "Invalid option. Please enter 'y' or 'n'" + colors_end_3)
    
# function to actually take feedback
def get_feedback():
    print("Please provide your feedback:")
    for key, value in emoji_dict.items():
        print(f"{key}: {value[0]} {value[1]}")

    while True:
        try:
            feedback = input(colors + "Enter the number corresponding to your feedback: " + colors_end)
           
            if feedback in emoji_dict:
                emoji, description = emoji_dict[feedback]
                print(f"Thank you for your feedback!\n {emoji} {description}")
                break
            else:
                print(colors_3 + "Invalid feedback." + colors_end_3)
        
        except ValueError:
            print(colors_3 + "Invalid feedback." + colors_end_3)
            
    return feedback

# function to actually implement reminder
def set_reminder():
        while True:
            try:
                reminder_interval = int(input(colors_5 + "Enter the reminder interval in seconds: " + colors_end_5))
                reminder_counter = 0

            
                reminder_counter += 1
                print(f"Reminder {reminder_counter}: It's time to take your medication!\U0001F48A")

                # Wait for the specified interval
                time.sleep(reminder_interval)

                # Prompt user for action: snooze or dismiss
                action = input(colors_5 + "Enter '1'to snooze the reminder or '0'to dismiss and stop the reminder.\nPlease enter '0' or '1': " + colors_end_5)

                if action == "0":
                    print("Reminder dismissed. See you next time!")
                    break
                elif action == "1":
                    snooze_duration = int(input("Enter the snooze duration in seconds: "))
                    print(f"Reminder snoozed for {snooze_duration} seconds.")
                    time.sleep(snooze_duration)
                else:
                    print(colors_3 + "Invalid action. Please enter '0' or '1'." + colors_end_3)
            except ValueError:
                print(colors_3 +"Invalid input" + colors_end_3)  
        print("Reminder stopped.")  

# dictionary of emojis used in the code
emoji_dict = {
    "1": ("\U0001F600", "Feeling good"),
    "2": ("\U0001F44D", "Thumbs up"),
    "3": ("\U0001F923", "Hilarious"),
    "4": ("\U0001F914", "Not sure"),
    "5": ("\U0001F622", "Feeling sad")
}

#Actual Main chunk of core code 
print_menu()
choice = get_user_choice()
med_choice = give_med_choice(choice)
print("Preparing your prescription... ")
time.sleep(2)
print(med_choice)
print("Now that you have your prescription... ... ")
if choice_feedback() =='y':
    get_feedback()
if choice_reminder() =='y':
    set_reminder()


