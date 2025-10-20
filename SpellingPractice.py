import json
import os
import pyttsx3
from time import sleep

DATA_FILE = "spelling_words.json"

# Initialize the speech engine and set the properties
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.setProperty('voice', ['2'])

def speak(text, speed=130):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Change the index to select a different voice
    engine.setProperty('voice', voices[0].id) # 0 for male, 1 for female
    engine.setProperty('voice', 'english')
    engine.setProperty('rate', speed)
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    engine.say(text)
    engine.runAndWait()

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- Main Features ---
def update_word_list(child_name, data):
    print(f"\n\nUpdating {child_name}'s word list...")
    words = []
    
    while True:
        word = input("Enter a word (or type ""DONE"" to finish): ").strip().lower()
        if word == "done":
            break
        if not all(c.isalpha() or c == "'" for c in word):
            print("❌ Words should only contain letters.")
            continue
        words.append(word)
    data[child_name] = words
    save_data(data)
    print(f"✅ {child_name}'s word list updated with {len(words)} words.")

def practice_words(child_name, data):
    words = data.get(child_name, [])
    if not words:
        print("⚠ No words saved. Please update the list first.")
        return
    
    print(f"\n\nPracticing {len(words)} words for {child_name}...")
    for word in words:
        attempts = 0
        while True:
            speak(word)
            attempt = input("Type the word (or type ""HELP"" for assistance): ").strip().lower()

            if attempt == word:
                print("✅ Correct!\n")
                speak("Good job!")
                sleep(2)
                break
            elif attempt == "help":
                spelling = "   ".join(list(word))
                speak(f"The spelling is:")
                sleep(0.5)
                speak(spelling, 80)
                print(f"Now type the spelled word 3 times correctly to move on")
                correct_count = 0
                while correct_count < 3:
                    retry = input(f"Attempt #{correct_count + 1} - Type the word: ").strip().lower()
                    if retry == word:
                        correct_count += 1
                    elif retry == "exit":
                        print("Exiting the practice session.")
                        return
                    else:
                        print("❌ Incorrect, try again.")
                        speak(spelling, 80)
                speak("Great job! Let's move on.")
                print("✅ Correct! moving on\n")
                sleep(2)
                break
            elif attempt == "exit":
                print("Exiting the practice session.")
                return
            else:
                print("❌ Incorrect, try again.")
                sleep(2)

def main():
    data = load_data()

    print("\n\n\nWelcome to the Spelling Practice Program!\n\n\n")
    child_name = input("Enter your name: ").strip().title()

    if child_name not in data:
        data[child_name] = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Practice words.")
        print("2. Update word list.")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()
        if int(choice) == 1:
            practice_words(child_name, data)
        elif int(choice) == 2:
            update_word_list(child_name, data)
        elif int(choice) == 3:
            print("Thanks for practicing with me!")
            sleep(3)
            break
        else:
            print("Invalid choice.\nPlease choose again from the options 1, 2, or 3.")

if __name__ == "__main__":
    main()
