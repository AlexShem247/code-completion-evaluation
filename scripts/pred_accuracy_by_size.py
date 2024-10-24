import json

import numpy as np
from fastchrf import pairwise_chrf
from tiny_starcoder import TextGenerator
import statistics


def load_json_file(filepath):
    """Load a JSON file and return its contents."""
    with open(filepath, "r") as file:
        return json.load(file)


def predictCodeInFunction(func, model):
    body_before = (func["header"] + func["docstring"] + func["body"]["bodyBefore"])[-50:]
    prefix = func["body"]["prefix"]
    return model.predict_text(prompt=f"{body_before} {prefix}").split("\n\n")[0]


def isPredictedCorrect(actual, predicted):
    """Calculate the CHRF score between the actual and predicted strings."""
    # Clean the input
    actual_cleaned = actual.strip()
    predicted_cleaned = predicted.strip()

    # Calculate CHRF score
    # Wrap the actual and predicted strings in lists to match the expected input format
    pairwise_scores = pairwise_chrf([[predicted_cleaned]], [[actual_cleaned]])

    # Extract the CHRF score from the output array
    chrf_score = np.array(pairwise_scores)[0][0][0]  # Access the score from the array structure
    return chrf_score / 100


# def isPredictedCorrect(actual, predicted):
#     # Clean the input
#     actual_cleaned = actual.strip()
#     predicted_cleaned = predicted.strip()
#     return float(actual_cleaned in predicted_cleaned)

# def levenshtein_distance(s1, s2):
#     """Compute the Levenshtein distance between two strings."""
#     if len(s1) < len(s2):
#         return levenshtein_distance(s2, s1)
#
#     if len(s2) == 0:
#         return len(s1)
#
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[j + 1] + 1
#             deletions = current_row[j] + 1
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#
#     return previous_row[-1]
#
#
# def isPredictedCorrect(actual, predicted):
#     """Measure similarity based on Levenshtein distance, returning a value between 0 and 1."""
#     actual_cleaned = actual.strip()
#     predicted_cleaned = predicted.strip()
#
#     if actual_cleaned == predicted_cleaned:
#         return 1.0  # Exact match
#
#     max_score = 0.0  # Initialize max score
#
#     # Check all possible substrings of the predicted string
#     for start in range(len(predicted_cleaned)):
#         for end in range(start + 1, len(predicted_cleaned) + 1):
#             substring = predicted_cleaned[start:end]
#             distance = levenshtein_distance(actual_cleaned, substring)
#             max_length = max(len(actual_cleaned), len(substring))
#
#             if max_length > 0:  # Avoid division by zero
#                 score = 1 - (distance / max_length)
#                 max_score = max(max_score, score)  # Update max score if current is higher
#
#     return max_score


datasets = ["../dataset/useful_math_dataset.json",
            "../dataset/python_kivy_app_dataset.json",
            "../dataset/python_pygame_app_dataset.json", "../dataset/python_pyqt_dataset.json",
            "../dataset/python_tkinter_app_dataset.json"
            ]

if __name__ == "__main__":
    model = TextGenerator()
    totalScore = 0
    no = 0

    # Dictionary to hold scores for each numWordsRemoved
    scores_by_num_words = {}

    for dataset_path in datasets:
        dataset = load_json_file(dataset_path)

        for file in dataset:
            print(file["file"])
            for func in file["contents"]:
                try:
                    # print(f"Trying function: {func['header']}")
                    body = func["body"]
                    # print(f"{body['bodyBefore']}{body['prefix']} ... {body['bodyAfter']}")

                    actual = body["prefix"] + body["removedWords"]
                    predicted = predictCodeInFunction(func, model)
                    # print(f"No words: {body['numWordsRemoved']}")
                    # print(f"Actual: {actual}\nPredicted: {predicted}")
                    score = isPredictedCorrect(actual, predicted)
                    # print(f"Accuracy Score of: {score}")

                    num_words_removed = body["numWordsRemoved"]

                    # Store all scores for this numWordsRemoved
                    if num_words_removed not in scores_by_num_words:
                        scores_by_num_words[num_words_removed] = []

                    scores_by_num_words[num_words_removed].append(score)

                    totalScore += score
                    no += 1
                except TypeError:
                    pass

    # Calculate statistics for each numWordsRemoved
    stats_by_num_words = {}
    for num, scores in scores_by_num_words.items():
        stats_by_num_words[num] = {
            "mean": sum(scores) / len(scores),
            "min": min(scores),
            "max": max(scores),
            "median": statistics.median(scores)
        }

    # Print statistics for each numWordsRemoved
    for num, stats in stats_by_num_words.items():
        print(f"Stats for numWordsRemoved = {num}:")
        print(f"  Mean: {stats['mean']}")
        print(f"  Min: {stats['min']}")
        print(f"  Max: {stats['max']}")
        print(f"  Median: {stats['median']}")

    if no > 0:
        overall_average = totalScore / no
        print(f"Overall Average Accuracy: {overall_average}")
    else:
        print("No functions processed.")
