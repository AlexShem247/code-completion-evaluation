import csv
import json
from enum import Enum

import Levenshtein
import numpy as np
from fastchrf import pairwise_chrf

from tiny_starcoder import TextGenerator


class Metric(Enum):
    EXACT_MATCH = 1
    CHRF = 2
    LEVENSHTEIN = 3
    JARO = 4


def loadJSONFile(filepath):
    """Load a JSON file and return its contents."""
    with open(filepath, "r") as file:
        return json.load(file)


def predictCodeInFunction(func, model):
    bodyBefore = (func["header"] + func["docstring"] + func["body"]["bodyBefore"])[-100:]
    prefix = func["body"]["prefix"]
    result = model.predictText(prompt=f"{bodyBefore} {prefix}")
    return result.replace(bodyBefore, "").lstrip().split("\n")[0]


datasets = ["../../datasets/missing_line_datasets/useful_math_dataset.json",
            "../../datasets/missing_line_datasets/python_kivy_app_dataset.json",
            "../../datasets/missing_line_datasets/python_pygame_app_dataset.json",
            "../../datasets/missing_line_datasets/python_pyqt_dataset.json",
            "../../datasets/missing_line_datasets/python_tkinter_app_dataset.json"
            ]


def isPredictedCorrect(actual, predicted, method):
    actualCleaned = actual.strip()
    predictedCleaned = predicted.strip()

    if method == Metric.EXACT_MATCH:
        return float(actualCleaned in predictedCleaned)
    elif method == Metric.LEVENSHTEIN:
        return Levenshtein.ratio(actualCleaned, predictedCleaned)
    elif method == Metric.JARO:
        return Levenshtein.jaro(actualCleaned, predictedCleaned)
    else:
        return np.array(pairwise_chrf([[predictedCleaned]], [[actualCleaned]]))[0][0][0] / 100


outputFile = "../../evaluation_results/accuracy_by_size_results.csv"

if __name__ == "__main__":
    model = TextGenerator()
    totalScore = 0
    no = 0

    # Stores results
    csvBuilder = [["Function Header", "Docstring", "Num. Words", "Original Code", "Predicted Code",
                   "Exact Match", "CHRF", "Levenshtein", "Jaro"]]

    for datasetPath in datasets:
        dataset = loadJSONFile(datasetPath)

        for file in dataset:
            print(f"Processing file: {file['file']}")
            for func in file["contents"]:
                try:
                    body = func["body"]
                    actual = body["prefix"] + body["removedWords"]
                    predicted = predictCodeInFunction(func, model)
                    exactMatchScore = isPredictedCorrect(actual, predicted, method=Metric.EXACT_MATCH)
                    chrfScore = isPredictedCorrect(actual, predicted, method=Metric.CHRF)
                    levenshteinScore = isPredictedCorrect(actual, predicted, method=Metric.LEVENSHTEIN)
                    jaroScore = isPredictedCorrect(actual, predicted, method=Metric.JARO)
                    numWordsRemoved = body["numWordsRemoved"]

                    # Store results
                    csvBuilder.append([func["header"], func["docstring"], body["numWordsRemoved"], actual,
                                       predicted, exactMatchScore, chrfScore, levenshteinScore, jaroScore])

                    totalScore += chrfScore
                    no += 1
                except TypeError:
                    pass

    if no > 0:
        overallAvg = totalScore / no
        print(f"Overall Average Accuracy: {overallAvg}")
    else:
        print("No functions processed.")

    # Write to a CSV file
    with open(outputFile, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(csvBuilder)

    print(f"Data written to {outputFile}")




