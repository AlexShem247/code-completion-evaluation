import json
import os
import random
import re
import sys

MAX_FUNCS_PER_FILE = 50
MAX_FILES = 10


def findPythonFiles(directory):
    """Recursively find all Python files in the given directory."""
    pythonFiles = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                pythonFiles.append(os.path.join(root, file))

    random.shuffle(pythonFiles)
    return pythonFiles[:MAX_FILES]


def extractFunctionsFromFile(filePath):
    """Extract complete function definitions from a Python file."""
    functionDefinitions = []
    functionPattern = re.compile(r"^\s*def\s+\w+\s*\(.*\):")

    with open(filePath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        currentFunction = []
        insideFunction = False
        currentIndent = None
        header = None
        docstring = None

        for line in lines:
            # Check if the line starts a function definition
            if functionPattern.match(line):
                if insideFunction:  # Save the previous function if one is ongoing
                    body = "".join(currentFunction).strip("\n")
                    body = removeHeaderAndDocstring(body, docstring)
                    functionDefinitions.append({"header": header, "docstring": docstring, "body": body})
                    currentFunction = []

                # Start a new function
                insideFunction = True
                currentIndent = len(line) - len(line.lstrip())
                header = line.strip()  # Store the function header
                currentFunction.append(line)  # Add the line with the function definition
                docstring = None  # Reset the docstring for the new function

            elif insideFunction:
                # Check for a docstring immediately after the header
                if docstring is None and ('"""' in line or "'''" in line):
                    docstring = line.strip()
                    currentFunction.append(line)
                # Continue adding lines to the current function definition if they are indented
                elif len(line) - len(line.lstrip()) > currentIndent:
                    currentFunction.append(line)
                else:
                    # End of the current function if indentation is less than or equal to the currentIndent
                    body = "".join(currentFunction).strip("\n")
                    body = removeHeaderAndDocstring(body, docstring)
                    functionDefinitions.append({"header": header, "docstring": docstring, "body": body})
                    currentFunction = []
                    insideFunction = False

        # If we finish reading the file and were still inside a function, save it
        if insideFunction:
            body = "".join(currentFunction).strip("\n")
            body = removeHeaderAndDocstring(body, docstring)
            functionDefinitions.append({"header": header, "docstring": docstring, "body": body})

    return functionDefinitions


def removeHeaderAndDocstring(body, docstring):
    """Remove the header and docstring from the body."""
    # Split body into lines
    bodyLines = body.splitlines()

    # Remove the header
    bodyWithoutHeader = bodyLines[1:]  # Exclude the header line

    # If a docstring exists, remove it
    if docstring:
        # Identify the opening and closing quotes
        if docstring.startswith('"""') or docstring.startswith("'''"):
            docstringQuotes = docstring[:3]  # Get the quote type (either """ or ''')
            # Remove the lines that contain the docstring
            bodyWithoutDocstring = [
                line for line in bodyWithoutHeader
                if not line.strip().startswith(docstringQuotes)
            ]
        else:
            bodyWithoutDocstring = bodyWithoutHeader
    else:
        bodyWithoutDocstring = bodyWithoutHeader

    return "\n".join(bodyWithoutDocstring).strip()  # Join back into a single string


def splitCodeLine(s):
    # Updated Regex:
    # 1. '([^']*)'   -> Match anything inside single quotes.
    # 2. "([^"]*)"   -> Match anything inside double quotes.
    # 3. (\[.*?\])   -> Match anything inside square brackets.
    # 4. (\(.*?\))   -> Match anything inside parentheses.
    # 5. [^.\s]+     -> Match any non-dot and non-space sequence outside quotes/brackets.
    # 6. ([\s.])     -> Match spaces or dots as separate groups (the delimiters).

    pattern = r'\'[^\']*\'|"[^"]*"|\[.*?\]|\(.*?\)|[^.\s]+|[\s.]'

    # Find all matches including delimiters (spaces and dots)
    matches = re.findall(pattern, s)

    return matches


def splitCode(funcs, minWordsToRemove=3, maxWordsToRemove=9, limit=MAX_FUNCS_PER_FILE):
    maxWordsToRemove *= 2
    random.shuffle(funcs)
    for i, func in enumerate(funcs[:limit]):
        body = func["body"].split("\n")
        validLines = [i for i, line in enumerate(body) if line.strip() and len(line.split()) > minWordsToRemove]

        if validLines:
            randomLineIdx = random.choice(validLines)  # Choose a random line with enough words
            words = splitCodeLine(body[randomLineIdx])  # Split the line into words

            # Determine a random number of words to remove between min and max
            numWordsToRemove = random.randrange(minWordsToRemove, min(maxWordsToRemove, len(words)), 1)

            if len(words) > numWordsToRemove:
                # Remove the last numWordsToRemove words and split into parts
                removedWords = words[-numWordsToRemove:]
                prefix = "".join(words[:-numWordsToRemove])
                suffix = ""  # No additional suffix after the removed words

                # Rebuild the body before and after the line with the removed words
                bodyBefore = "\n".join(body[:randomLineIdx])
                if bodyBefore:
                    bodyBefore += "\n"
                bodyAfter = "\n".join(body[randomLineIdx + 1:])
                if bodyAfter:
                    bodyAfter = "\n" + bodyAfter

                # Append to the result
                funcs[i]["body"] = {
                    "bodyBefore": bodyBefore,
                    "prefix": prefix,
                    "removedWords": "".join(removedWords),
                    "bodyAfter": bodyAfter,
                    "numWordsRemoved": (numWordsToRemove + 1) // 2
                }

    return funcs[:limit]


if __name__ == "__main__":
    if len(sys.argv) > 2:
        directoryToSearch = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        print("Insufficient number of arguments provided.")
        exit(-1)

    pythonFiles = findPythonFiles(directoryToSearch)
    dataset = [{"file": file, "contents": splitCode(extractFunctionsFromFile(file))} for file in pythonFiles]

    with open(outputFile, "w") as jsonFile:
        json.dump(dataset, jsonFile, indent=4)

    print(f"Dataset has been written to {outputFile}")
