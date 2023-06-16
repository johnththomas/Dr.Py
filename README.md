# Dr.Py


*GOAL*

This program aims to be helpful in organising lives of many people who are sick and helps them to keep track of their medication intake.
In addition it helps them understand how they are feeling once they have the medicines. It records the feedback from users.


Primary step: User inputs what is his/her ailment from a list of diseases
program Dr.Py (DP) will suggest medicines and give patient options to choose from.
1. Lists
   - List of most common diseases
    - sublists : 
        –commonly prescribed medicines for each disease
2. Dictionaries
    - Medicines and their possible outcomes
            –positive and side-effects
    - Medicines and corresponding Emoticons


Reminder function
maybe use pync, time modules
or schedule-reminder

pync.notify(title = “reminder”, message=”hello”,timeout = 1)
while True:
reminder()
time.sleep(timeout in seconds)