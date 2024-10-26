import csv
import unittest

from scripts.code_generation.pred_accuracy_by_size import loadJSONFile
from scripts.code_generation.tiny_starcoder import TextGenerator

datasets = ["../../datasets/function_library_datasets/string_manipulation_and_tests.json"]


def testFunc(func, model=None, useDocstring=False):
    funcToFill = func["header"]
    if useDocstring:
        funcToFill += "\n    " + func["docstring"]

    if model:
        prediction = model.predictText(funcToFill).split("\n\n")[0].replace("\n    ", "\n            ")
    else:
        prediction = (funcToFill + "\n    " + func["body"]).replace("\n    ", "\n            ")
    testFuncCode = f"""
import unittest
class TestFunc(unittest.TestCase):
    """

    asserts = ["self." + f for f in func["test"].split("self.")[1:]]
    for i, test in enumerate(asserts):
        # Append test
        testFuncCode += f"""
    def test_{i}(self):
        {prediction}
        {test}
"""

    localNamespace = {}
    prediction = "\n".join([line.lstrip() for line in prediction.split("\n")[1:]])
    # Try to execute the test code to define the test class
    try:
        exec(testFuncCode, {}, localNamespace)
    except SyntaxError as se:
        print(f"Syntax error in test code: {se}")
        return prediction, "No", 0, 1
    except Exception as e:
        print(f"Error while executing test code: {e}")
        return prediction, "No", 0, 1

        # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(localNamespace["TestFunc"])

    # Run the tests and collect the results
    result = unittest.TextTestRunner().run(suite)

    totalTests = result.testsRun
    passedTests = totalTests - len(result.failures) - len(result.errors)

    return prediction, "Yes", passedTests, totalTests


outputFile = "../../evaluation_results/func_gen_accuracy_results.csv"

if __name__ == "__main__":
    model = TextGenerator()
    noTests = 0
    score = 0
    csvBuilder = [["Function Header", "Docstring", "Body Length", "Original Code", "Predicted Code",
                   "Code Compiles", "No. Tests Passed", "No. Tests Available", "Accuracy"]]

    for datasetPath in datasets:
        dataset = loadJSONFile(datasetPath)

        for file in dataset:
            print(file["file"])
            for func in file["contents"]:
                prediction, compiles, noPassed, totalTests = testFunc(func, model=model, useDocstring=False)
                score += noPassed / totalTests
                noTests += 1
                csvBuilder.append([func["header"], func["docstring"], len(func["body"]), func["body"],
                                   prediction, compiles, noPassed, totalTests, noPassed / totalTests])

    print(f"Tests passed: {score}")
    print(f"Number of tests: {noTests}")

    # Write to a CSV file
    with open(outputFile, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(csvBuilder)

    print(f"Data written to {outputFile}")
