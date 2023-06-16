import time, random

#Diseases
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
# Medications
Meds = ["Laughitol", "Freezepam","Chuckle acid Drops","Grinergy Drink","Massage",
    "Idukkigold","Jollygum","Malanacream","Coke","Fireup"
]
def display_menu():
    print("Menu:")
    print("1. Headache")
    print("2. Fever")
    print("3. Cold & Sore throat")
    print("4. Lethargy")
    print("5. Bodypain")
    print("6. Digestion_issues")
    print("7. Muscle soreness")
    print("8. Depression")
    print("9. Overeating")
    print("10. Laziness")

def get_user_choice():
    while True:
        try:
            choice = int(input("Please enter your health problem (1-10): "))
            if 1 <= choice <= 10:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Don't be shy. Just enter a number.")


#Add preparing prescription time window

def give_med_choice():
    while True:
        try:
            choice = get_user_choice()
            if choice == 1:
                pc =(f"You should be having 2 shots of {Meds[0]} thrice a day")
            elif choice == 2:
                pc =(f"You can try having 1 tablet of {Meds[1]} thrice a day")
            elif choice == 3:
                pc =(f"You just have few drops of {Meds[2]} every 4 hours")
            elif choice == 4:
                pc =(f"Try having {Meds[3]} once a day")
            elif choice == 5:
                pc =(f"You should get a nice {Meds[4]} ")
            elif choice == 6:
                pc =(f"Stop eating! Give your body a break. Smoke up {Meds[5]}")
            elif choice == 7:
                pc =(f"You can try chewing {Meds[6]} few times a day")
            elif choice == 8:
                pc =(f"Try {Meds[7]} and have cold shower")
            elif choice == 9:
                pc =(f"You should be having 1 tab of {Meds[8]} twice a day")
            else:
                pc =(f"You should be having 1 tablet of {Meds[9]} once a day")
            return pc
        except ValueError:
                print("Don't be shy. Just enter the number")

def main():
    print("Welcome to the 'Dr.Py'! We aim to help you overcome your troubles")
    display_menu()
    health_problem_choice = get_user_choice()
    selected_health_problem = Diseases[health_problem_choice]
    med_choice = print(give_med_choice())
    print(f"""
    Your problem is: {selected_health_problem}
    and my suggestion for you: {med_choice}
    """)

# Run the program
main()