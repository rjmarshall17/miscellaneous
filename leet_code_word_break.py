#!/usr/bin/env python3

from functools import wraps

"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine 
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]

Output: true

Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]

Output: true

Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]

Output: false

"""


# Use a trie to determine if each sub word within the string is a valid word according to the
# dictionary we received.

# Let's look at time complexities:
# For building the trie the time complexity is: O(nm) where n is the number
# of keys in the trie and m is the length of the longest key.
# For searching, inserting and deleting the time is: O(an) where n is the
# total number of words in the trie and a is the length of the word being
# searched, inserted or deleted.
class Trie:
    WORD_TERMINATOR = '*'

    def __init__(self):
        self.root = {}

    def add(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {'count':0}
            current_node = current_node[letter]
            current_node['count'] += 1
        current_node[Trie.WORD_TERMINATOR] = True

    def search(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        if Trie.WORD_TERMINATOR not in current_node:
            return False
        return True


# Define a decorator for the recursive function that will check if we've already seen a "word"
def track_words(func):
    memo = {}
    
    @wraps(func)
    def inner(*args):
        if (args,) not in memo:
            memo[(args,)] = func(*args)
            print("Added %s to memo" % (args,))
        return memo[(args,)]
    return inner
