import json
import os

from generate_dataset import extractFunctionsFromFile


def listPythonFiles(folderPath):
    # List to store the names of Python files
    pythonFiles = []

    # Loop through the items in the specified folder
    for item in os.listdir(folderPath):
        # Check if the item is a file and ends with .py
        if os.path.isfile(os.path.join(folderPath, item)) and item.endswith(".py"):
            pythonFiles.append(item)

    return pythonFiles


def matchSrcWithTests(srcFolder, testFolder):
    # Convert folder paths to absolute paths
    srcFolder = os.path.abspath(srcFolder)
    testFolder = os.path.abspath(testFolder)

    # Get lists of Python files from both folders
    srcFiles = listPythonFiles(srcFolder)
    testFiles = listPythonFiles(testFolder)

    # List to store matched files
    matchedFiles = []

    # Create a dictionary for matching
    for srcFile in srcFiles:
        # Construct the expected test file name
        testFileName = f"{os.path.splitext(srcFile)[0]}_test.py"

        # Check if the test file exists in the test folder
        if testFileName in testFiles:
            matchedFiles.append({
                "srcFile": os.path.join(srcFolder, srcFile),
                "testFile": os.path.join(testFolder, testFileName)
            })

    return matchedFiles


def findFuncsAndTests(file):
    srcFile = file["srcFile"]
    testFile = file["testFile"]

    # Find functions
    funcs = extractFunctionsFromFile(srcFile)
    tests = extractFunctionsFromFile(testFile)

    matchedFuncs = []  # List to store matched functions with tests

    for func in funcs:
        # Find corresponding unit test
        functionName = func["header"].lstrip("def ").split("(")[0]
        testName = f"test_{functionName}"

        # Check if there's a matching test
        for test in tests:
            testFunctionName = test["header"].lstrip("def ").split("(")[0]
            if testName == testFunctionName :
                # Add the test body to the function
                func["test"] = test["body"]
                matchedFuncs.append(func)
                break

    return {"file": srcFile, "contents": matchedFuncs}


if __name__ == "__main__":
    srcFolder = "../../sample/string/src"  # Path to the source files
    testFolder = "../../sample/string"  # Path to the test files
    outputFile = "string_manipulation_and_tests.json"
    matchedFiles = matchSrcWithTests(srcFolder, testFolder)

    funcsWithTest = [findFuncsAndTests(file) for file in matchedFiles]

    with open(outputFile, "w") as jsonFile:
        json.dump(funcsWithTest, jsonFile, indent=4)

    print(f"Dataset has been written to {outputFile}")
