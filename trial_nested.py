import time, sys

# Diseases dictionary
Diseases = {
    1: "Headache",
    2: "Fever",
    3: "Cold & Sore throat",
    4: "Lethargy",
    5: {
        "name": "Bodypain",
        "subpains": {
            11: "Neck pain",
            12: "Shoulder pain",
            13: "Back pain"
        }
    },
    6: "Digestion_issues",
    7: "Muscle soreness",
    8: "Depression",
    9: "Overeating",
    10: "Laziness"
}

# Medications list
Meds = ["Laughitol", "Freezepam", "Chuckle acid Drops", "Grinergy Drink", "Massage",
        "Idukkigold", "Jollygum", "Malanacream", "Coke", "Fireup"]

# Print menu function
def print_menu():
    print("---Welcome to 'Dr.Py'! We aim to help you overcome your troubles---")
    for key, value in Diseases.items():
        if isinstance(value, dict):
            print(f"{key}: {value['name']}")
        else:
            print(f"{key}: {value}")
    print("---------------------")

# Get user choice function
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number corresponding to your health issue: "))
            if choice in Diseases:
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Give medication choice function
def give_med_choice(choice):
    try:
        if isinstance(Diseases[choice], dict):
            pc = f"For {Diseases[choice]['name']}, you can try {Meds[4]}."
        else:
            pc = f"You should be having 1 tablet of {Meds[choice-1]} once a day."
        return pc
    except IndexError:
        return "Invalid choice."

# Choice reminder function
def choice_reminder():
    cr = input("Do you want to get reminders for your medication?     y/n\n")

    if cr == "n":
        print("Exit without utilizing reminders\nSayonara! See you next time")
        sys.exit()
    else:
        return cr

# Set reminder function
def set_reminder():
    reminder_interval = int(input("Enter the reminder interval in seconds: "))
    reminder_counter = 0

    while True:
        reminder_counter += 1
        print(f"Reminder {reminder_counter}: It's time to take your medication!")

        # Wait for the specified interval
        time.sleep(reminder_interval)

        # Prompt user for action: snooze or dismiss
        action = input("Enter '1' to snooze the reminder or '0' to dismiss and stop the reminder.\nPlease enter '0' or '1': ")

        if action == "0":
            print("Reminder dismissed.")
            break
        elif action == "1":
            snooze_duration = int(input("Enter the snooze duration in seconds: "))
            print(f"Reminder snoozed for {snooze_duration} seconds.")
            time.sleep(snooze_duration)
        else:
            print("Invalid action. Please enter '0' or '1'.")

    print("Reminder stopped.")

# Choice feedback function
def choice_feedback():
    cf = input("Do you want to give your feedback?   y/n\n")

    if cf == "n":
        print("Exit without feedback\nSayonara! See you next time")
        sys.exit()
    else:
        return cf

# Get feedback function
def get_feedback():
    print("Please provide your feedback:")
    for key, value in emoji_dict.items():
        print(f"{key}: {value[0]} {value[1]}")

    while True:
        try:
            feedback = input("Enter the number corresponding to your feedback: ")

            if feedback in emoji_dict:
                emoji, description = emoji_dict[feedback]
                print(f"Thank you for your feedback! {emoji} {description}")
                break
            else:
                print("Invalid feedback.")

        except ValueError:
            print("Invalid feedback.")

    return feedback

# Emoji dictionary for feedback
emoji_dict = {
    "1": ("😀", "Feeling good"),
    "2": ("👍", "Thumbs up"),
    "3": ("🤣", "Hilarious"),
    "4": ("🤔", "Not sure"),
    "5": ("😢", "Feeling sad")
}

# Main program flow
print_menu()
choice = get_user_choice()
med_choice = give_med_choice(choice)

if isinstance(Diseases[choice], dict):
    subpains = Diseases[choice]["subpains"]
    nested_pain = Diseases[choice]["name"]
    print("---------------------")
    for key, value in subpains.items():
        print(f"{key}: {value}")
    print("---------------------")

    subpain_choice = int(input("Enter the number corresponding to your sub-pain issue: "))
    if subpain_choice in subpains:
        subpain = subpains[subpain_choice]
        massage_type = ""
        if subpain == "Neck pain":
            massage_type = "neck massage"
        elif subpain == "Shoulder pain":
            massage_type = "shoulder massage"
        elif subpain == "Back pain":
            massage_type = "back massage"

        med_choice += f" For {subpain}, you can try {massage_type}."
    else:
        print("Invalid sub-pain choice.")

print("Preparing your prescription...")
time.sleep(3)
print(med_choice)

choice_feedback()
time.sleep(3)
get_feedback()

choice_reminder()
set_reminder()
