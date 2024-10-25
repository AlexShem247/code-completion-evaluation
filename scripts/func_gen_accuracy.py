import unittest

from scripts.pred_accuracy_by_size import load_json_file
from scripts.tiny_starcoder import TextGenerator

datasets = ["../dataset/string_manipulation_and_tests.json"]


def test_func_dummy(func, model):
    func['body'] = func['body'].replace('\n    ', '\n            ')
    test_func_code = f"""
import unittest
class TestFunc(unittest.TestCase):
    def test_myTest(self):
        {func['header']}
            {func['body']}
        {func['test']}
    """
    # Create a new local namespace
    local_namespace = {}

    # Try to execute the test code to define the test class
    try:
        exec(test_func_code, {}, local_namespace)
    except SyntaxError as se:
        print(f"Syntax error in test code: {se}")
        return 0  # Return 0 for syntax errors
    except Exception as e:
        print(f"Error while executing test code: {e}")
        return 0  # Return 0 for any other errors

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(local_namespace['TestFunc'])

    # Run the tests and collect the results
    result = unittest.TextTestRunner().run(suite)

    # Return 1 if all tests passed, otherwise return 0
    return 1 if result.wasSuccessful() else 0


def test_func(func, model, useDocstring=False):
    funcToFill = func["header"]
    if useDocstring:
        funcToFill += "\n    " + func["docstring"]
    result = model.predict_text(funcToFill).split("\n\n")[0].replace('\n    ', '\n            ')
    test_func_code = f"""
import unittest
class TestFunc(unittest.TestCase):
    """

    for i, test in enumerate(func["test"].split("\n        ")):
        # Append test
        test_func_code += f"""
    def test_{i}(self):
        {result}
        {test}
"""
    # Create a new local namespace
    local_namespace = {}

    # Try to execute the test code to define the test class
    try:
        exec(test_func_code, {}, local_namespace)
    except SyntaxError as se:
        print(f"Syntax error in test code: {se}")
        return 0  # Return 0 for syntax errors
    except Exception as e:
        print(f"Error while executing test code: {e}")
        return 0  # Return 0 for any other errors

        # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(local_namespace['TestFunc'])

    # Run the tests and collect the results
    result = unittest.TextTestRunner().run(suite)

    total_tests = result.testsRun
    passed_tests = total_tests - len(result.failures) - len(result.errors)

    if total_tests > 0:
        percentage_passed = passed_tests / total_tests  # Decimal percentage
    else:
        percentage_passed = 0.0  # Avoid division by zero

    return percentage_passed


if __name__ == "__main__":
    model = TextGenerator()
    noTests = 0
    score = 0
    plots = []

    for dataset_path in datasets:
        dataset = load_json_file(dataset_path)

        for file in dataset:
            print(file["file"])
            for func in file["contents"]:
                result = test_func_dummy(func, model)
                score += result
                noTests += 1
                plots.append((len(func["body"]), result))

    print(f"Tests passed: {score}")
    print(f"Number of tests: {noTests}")
