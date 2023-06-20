import time, sys

Diseases = {
    1: "Headache",
    2: "Fever",
    3: "Cold & Sore throat",
    4: "Lethargy",
    5: "Bodypain",
    6: "Digestion_issues",
    7: "Muscle soreness",
    8: "Depression",
    9: "Overeating",
    10: "Laziness"
}

Meds = ["Laughitol", "Freezepam", "Chuckle acid Drops", "Grinergy Drink", "Massage",
        "Idukkigold", "Jollygum", "Malanacream", "Coke", "Fireup"]

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

def print_menu():
    print(colors +"---Welcome to the 'Dr.Py'! We aim to help you overcome your troubles---" + colors_end)
    for key, value in Diseases.items():
        print(f"{key}: {value}")
    print("---------------------")


def get_user_choice():
    while True:
        try:
            choice = int(input(colors + "Enter the number corresponding to your health issue: " + colors_end))
            if choice in Diseases:
                return choice
            else:
                print(colors_3 + "Invalid choice. Please enter a valid number." + colors_end_3)
        except ValueError:
            print(colors_3 +"Invalid input. Please enter a number." + colors_end_3)


def give_med_choice(choice):
    try:
        if choice == 1:
            pc = colors_2 + f"You should be having 2 shots of {Meds[0]} thrice a day" + colors_end_2
        elif choice == 2:
            pc = colors_2 + f"You can try having 1 tablet of {Meds[1]} thrice a day" + colors_end_2
        elif choice == 3:
            pc = colors_2 + f"You just have a few drops of {Meds[2]} every 4 hours" + colors_end_2
        elif choice == 4:
            pc = colors_2 + f"Try having {Meds[3]} once a day" + colors_end_2
        elif choice == 5:
            pc = colors_2 + f"You should get a nice {Meds[4]}" + colors_end_2
        elif choice == 6:
            pc = colors_2 + f"Stop eating! Give your body a break. Smoke up {Meds[5]}" + colors_end_2
        elif choice == 7:
            pc = colors_2 + f"You can try chewing {Meds[6]} few times a day" + colors_end_2
        elif choice == 8:
            pc = colors_2 + f"Try {Meds[7]} and have a cold shower" + colors_end_2
        elif choice == 9:
            pc = colors_2 + f"You should be having 1 tab of {Meds[8]} twice a day" + colors_end_2
        else:
            pc = colors_2 + f"You should be having 1 tablet of {Meds[9]} once a day" + colors_end_2
        return pc
    except IndexError:
        return colors_3 + "Invalid choice." + colors_end_3

def choice_reminder():
    cr = input ("Do you want to get reminders for your medication?     y/n\n")
   
    if cr =="n":
        print("\U0001F910", "Exit without utilising reminders\nSayanora! see you next time")
        sys.exit()
    else:
        return cr
    
def set_reminder():
    reminder_interval = int(input(colors_5 + "Enter the reminder interval in seconds: " + colors_end_5))
    reminder_counter = 0

    while True:
        reminder_counter += 1
        print(f"Reminder {reminder_counter}: It's time to take your medication!")

        # Wait for the specified interval
        time.sleep(reminder_interval)

        # Prompt user for action: snooze or dismiss
        action = input(colors_5 + "Enter '1'to snooze the reminder or '0'to dismiss and stop the reminder.\nPlease enter '0' or '1': " + colors_end_5)

        if action == "0":
            print("Reminder dismissed.")
            break
        elif action == "1":
            snooze_duration = int(input("Enter the snooze duration in seconds: "))
            print(f"Reminder snoozed for {snooze_duration} seconds.")
            time.sleep(snooze_duration)
        else:
            print(colors_3 + "Invalid action. Please enter '0' or '1'." + colors_end_3)
        

    print("Reminder stopped.")

def choice_feedback():
    cf = input ("Do you want to give your feedback?   y/n\n")
   
    if cf =="n":
        print("\U0001F910", "Exit without feedback\nSayanora! see you next time")
        sys.exit()
    else:
        return cf
                


def get_feedback():
    print("Please provide your feedback:")
    for key, value in emoji_dict.items():
        print(f"{key}: {value[0]} {value[1]}")

    while True:
        try:
            feedback = input(colors + "Enter the number corresponding to your feedback: " + colors_end)
           
            if feedback in emoji_dict:
                emoji, description = emoji_dict[feedback]
                print(f"Thank you for your feedback! {emoji} {description}")
                break
            else:
                print(colors_3 + "Invalid feedback." + colors_end_3)
        
        except ValueError:
            print(colors_3 + "Invalid feedback." + colors_end_3)
            
    return feedback

       
emoji_dict = {
    "1": ("\U0001F600", "Feeling good"),
    "2": ("\U0001F44D", "Thumbs up"),
    "3": ("\U0001F923", "Hilarious"),
    "4": ("\U0001F914", "Not sure"),
    "5": ("\U0001F622", "Feeling sad")
}

print_menu()
choice = get_user_choice()
med_choice = give_med_choice(choice)
print("Preparing your prescription... ")
time.sleep(3)
print(med_choice)
print("Now that you have your prescription... ... ")
choice_feedback()
time.sleep(3)
get_feedback()
choice_reminder()
time.sleep(3)
set_reminder()