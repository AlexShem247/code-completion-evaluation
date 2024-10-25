import json
import os

from scripts.parsingCode.generate_dataset import extractFunctionsFromFile


def list_python_files(folder_path):
    # List to store the names of Python files
    python_files = []

    # Loop through the items in the specified folder
    for item in os.listdir(folder_path):
        # Check if the item is a file and ends with .py
        if os.path.isfile(os.path.join(folder_path, item)) and item.endswith('.py'):
            python_files.append(item)

    return python_files


def match_src_with_tests(src_folder, test_folder):
    # Convert folder paths to absolute paths
    src_folder = os.path.abspath(src_folder)
    test_folder = os.path.abspath(test_folder)

    # Get lists of Python files from both folders
    src_files = list_python_files(src_folder)
    test_files = list_python_files(test_folder)

    # List to store matched files
    matched_files = []

    # Create a dictionary for matching
    for src_file in src_files:
        # Construct the expected test file name
        test_file_name = f"{os.path.splitext(src_file)[0]}_test.py"

        # Check if the test file exists in the test folder
        if test_file_name in test_files:
            matched_files.append({
                "src_file": os.path.join(src_folder, src_file),
                "test_file": os.path.join(test_folder, test_file_name)
            })

    return matched_files


def findFuncsAndTests(file):
    src_file = file["src_file"]
    test_file = file["test_file"]

    # Find functions
    funcs = extractFunctionsFromFile(src_file)
    tests = extractFunctionsFromFile(test_file)

    matched_funcs = []  # List to store matched functions with tests

    for func in funcs:
        # Find corresponding unit test
        function_name = func["header"].lstrip("def ").split("(")[0]
        test_name = f"test_{function_name}"

        # Check if there's a matching test
        for test in tests:
            test_function_name = test["header"].lstrip("def ").split("(")[0]
            if test_name == test_function_name:
                # Add the test body to the function
                func["test"] = test["body"]
                matched_funcs.append(func)  # Include only matched functions
                break  # Exit loop once a match is found

    return {"file": src_file, "contents": matched_funcs}


if __name__ == "__main__":
    src_folder = "../../sample/string/src"  # Path to the source files
    test_folder = "../../sample/string"  # Path to the test files
    outputFile = "string_manipulation_and_tests.json"
    matched_files = match_src_with_tests(src_folder, test_folder)

    funcsWithTest = [findFuncsAndTests(file) for file in matched_files]

    with open(outputFile, "w") as jsonFile:
        json.dump(funcsWithTest, jsonFile, indent=4)

    print(f"Dataset has been written to {outputFile}")
