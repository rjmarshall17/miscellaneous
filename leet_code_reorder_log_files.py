#!/usr/bin/env python3
from typing import List

'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digit_logs.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at
least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered
lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should
be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

CHECK_LOGS = [
              ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
              ["dig1 15 34 19 21", "let1 this is a test", "let2 another test", "dig3 1 5 67 14",
               "let1 how about another log"],
              ]

EXPECTED_OUTPUTS = [
                    ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
                    ['let2 another test', 'let1 how about another log', 'let1 this is a test',
                     'dig1 15 34 19 21', 'dig3 1 5 67 14'],
                    ]


def reorderLogFiles(logs: List[str]) -> List[str]:
    # Make sure to set up digit_logs and letter_logs outside of the loop
    # due to variable scope, i.e. if they are defined in the loop
    # they are unknown outside of it.
    digit_logs = []
    letter_logs = []
    for log_entry in logs:
        # Split the log entry into the ID and the data
        log_id, log_data = log_entry.split(maxsplit=1)
        # Check the data, minus any spaces, to see if all of the characters are digit_logs.
        # If they are, then append to the digit_logs list, else the "letter_logs" list.
        if log_data.replace(' ', '').isdigit():
            digit_logs.append(log_entry)
        else:
            letter_logs.append(log_entry)
    # Sort letter_logs, don't use letter_logs.sort() because that changes the list and doesn't return
    # a sorted list. That's why I use sorted() instead. Sort the logs based on the data,
    # followed by the ID of the entry. The digit_logs list can be left alone since it should
    # be returned in the order given.
    return sorted(letter_logs, key=lambda x: (x.split()[1:], x.split()[0])) + digit_logs


if __name__ == '__main__':
    for i, check_logs in enumerate(CHECK_LOGS):
        output = reorderLogFiles(logs=check_logs)
        assert output == EXPECTED_OUTPUTS[i]
        print("The output for index %d was correct:" % i)
        print(" Input was: %s" % check_logs)
        print("Output was: %s" % output)
