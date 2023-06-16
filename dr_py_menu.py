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

def set_reminder():
    reminder_time = random.randint(5, 15)  # Generate a random time between 5 and 15 seconds
    time.sleep(reminder_time)
    print("Reminder: It's time to take your medication!")

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
    set_reminder()

# Run the program
main()
