#!/usr/bin/env python3

from collections import defaultdict
from typing import List
from string import punctuation

"""
819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in 
the list of banned words.  It is guaranteed there is at least one word that isn't banned, and 
that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in 
the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input:

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

Output: "ball"

Explanation: 

"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.

The answer is unique, and written in lowercase (even if its occurrences in paragraph may 
have uppercase symbols, and even if it is a proper noun.)

paragraph only consists of letters, spaces, or the punctuation symbols !?',;.

There are no hyphens or hyphenated words.

Words only consist of letters, never apostrophes or other punctuation symbols.
"""


# The time complexity is O(N + M) where N is the number of words in the paragraph
# and M is the number of banned words. At this point I assume that maketrans has
# a time complexity of O(X) where X is the number of characters being translated
# and the space complexity is: O(X) as well, more specifically 2X.
# The time complexity for translation is...unclear.
def most_common_word(paragraph: str, banned: List[str]) -> str:
    table = str.maketrans('', '', punctuation)
    words = defaultdict(int)
    for word in paragraph.translate(table).lower().split():
        words[word] += 1
    for word, count in reversed(sorted(words.items(), key=lambda item: item[1])):
        if word in banned:
            continue
        return word


EXAMPLE_INPUTS = [
    [
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        ['hit'],
    ],
]

EXPECTED_RESULTS = [
    'ball',
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = most_common_word(input_data[0], input_data[1])
        output = "The result (%s) {} match the expected result: %s" % (result,
                                                                       EXPECTED_RESULTS[i])
        assert result == EXPECTED_RESULTS[i], output.format('did not')
        print(output.format('did'))
