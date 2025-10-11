"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    scores_by_subject = reorganise_scores_by_subject(score_values)
    display_subject_details(scores_by_subject, subjects)

def reorganise_scores_by_subject(score_values):
    """Process list of by-student scores into list of by-subject scores."""
    subject_scores = []
    number_of_subjects = len(score_values[0])
    for _ in range(number_of_subjects):
        scores_for_one_subject = []
        for scores in score_values:
            scores_for_one_subject.append(scores.pop(0))
        subject_scores.append(scores_for_one_subject)
    return subject_scores

def display_subject_details(scores_by_subject, subject_names):
    for i, scores_for_one_subject in enumerate(scores_by_subject):
        print(subject_names[i], "Scores:")
        for score in scores_for_one_subject:
            print(f"{score:>2}")
        print(f"Max: {max(scores_for_one_subject):3}")
        print(f"Min: {min(scores_for_one_subject):3}")
        average = sum(scores_for_one_subject) / len(scores_for_one_subject)
        print(f"Avg: {average:6.2f}\n")

main()



