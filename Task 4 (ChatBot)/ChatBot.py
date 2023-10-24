import json
from difflib import get_close_matches

def load_Dict(path: str) -> dict:
    with open(path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_Dict(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)

def find_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(
        user_question, questions, n=1, cutoff=0.65)
    return matches[0] if matches else None

def get_answer(question: str, Dictionary: dict) -> str | None:
    for q in Dictionary["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_Dict("Dictionary.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break

        best_match: str | None = find_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print("Bot: Don't know the answer. Help Me?")
            new_answer: str = input ("Type the answer or skip: ")

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_Dict("Dictionary.json", knowledge_base)
                print('Bot: Thank you for the new response')

if __name__ == "__main__":
    chat_bot()