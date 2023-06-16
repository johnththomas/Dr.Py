import time

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


def print_menu():
    print("----- Main Menu -----")
    for key, value in Diseases.items():
        print(f"{key}: {value}")
    print("---------------------")


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


def give_med_choice(choice):
    try:
        if choice == 1:
            pc = f"You should be having 2 shots of {Meds[0]} thrice a day"
        elif choice == 2:
            pc = f"You can try having 1 tablet of {Meds[1]} thrice a day"
        elif choice == 3:
            pc = f"You just have a few drops of {Meds[2]} every 4 hours"
        elif choice == 4:
            pc = f"Try having {Meds[3]} once a day"
        elif choice == 5:
            pc = f"You should get a nice {Meds[4]}"
        elif choice == 6:
            pc = f"Stop eating! Give your body a break. Smoke up {Meds[5]}"
        elif choice == 7:
            pc = f"You can try chewing {Meds[6]} few times a day"
        elif choice == 8:
            pc = f"Try {Meds[7]} and have a cold shower"
        elif choice == 9:
            pc = f"You should be having 1 tab of {Meds[8]} twice a day"
        else:
            pc = f"You should be having 1 tablet of {Meds[9]} once a day"
        return pc
    except IndexError:
        return "Invalid choice."


def set_reminder():
    reminder_interval = int(input("Enter the reminder interval in seconds: "))
    reminder_counter = 0

    while True:
        reminder_counter += 1
        print(f"Reminder {reminder_counter}: It's time to take your medication!")

        # Wait for the specified interval
        time.sleep(reminder_interval)

        # Prompt user for action: snooze or dismiss
        action = input("Enter 'snooze' to snooze the reminder or 'dismiss' to stop the reminder: ")

        if action.lower() == "snooze":
            snooze_duration = int(input("Enter the snooze duration in seconds: "))
            print(f"Reminder snoozed for {snooze_duration} seconds.")
            time.sleep(snooze_duration)
        elif action.lower() == "dismiss":
            print("Reminder dismissed.")
            break
        else:
            print("Invalid action. Please enter 'snooze' or 'dismiss'.")

    print("Reminder stopped.")


def get_feedback():
    print("Please provide your feedback:")
    for key, value in emoji_dict.items():
        print(f"{key}: {value[0]} {value[1]}")

    feedback = input("Enter the number corresponding to your feedback: ")
    if feedback in emoji_dict:
        emoji, description = emoji_dict[feedback]
        print(f"Thank you for your feedback! {emoji} {description}")
    else:
        print("Invalid feedback.")


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
print(med_choice)

get_feedback()

set_reminder()
