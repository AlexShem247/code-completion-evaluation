def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]


def to_uppercase(s):
    """Converts all characters to uppercase."""
    return s.upper()


def to_lowercase(s):
    """Converts all characters to lowercase."""
    return s.lower()


def capitalize_first(s):
    """Capitalizes the first letter of the string."""
    return s.capitalize()


def title_case(s):
    """Converts the string to title case."""
    return s.title()


def count_substring(s, sub):
    """Counts occurrences of a substring."""
    return s.count(sub)


def is_palindrome(s):
    """Checks if the string is a palindrome."""
    return s == s[::-1]


def remove_whitespace(s):
    """Removes all whitespace from the string."""
    return "".join(s.split())


def replace_substring(s, old, new):
    """Replaces occurrences of a substring with another."""
    return s.replace(old, new)


def repeat_string(s, n):
    """Repeats the string n times."""
    return s * n


def strip_string(s):
    """Removes leading and trailing whitespace."""
    return s.strip()


def split_string(s, delimiter=" "):
    """Splits the string by a delimiter."""
    return s.split(delimiter)


def join_strings(strings, delimiter=" "):
    """Joins a list of strings with a delimiter."""
    return delimiter.join(strings)


def count_vowels(s):
    """Counts the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def find_substring(s, sub):
    """Finds the first occurrence of a substring."""
    return s.find(sub)


def remove_punctuation(s):
    """Removes punctuation from the string."""
    import string
    return "".join(char for char in s if char not in string.punctuation)


def swap_case(s):
    """Swaps the case of all characters in the string."""
    return s.swapcase()


def center_string(s, width, fillchar=" "):
    """Centers the string with a given fill character."""
    return s.center(width, fillchar)


def is_alpha(s):
    """Checks if the string contains only alphabetic characters."""
    return s.isalpha()


def is_digit(s):
    """Checks if the string contains only digits."""
    return s.isdigit()


def is_alphanumeric(s):
    """Checks if the string contains only alphanumeric characters."""
    return s.isalnum()


def pad_left(s, width, fillchar=" "):
    """Pads the string on the left with a fill character."""
    return s.rjust(width, fillchar)


def pad_right(s, width, fillchar=" "):
    """Pads the string on the right with a fill character."""
    return s.ljust(width, fillchar)


def truncate_string(s, max_length):
    """Truncates the string to a maximum length."""
    return s[:max_length] if len(s) > max_length else s


def alternate_case(s):
    """Alternates case of each letter in the string."""
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    return "".join(result)


def remove_duplicate_words(s):
    """Removes duplicate words from the string, keeping the first occurrence."""
    words = s.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)


def most_frequent_char(s):
    """Finds the most frequently occurring character in the string."""
    from collections import Counter
    if not s:
        return ""
    counts = Counter(s)
    most_common = counts.most_common(1)[0]
    return most_common[0]


def wrap_text(s, width):
    """Wraps text to a specific width."""
    lines = []
    while len(s) > width:
        line = s[:width].rsplit(" ", 1)[0]
        lines.append(line)
        s = s[len(line):].strip()
    lines.append(s)
    return "\n".join(lines)


def longest_word(s):
    """Finds the longest word in the string."""
    words = s.split()
    longest = max(words, key=len) if words else ""
    return longest


def censor_words(s, bad_words):
    """Censors specified words in the string with asterisks."""
    words = s.split()
    censored = [
        "*" * len(word) if word.lower() in bad_words else word
        for word in words
    ]
    return " ".join(censored)


def reverse_words_order(s):
    """Reverses the order of words in the string."""
    words = s.split()
    return " ".join(words[::-1])


def find_longest_palindromic_substring(s):
    """Finds the longest palindromic substring in the string."""

    longest = ""
    length = len(s)

    for i in range(length):
        # Check for odd-length palindromes
        left, right = i, i
        while left >= 0 and right < length and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1

        # Check for even-length palindromes
        left, right = i, i + 1
        while left >= 0 and right < length and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1

    return longest



def compress_string(s):
    """Compresses a string by collapsing consecutive characters."""
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    result.append(s[-1] + (str(count) if count > 1 else ""))
    return "".join(result)


def expand_compressed_string(s):
    """Expands a compressed string (like a2b3) into its full form (aabbb)."""
    import re
    result = []
    matches = re.findall(r"(\D)(\d*)", s)
    for char, count in matches:
        result.append(char * (int(count) if count else 1))
    return "".join(result)


def snake_to_camel_case(s):
    """Converts snake_case to camelCase."""
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


def camel_to_snake_case(s):
    """Converts camelCase to snake_case."""
    result = []
    for char in s:
        if char.isupper():
            result.append("_" + char.lower())
        else:
            result.append(char)
    return "".join(result)


def mask_sensitive_info(s):
    """Masks sensitive information, such as email or phone numbers."""
    import re
    s = re.sub(r'\b(\w{3})\w+@(\w+\.\w+)', r'\1****@\2', s)  # Mask email
    s = re.sub(r'\b(\d{3})\d+(\d{2})\b', r'\1****\2', s)  # Mask phone
    return s


def find_anagrams(word, candidates):
    """Finds anagrams of a word from a list of candidates."""
    word_sorted = sorted(word)
    return [candidate for candidate in candidates if sorted(candidate) == word_sorted]


def word_wrap_with_indent(s, width, indent=0):
    """Wraps text to a specific width with an optional indent."""
    lines = []
    while len(s) > width - indent:
        line = s[:width - indent].rsplit(" ", 1)[0]
        lines.append(" " * indent + line)
        s = s[len(line):].strip()
    lines.append(" " * indent + s)
    return "\n".join(lines)

def count_word_frequencies(s):
    """Counts the frequency of each word in the string."""
    from collections import Counter
    words = s.lower().split()
    return dict(Counter(words))

