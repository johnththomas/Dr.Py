import time

# Define a dictionary of emojis and their corresponding descriptions
emoji_dict = {
    "1": ("\U0001F600", "Feeling good"),
    "2": ("\U0001F44D", "Thumbs up"),
    "3": ("\U0001F923", "Hilarious"),
    "4": ("\U0001F914", "Not sure"),
    "5": ("\U0001F622", "Feeling sad")
}

# Function to display the medication reminder
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
    
    # Print the selected emoji
    print(f"You selected: {selected_emoji}")

def set_reminder(reminder_text, interval):
    while True:
        # Display the reminder text
        print(reminder_text)
        
        # Wait for the specified interval
        time.sleep(interval)

# Example usage
reminder_text = "It's time to take your medication!"
interval = 60  # 60 seconds = 1 minute

show_medication_reminder()
set_reminder(reminder_text, interval)
