import math


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x and y."""
    return x / y


def square_root(x):
    """Return the square root of x."""
    return math.sqrt(x)


def power(base, exponent):
    """Return base raised to the power of exponent."""
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def factorial(n):
    """Return the factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def area_of_circle(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius ** 2)


def gcd(a, b):
    """Return the greatest common divisor of a and b using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)


def is_palindrome(s):
    """Return True if s is a palindrome, else False."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def transpose_matrix(matrix):
    """Return the transpose of a given matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def merge_sorted_lists(list1, list2):
    """Return a new sorted list by merging two sorted lists."""
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def prime_factors(n):
    """Return a list of the prime factors of n."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


def calculate_mean(numbers):
    """Return the mean of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0


def find_median(numbers):
    """Return the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    mid = count // 2
    if count % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def count_vowels(s):
    """Return the number of vowels in a given string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_anagram(str1, str2):
    """Return True if str1 and str2 are anagrams, else False."""
    cleaned_str1 = sorted(str1.replace(' ', '').lower())
    cleaned_str2 = sorted(str2.replace(' ', '').lower())
    return cleaned_str1 == cleaned_str2


def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers up to the given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit + 1, number):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def fibonacci_sequence(n):
    """Return a list of the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_valid_email(email):
    """Return True if the email address is valid, else False."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def merge_dictionaries(dict1, dict2):
    """Return a new dictionary that merges two dictionaries."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values if the key exists
        else:
            merged[key] = value
    return merged


def find_longest_word(words):
    """Return the longest word from a list of words."""
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def quicksort(arr):
    """Return a sorted list using the quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def longest_common_subsequence(str1, str2):
    """Return the longest common subsequence of str1 and str2."""
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def dijkstra(graph, start):
    """Return the shortest path distances from start to all other nodes in the graph."""
    import heapq
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


def matrix_multiplication(matrix_a, matrix_b):
    """Return the product of two matrices."""
    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def knapsack(weights, values, capacity):
    """Return the maximum value that can be obtained from the knapsack problem."""
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]
