
import time # Module allows delays
import random # Import random module to generate exercises randomly

# Welcome messages with pauses to allow users to read coherently
print("Welcome! Running this program is a form of cardio. Right?") 
time.sleep(1.5) # Wait 1.5 seconds before following message
print("You have just outsourced your fitness decisions to a Python script.")
time.sleep(1.5) # Wait 1.5 seconds before following message
print("Dont worry. We will guide you step by step to an exercise that fits your goal.")

# Ask for users name
name = input("Before we start, whats your name?")
print(f"Great to meet you, {name}! Lets go!\n") # Greets user

# Defines the possible goals as a list
goals = ["strength", "endurance", "flexibility"]
goal = input(f"Choose your goal {goals}: ").lower() # Prompts users to select a goal and converts to lowercase

# Define focus options as a list of strings
focus_options = ["arms", "legs", "core"]
if goal == "endurance":
     focus_options.append("full body") # Add an additional option:'full body' if endurance is selected

# Ask user for focus and converts to lowercase
focus = input(f"Choose your focus {focus_options}: ").lower() # Get focus input

          
# Dictionary storing exercises organised by goal
# Each goal contains sub-dictionaries for focus areas
# Under each focus is a list of exercise strings the random module will randomly choose
workouts = { 
    "strength": {
        "arms": [
            "Wall Push-ups: 3 sets of 12",
            "Arms Circles: 3 sets of 30 seconds each",
            "Plank Shoulder Taps: 3 sets of 15 each side"
        ],
        "legs":[
            "Standing Calf Raises: 3 sets of 20 each leg",
            "lunges: 3 sets of 12 each leg",
            "Glute Bridges: 3 sets of 12"
        ],
        "core": [
            "Crunches: 3 sets of 15",
            "Russian Twists: 3 sets of 15",
            "Plank: 3 x 45 seconds"
        ],
    },
    "endurance": {
        "arms": [
            "Diamond Push-ups: 3 sets of 12",
            "Tricep Dips: 3 sets of 12",
            "Standard Push-ups: 3 sets of 15"
        ],
        "legs": [ 
            "Walking in place: 3 minutes",
            "Jump Squats: 3 sets of 15",
            "High Knees: 3 x 30 seconds"
        ],
        "core": [
            "Side Plank with Hip Dips: 3 x 30-45 seconds each side",
            "Knee Plank: 3 x 30 seconds",
            "Bird Dog: 3 x 12 seconds each side"
        ],
        "full body": [
            "Burpees: 3 x 10",
            "Mountain Climbers: 3 x 30 seconds",
            "Plank to Push-up: 3 x 12"
        ],
    },
    "flexibility": {
        "arms": [
            "Cross body stretch: 30 seconds",
            "Childs pose: 1 minute",
            "Wrist rotation: 1 minute"
        ],
        "legs": [
            "Touch your toes: 1 minute hold",
            "Hip flexor: 1 minute each leg",
            "Prone quad stretch: 1 minute each stretch"
        ],
        "core": [
            "Childs pose: 30 seconds",
            "Cobra pose abdominal stretch: 1 minute",
            "Cat cow stretch: 3 x 10"
        ]
    }
}
# Picks a random workout from chosen goal and focus
chosen_exercise=random.choice(workouts[goal][focus])

print(f'\nYour exercise is: {chosen_exercise}') # Displays chosen exercise

workouts[goal][focus].remove(chosen_exercise) # Remove the chosen exercise so it cannot repeat

time.sleep(2) # Pause before next steps

#Present options to continue or exit
print("\nWhat would you like to do next?")
print("1. Pick a new goal")
print("2. Get a new focus (same goal)")
print("3. Exit")

time.sleep(2) # Pause before next steps

# Loop to allow user to select new options until they exit
while True:
    print("\nWhat would you like to do next?")
    choice = input("Enter 1, 2 or 3:") # Get users input

    if choice == "1":
        # User starts from the beginning, selecting a new goal then focus
        goal = input(f"Choose your goal {goals}: ").lower() # Prompts user to select a goal from 'goals' list 
        focus_options = ["arms", "legs", "core"] # Defines possible focus areas
        if goal == "endurance":
            focus_options.append("full body") # Add 'full body' option for endurance goal
        focus = input(f"Choose your focus {focus_options}: ").lower() # Prompts user to select a focus

        exercises = workouts[goal][focus].copy() # Copies the list of exercises for the selected goal/focus to avoid modifying the original dictionary
        chosen_exercise = random.choice(exercises) # Select a random exercise from the copied list
        exercises.remove(chosen_exercise) # Removes the original selected exericise from list to prevent repetition if user picks another exercise in this section
        print(f'\nYour exercise is: {chosen_exercise}')
    elif choice == "2":
        # User picks a new focus with the same original goal
        focus = input(f"Get a new focus {focus_options}: ").lower()
        exercises = workouts[goal][focus].copy() # Copies exercise list for new focus
        chosen_exercise = random.choice(exercises) # Picks a random exercise from the new focus 
        exercises.remove(chosen_exercise) # Remove original selected exercise to avoid repeats
        print(f'Your new exercise is: {chosen_exercise}')
    elif choice =="3":
        print("Dont sweat it! See you next time!") # Goodbye message if user chooses to exit
        break # Loop ends, ending the program

   