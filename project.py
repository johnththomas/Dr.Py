# Define a dictionary of emojis and their corresponding descriptions
emoji_dict = {
    "1": "\U0001F600": "Feeling good",
    "2": "\U0001F44D": "Thumbs up",
    "3": "\U0001F923": "Hilarious",
    "4": "\U0001F914": "Not sure",
    "5": "\U0001F622": "Feeling sad
}

# Function to display the medication reminder
def show_medication_reminder():
    # Display available emoji options
    print("How do you feel after taking your medication?")
    print("Choose an emoji:")
    for emoji_code, description in emoji_dict.items():
        print(f"{emoji_code}: {description}")
    
    # Get user input
    while True:
        selected_emoji = input("Enter the emoji code: ")
        if selected_emoji in emoji_dict:
            break
        else:
            print("Invalid emoji code. Please try again.")
    
    # Return the selected emoji
    return selected_emoji

# Example usage
selected_emoji = show_medication_reminder()
print(f"You selected: {emoji_dict[selected_emoji]}")
