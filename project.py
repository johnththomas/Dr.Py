import random
import time

# Health Problems
health_problems = {
    1: "Headache",
    2: "Muscle soreness",
    3: "Depression",
    4: "Overeating",
    5: "Laziness"
}

# Medicaments
medicaments = {
    1: "Alcohol",
    2: "Methamphetamine",
    3: "Marijuana",
    4: "Heroin",
    5: "Cocaine"
}

# Define a dictionary of emojis and their corresponding descriptions
emoji_dict = {
    "1": ("\U0001F600", "Feeling good"),
    "2": ("\U0001F44D", "Thumbs up"),
    "3": ("\U0001F923", "Hilarious"),
    "4": ("\U0001F914", "Not sure"),
    "5": ("\U0001F622", "Feeling sad")
}

def display_menu():
    print("Menu:")
    print("1. Headache")
    print("2. Muscle soreness")
    print("3. Depression")
    print("4. Overeating")
    print("5. Laziness")

def get_user_choice():
    while True:
        try:
            choice = int(input("Please enter your disease (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_medicament():
    print("Select a medicament:")
    print("1. Alcohol")
    print("2. Methamphetamine")
    print("3. Marijuana")
    print("4. Heroin")
    print("5. Cocaine")

def get_medicament_choice():
    while True:
        try:
            choice = int(input("Please enter your choice of medicament (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_medication_reminder():
    # Display available emoji options
    print("How do you feel after taking your medication?")
    print("Choose an emoji:")
    for emoji_code, (emoji, description) in emoji_dict.items():
        print(f"{emoji_code} - {emoji} - {description}")
    
    # Get user input
    while True:
        selected_emoji = input("Enter the emoji code: ")
        if selected_emoji in emoji_dict:
            break
        else:
            print("Invalid emoji code. Please try again.")
    
    # Print the selected emoji and feeling
    emoji, feeling = emoji_dict[selected_emoji]
    print(f"You selected: {emoji} - {feeling}")

# Function to set the medication reminder
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

def main():
    print("Welcome to the 'Dr.Py' Medicament Reminder!")
    display_menu()
    health_problem_choice = get_user_choice()
    selected_health_problem = health_problems[health_problem_choice]
    print("You have selected:", selected_health_problem)

    select_medicament()
    medicament_choice = get_medicament_choice()
    selected_medicament = medicaments[medicament_choice]
    print("You have selected:", selected_medicament)

    print("Prescription: Take", selected_medicament, "for", selected_health_problem)
    show_medication_reminder()

# Run the program
main()
set_reminder()
