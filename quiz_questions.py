import csv

def load_questions(filepath="quiz_questions.csv"):
    questions = []

    with open (filepath) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            question = {
                "questions": row["questions"],
                "options": [
                    row["choice1"],
                    row["choice2"],
                    row["choice3"],
                    row["choice4"],
                ],
                "answer": int(row["answer"]) - 1
            }
            questions.append(question)

    return questions

