import random

# List of questions and keys
def get_questions():
    return [
        ("What is your name? ", "name"),
        ("How old are you? ", "age"),
        ("What is your favorite color? ", "color"),
        ("What is your favourite food? ", "food"),
        ("Which city do you live in? ", "city"),
        ("Which SHS did you attend? ", "shs"),
        ("What's your favourite soccer team? ", "team")
    ]

# Ask all questions and collect answers
def ask_questions():
    questions = get_questions()
    random.shuffle(questions)
    answers = {}

    for question, key in questions:
        response = input(question).strip()
        while response == "":
            response = input(f"Please answer - {question}").strip()
        answers[key] = response
    return answers

# Create and show summary
def display_summary(data):
    summary = f"""
Hello, {data['name']}!
You are {data['age']}-years-old, love the color {data['color']}, and enjoy eating {data['food']}.
You attended {data['shs']}. {data['team']} must be a very good soccer team that's why it's your favorite.
Life must be awesome in {data['city']}!
"""
    print(summary)
    return summary

# Save answers to a text file named after the user
def save_to_file(data, summary, rating):
    filename = f"{data['name'].capitalize()}.txt"
    try:
        with open(filename, "w") as file:
            file.write("====Personal Assistant Summary====\n")
            file.write(summary)
            file.write(f"\nUser rating: {rating}/5 stars\n")
        print(f"\n✅ Summary successfully saved to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

# Main assistant logic
def main():
    print("Welcome to the Simple Personal Assistant!\n")
    while True:
        user_data = ask_questions()
        summary = display_summary(user_data)
        
        save = input("Would you like to save this summary to a file? (yes/no): ").strip().lower()
        if save == "yes":
            rating = input("How would you rate this assistant? (1 to 5 stars): ").strip()
            while rating not in ["1", "2", "3", "4", "5"]:
                rating = input("Please enter a number between 1 and 5: ").strip()
            save_to_file(user_data, summary, rating)
        else:
            print("Okay, the summary won't be saved.")

        restart = input("\nWould you like to restart the assistant? (yes/no): ").strip().lower()
        if restart != "yes":
            print("\nGoodbye! Have a great day!")
            break
        print("\nRestarting...\n")

# Start the program
if __name__ == "__main__":
    main()
