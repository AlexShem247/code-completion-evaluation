import unittest

from src.string_manipulation import *


class TestStringManipulations(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Hello World"), "HELLO WORLD")
        self.assertEqual(to_uppercase(""), "")
        self.assertEqual(to_uppercase("123"), "123")
        self.assertEqual(to_uppercase("already uppercase"), "ALREADY UPPERCASE")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Hello World"), "hello world")
        self.assertEqual(to_lowercase(""), "")
        self.assertEqual(to_lowercase("123"), "123")
        self.assertEqual(to_lowercase("already lowercase"), "already lowercase")

    def test_capitalize_first(self):
        self.assertEqual(capitalize_first("hello"), "Hello")
        self.assertEqual(capitalize_first("hello world"), "Hello world")
        self.assertEqual(capitalize_first("HELLO"), "Hello")
        self.assertEqual(capitalize_first("123abc"), "123abc")
        self.assertEqual(capitalize_first(""), "")

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("HELLO WORLD"), "Hello World")
        self.assertEqual(title_case("hello"), "Hello")
        self.assertEqual(title_case("123abc title"), "123Abc Title")
        self.assertEqual(title_case(""), "")

    def test_count_substring(self):
        self.assertEqual(count_substring("hello world", "o"), 2)
        self.assertEqual(count_substring("abababab", "ab"), 4)
        self.assertEqual(count_substring("hello", "x"), 0)
        self.assertEqual(count_substring("", "a"), 0)
        self.assertEqual(count_substring("aaaa", "aa"), 2)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("hello world"), "helloworld")
        self.assertEqual(remove_whitespace(" a b c "), "abc")
        self.assertEqual(remove_whitespace(""), "")
        self.assertEqual(remove_whitespace("   "), "")
        self.assertEqual(remove_whitespace("no whitespaces"), "nowhitespaces")

    def test_replace_substring(self):
        self.assertEqual(replace_substring("hello world", "world", "there"), "hello there")
        self.assertEqual(replace_substring("aaa", "a", "b"), "bbb")
        self.assertEqual(replace_substring("hello", "x", "y"), "hello")
        self.assertEqual(replace_substring("", "a", "b"), "")
        self.assertEqual(replace_substring("aaa", "aa", "b"), "ba")

    def test_repeat_string(self):
        self.assertEqual(repeat_string("hello", 3), "hellohellohello")
        self.assertEqual(repeat_string("ab", 2), "abab")
        self.assertEqual(repeat_string("a", 5), "aaaaa")
        self.assertEqual(repeat_string("", 10), "")
        self.assertEqual(repeat_string("test", 0), "")

    def test_strip_string(self):
        self.assertEqual(strip_string("   hello world   "), "hello world")
        self.assertEqual(strip_string("no_whitespace"), "no_whitespace")
        self.assertEqual(strip_string("   leading"), "leading")
        self.assertEqual(strip_string("trailing   "), "trailing")
        self.assertEqual(strip_string(""), "")

    def test_split_string(self):
        self.assertEqual(split_string("hello world"), ["hello", "world"])
        self.assertEqual(split_string("a,b,c", ","), ["a", "b", "c"])
        self.assertEqual(split_string("no delimiter"), ["no", "delimiter"])
        self.assertEqual(split_string("split,me,again,", ","), ["split", "me", "again", ""])
        self.assertEqual(split_string(""), [""])

    def test_join_strings(self):
        self.assertEqual(join_strings(["hello", "world"], " "), "hello world")
        self.assertEqual(join_strings(["a", "b", "c"], ","), "a,b,c")
        self.assertEqual(join_strings(["single"]), "single")
        self.assertEqual(join_strings(["", "blank", ""], "-"), "-blank-")
        self.assertEqual(join_strings([], ","), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("MixedCASE vowels"), 6)

    def test_find_substring(self):
        self.assertEqual(find_substring("hello world", "world"), 6)
        self.assertEqual(find_substring("repeat repeat", "repeat"), 0)
        self.assertEqual(find_substring("no match here", "xyz"), -1)
        self.assertEqual(find_substring("caseSensitive", "Sensitive"), 4)
        self.assertEqual(find_substring("", "a"), -1)

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")
        self.assertEqual(remove_punctuation("No punctuation here"), "No punctuation here")
        self.assertEqual(remove_punctuation("...Ellipses..."), "Ellipses")
        self.assertEqual(remove_punctuation("What? This, too!"), "What This too")
        self.assertEqual(remove_punctuation(""), "")

    def test_swap_case(self):
        self.assertEqual(swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(swap_case("123"), "123")
        self.assertEqual(swap_case(""), "")
        self.assertEqual(swap_case("MiXeD CaSe"), "mIxEd cAsE")
        self.assertEqual(swap_case("UPPERlower"), "upperLOWER")

    def test_center_string(self):
        self.assertEqual(center_string("hello", 10, "-"), "--hello---")
        self.assertEqual(center_string("world", 8, "*"), "*world**")
        self.assertEqual(center_string("test", 4), "test")
        self.assertEqual(center_string("center", 6), "center")
        self.assertEqual(center_string("align", 10), "  align   ")

    def test_is_alpha(self):
        self.assertTrue(is_alpha("HelloWorld"))
        self.assertFalse(is_alpha("Hello World"))
        self.assertFalse(is_alpha("123"))
        self.assertFalse(is_alpha("Hello123"))
        self.assertTrue(is_alpha("alpha"))

    def test_is_digit(self):
        self.assertTrue(is_digit("123456"))
        self.assertFalse(is_digit("123 456"))
        self.assertFalse(is_digit("Hello123"))
        self.assertTrue(is_digit("007"))
        self.assertFalse(is_digit("test"))

    def test_is_alphanumeric(self):
        self.assertTrue(is_alphanumeric("Hello123"))
        self.assertFalse(is_alphanumeric("Hello 123"))
        self.assertFalse(is_alphanumeric("!@#"))
        self.assertTrue(is_alphanumeric("alphanumeric"))
        self.assertTrue(is_alphanumeric("123456"))

    def test_pad_left(self):
        self.assertEqual(pad_left("hello", 10, "-"), "-----hello")
        self.assertEqual(pad_left("world", 8, "*"), "***world")
        self.assertEqual(pad_left("pad", 5), "  pad")
        self.assertEqual(pad_left("left", 4), "left")
        self.assertEqual(pad_left("fit", 2), "fit")

    def test_pad_right(self):
        self.assertEqual(pad_right("hello", 10, "-"), "hello-----")
        self.assertEqual(pad_right("world", 8, "*"), "world***")
        self.assertEqual(pad_right("pad", 5), "pad  ")
        self.assertEqual(pad_right("right", 5), "right")
        self.assertEqual(pad_right("fit", 2), "fit")

    def test_truncate_string(self):
        self.assertEqual(truncate_string("hello world", 5), "hello")
        self.assertEqual(truncate_string("truncate", 8), "truncate")
        self.assertEqual(truncate_string("short", 10), "short")
        self.assertEqual(truncate_string("exactly", 7), "exactly")
        self.assertEqual(truncate_string("", 5), "")

    def test_alternate_case(self):
        self.assertEqual(alternate_case("hello"), "hElLo")
        self.assertEqual(alternate_case("world"), "wOrLd")
        self.assertEqual(alternate_case(""), "")
        self.assertEqual(alternate_case("abcdefg"), "aBcDeFg")
        self.assertEqual(alternate_case("HELLO"), "hElLo")

    def test_remove_duplicate_words(self):
        self.assertEqual(remove_duplicate_words("hello world hello"), "hello world")
        self.assertEqual(remove_duplicate_words("no duplicates here"), "no duplicates here")
        self.assertEqual(remove_duplicate_words("repeat repeat repeat"), "repeat")
        self.assertEqual(remove_duplicate_words("a a a b b c"), "a b c")
        self.assertEqual(remove_duplicate_words(""), "")

    def test_most_frequent_char(self):
        self.assertEqual(most_frequent_char("hello"), "l")
        self.assertEqual(most_frequent_char("abracadabra"), "a")
        self.assertEqual(most_frequent_char("xyz"), "x")
        self.assertEqual(most_frequent_char(""), "")
        self.assertEqual(most_frequent_char("aabbcc"), "a")  # First in tie

    def test_wrap_text(self):
        self.assertEqual(wrap_text("This is a simple wrap test", 10), "This is a\nsimple\nwrap test")
        self.assertEqual(wrap_text("Hello world", 5), "Hello\nworld")
        self.assertEqual(wrap_text("Short text", 20), "Short text")
        self.assertEqual(wrap_text("Wrap this long sentence nicely", 8), "Wrap\nthis\nlong\nsentence\nnicely")
        self.assertEqual(wrap_text("", 5), "")

    def test_longest_word(self):
        self.assertEqual(longest_word("Find the longest word in this sentence"), "sentence")
        self.assertEqual(longest_word("Short words only"), "Short")
        self.assertEqual(longest_word("one two three"), "three")
        self.assertEqual(longest_word(""), "")
        self.assertEqual(longest_word("a ab abc"), "abc")

    def test_censor_words(self):
        self.assertEqual(censor_words("This is a bad word", {"bad"}), "This is a *** word")
        self.assertEqual(censor_words("Sensitive words are here", {"sensitive", "words"}), "********* ***** are here")
        self.assertEqual(censor_words("All clean here", {"not", "in", "text"}), "All clean here")
        self.assertEqual(censor_words("Word repeated word", {"word"}), "**** repeated ****")
        self.assertEqual(censor_words("", {"any"}), "")

    def test_reverse_words_order(self):
        self.assertEqual(reverse_words_order("Hello world"), "world Hello")
        self.assertEqual(reverse_words_order("Python is fun"), "fun is Python")
        self.assertEqual(reverse_words_order("single"), "single")
        self.assertEqual(reverse_words_order("  multiple   spaces  "), "spaces multiple")
        self.assertEqual(reverse_words_order(""), "")

    def test_find_longest_palindromic_substring(self):
        self.assertEqual(find_longest_palindromic_substring("babad"), "bab")  # or "aba"
        self.assertEqual(find_longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(find_longest_palindromic_substring("a"), "a")
        self.assertEqual(find_longest_palindromic_substring(""), "")
        self.assertEqual(find_longest_palindromic_substring("racecar"), "racecar")

    def test_compress_string(self):
        self.assertEqual(compress_string("aaabbc"), "a3b2c")
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("ccccc"), "c5")
        self.assertEqual(compress_string("ab"), "ab")

    def test_expand_compressed_string(self):
        self.assertEqual(expand_compressed_string("a2b3"), "aabbb")
        self.assertEqual(expand_compressed_string("c3"), "ccc")
        self.assertEqual(expand_compressed_string("d"), "d")
        self.assertEqual(expand_compressed_string("x1y2z3"), "xyyzzz")
        self.assertEqual(expand_compressed_string("a10"), "aaaaaaaaaa")

    def test_snake_to_camel_case(self):
        self.assertEqual(snake_to_camel_case("snake_case"), "snakeCase")
        self.assertEqual(snake_to_camel_case("another_example_here"), "anotherExampleHere")
        self.assertEqual(snake_to_camel_case("alreadyCamelCase"), "alreadyCamelCase")
        self.assertEqual(snake_to_camel_case(""), "")
        self.assertEqual(snake_to_camel_case("singleword"), "singleword")

    def test_camel_to_snake_case(self):
        self.assertEqual(camel_to_snake_case("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake_case("thisIsATest"), "this_is_a_test")
        self.assertEqual(camel_to_snake_case("already_snake_case"), "already_snake_case")
        self.assertEqual(camel_to_snake_case("singleWord"), "single_word")
        self.assertEqual(camel_to_snake_case(""), "")

    def test_mask_sensitive_info(self):
        self.assertEqual(mask_sensitive_info("My email is test@example.com"), "My email is tes****@example.com")
        self.assertEqual(mask_sensitive_info("Call me at 1234567890"), "Call me at 123****90")
        self.assertEqual(mask_sensitive_info("Reach out at john.doe@mail.com or 9876543210"), "Reach out at john.doe@mail.com or 987****10")
        self.assertEqual(mask_sensitive_info("No sensitive info here"), "No sensitive info here")
        self.assertEqual(mask_sensitive_info("Contact: myname@domain.com"), "Contact: myn****@domain.com")

    def test_find_anagrams(self):
        self.assertEqual(find_anagrams("listen", ["enlist", "google", "inlets"]), ["enlist", "inlets"])
        self.assertEqual(find_anagrams("evil", ["vile", "live", "veil"]), ["vile", "live", "veil"])
        self.assertEqual(find_anagrams("apple", ["pale", "peal", "leap"]), [])
        self.assertEqual(find_anagrams("abc", ["cab", "bac", "cba"]), ["cab", "bac", "cba"])
        self.assertEqual(find_anagrams("a", ["a", "b", "c"]), ["a"])

    def test_word_wrap_with_indent(self):
        self.assertEqual(word_wrap_with_indent("This is a long line of text that needs wrapping.", 20, 4),
                         "    This is a long\n    line of text\n    that needs\n    wrapping.")
        self.assertEqual(word_wrap_with_indent("Short line", 20, 2), "  Short line")
        self.assertEqual(word_wrap_with_indent("A line that is exactly twenty characters.", 20, 2),
                         "  A line that is\n  exactly twenty\n  characters.")
        self.assertEqual(word_wrap_with_indent("A quick brown fox", 10, 0), "A quick\nbrown fox")
        self.assertEqual(word_wrap_with_indent("", 10, 0), "")

    def test_count_word_frequencies(self):
        self.assertEqual(count_word_frequencies("Hello world hello"), {'hello': 2, 'world': 1})
        self.assertEqual(count_word_frequencies("This is a test this is only a test"),
                         {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1})
        self.assertEqual(count_word_frequencies(""), {})
        self.assertEqual(count_word_frequencies("word word WORD"), {'word': 3})
        self.assertEqual(count_word_frequencies("Case insensitivity test case"),
                         {'case': 2, 'insensitivity': 1, 'test': 1})


if __name__ == "__main__":
    unittest.main()
