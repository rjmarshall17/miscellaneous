#!/usr/bin/env python3

import string

"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a" 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


# The time complexity of the brute force method is O(N^3) because we
# are going through the string in a nested for loop O(N^2) and we need
# to reverse the individual pieces of the string to see if it's a
# palindrome, or not, which is O(N). So, technically the time
# complexity is: O(N*N*N), i.e. O(N^3).
# We assume that the incoming string will not have any spaces or
# punctuation marks, just numbers and letters.
def brute_force_longest_palindrome(string_in: str) -> str:
    if len(string_in) == 1:
        return string_in
    string_to_check = string_in.lower()
    longest_palindrome = ''
    for index in range(len(string_to_check)):
        for index2 in range(index+1,len(string_to_check) + 1):
            # print("index=%d index2=%d" % (index, index2))
            if string_to_check[index:index2] == string_to_check[index:index2][::-1]:
                if index2 - index > len(longest_palindrome):
                    longest_palindrome = string_to_check[index:index2]
                    # print("Current longest palindrome: %s" % longest_palindrome)
    return longest_palindrome


def getLongestPalindromeFrom(string,leftIdx,rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]

# The time complexity for this is: O(n^2). It's better than the brute
# force method, but it's still not great.
def longest_palindrome(string_in: str) -> str:
    # Before doing anything else, check if the incoming string as a whole is
    # a palindrome and, if so, return it.
    # For the problem as described, all that would be necessary is: string_in.lower()
    if string_in == string_in[::-1]:
        return string_in
    # This is a special case where the incoming string is only two characters and
    # it is not already a palindrome. Because the problem description says that the
    # result for this particular case, i.e. 'ac', should be: 'a', we return the 0th
    # character from the string.
    if len(string_in) == 2:
        return string_in[0]

    currentLongest = [0, 1]
    for i in range(1, len(string_in)):
        odd = getLongestPalindromeFrom(string_in, i - 1, i + 1)
        even = getLongestPalindromeFrom(string_in, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        # print("odd=%s even=%s longest=%s currentLongest=%s" % (odd,
        #                                                        even,
        #                                                        longest,
        #                                                        currentLongest))
    return string_in[currentLongest[0]:currentLongest[1]]


def print_numbered_array(array):
    l = len(array)
    for i in range(l):
        print('{:^5}'.format(str(i)), end='')
    print()
    for i in range(l):
        print('{:^5}'.format(str(array[i])), end='')
    print()

# Manacher algorithm
# This is based on the pseudo code at: https://seedbx.com/understanding-manachers-algorithm/
# http://en.wikipedia.org/wiki/Longest_palindromic_substring
# https://tarokuriyama.com/projects/palindrome2.php
# The advantage of this algorithm is that finding the longest palindrome has
# a time complexity of O(N) and a space complexity of O(N+M) where N is the
# length of the incoming string and M is the number of delimiters added for
# the new string. The time complexity for that is O(N) for the join and O(N+M)
# where N is the number of characters in the string (after the join) plus
# the number of additional characters. There seems to be some confusion around
# how Python concatenates strings. Some suggest using joins, but in a quick
# timeit test I did the the joins, as opposed to '' + '', took slightly longer.
def manacher_palindromes(string_in: str) -> str:
    # If the length of the incoming string is less than 2, just return it
    if len(string_in) < 2:
        return string_in

    # If the incoming string is already a palindrome, just return it
    if string_in == string_in[::-1]:
        return string_in

    # First we transform the incoming string to have hash marks, '#', in between
    # each letter at the even positions, i.e. 0, 2, 4... The delimiter can be any
    # character that is NOT in the incoming string.
    delimiter = '#'
    new_string = delimiter + delimiter.join(string_in) + delimiter
    # print_numbered_array(new_string)
    new_string_length = len(new_string)

    palindrome_lengths = [0] * new_string_length
    center = 0
    right = 0
    for index in range(new_string_length):
        mirror = (2 * center) + 1
        # print("index=%d right=%d" % (index, right))
        if index < right:
            # print("Updating palindrome lengths at index %d with: %d" % (index,
            #                                                             min(right - 1, palindrome_lengths[mirror])))
            palindrome_lengths[index] = min(right - 1, palindrome_lengths[mirror])
        while ((index + (1 + palindrome_lengths[index])) < new_string_length and
               new_string[index + (1 + palindrome_lengths[index])] ==
               new_string[index - (1 + palindrome_lengths[index])]):
            # print("Incrementing palindrome lengths at index %d" % index)
            palindrome_lengths[index] += 1
        # If we move past the current right index, update both the center
        # and the right.
        if index + palindrome_lengths[index] > right:
            center = index
            right = 1 + palindrome_lengths[index]
    print_numbered_array(new_string)
    print_numbered_array(palindrome_lengths)
    longest = max(palindrome_lengths)
    # We need to subtract 1 here because of the initial character
    # that was added to the string.
    center = (palindrome_lengths.index(longest) // 2)
    half_word = longest // 2
    start, end = center - half_word, center + half_word
    end += 0 if longest % 2 == 0 else 1
    return string_in[start:end]

EXAMPLE_INPUTS = [
    'babad',
    'cbbd',
    'a',
    'ac',
    'racecarfred',
    'FA nut for a jar of tuna.G',
    'baddad'
]

EXPECTED_RESULTS = [
    ['bab', 'aba'],
    ['bb'],
    ['a'],
    ['a', 'c'],
    ['racecar'],
    ['anutforajaroftuna'],
    ['adda'],
]


if __name__ == '__main__':
    translate_table = str.maketrans('', '', string.punctuation + ' ')
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        if i:
            print('-'*80)
        input_data = input_data.translate(translate_table).lower()
        print("input_data=%s" % input_data)
        result = brute_force_longest_palindrome(input_data)
        result2 = longest_palindrome(input_data)
        result3 = manacher_palindromes(input_data)
        print("Brute force result=%s center out index result2=%s Manacher algorithm result3=%s" % (result,
                                                                                                   result2,
                                                                                                   result3))
        output = "The result (%s) for %s {} match the expected result: %s" % (result,
                                                                              input_data,
                                                                              EXPECTED_RESULTS[i])
        assert result in EXPECTED_RESULTS[i], output.format("does not (1)")
        assert result2 in EXPECTED_RESULTS[i], output.format("does not (2)")
        assert result3 in EXPECTED_RESULTS[i], output.format("does not (3)")
        print(output.format("does"))