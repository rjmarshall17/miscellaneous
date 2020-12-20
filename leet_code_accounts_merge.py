#!/usr/bin/env python3

from collections import defaultdict
from typing import List
from pprint import pprint

"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element 
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if 
there is some email that is common to both accounts. Note that even if two accounts have the same 
name, they may belong to different people as people could have the same name. A person can have 
any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of 
each account is the name, and the rest of the elements are emails in sorted order. The accounts 
themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation: 

The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], 
['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] 
would still be accepted.

Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""


# Set up a UnionFind, Disjoint Set Union, with path compression in the find
class UnionFind:
    def __init__(self, number):
        self.ids = list(range(number))

    def find(self, index):
        while index != self.ids[index]:
            self.ids[index] = self.ids[self.ids[index]]
            index = self.ids[index]
        return index

    def union(self, first, second):
        first, second = self.find(first), self.find(second)
        self.ids[first] = self.ids[second]


def merge_accounts(accounts: List[List[str]]) -> List[List[str]]:
    # First map the names to the emails
    email_to_name = dict()
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name

    # Set up unique integer IDs for each email
    email_to_ids = {email: index for index, email in enumerate(email_to_name.keys())}

    # Create the union find which will union all emails for the same account
    uf = UnionFind(len(email_to_ids))
    # pprint(accounts)
    for account in accounts:
        for email in account[2:]:
            uf.union(email_to_ids[account[1]], email_to_ids[email])

    users = defaultdict(list)
    for email in email_to_name:
        users[uf.find(email_to_ids[email])].append(email)
    # pprint(users)

    # Create the return value by adding the name to the sorted list
    # of email addresses.
    merge_result = []
    for emails in users.values():
        merge_result.append([email_to_name[emails[0]]] + sorted(emails))
    return merge_result


EXAMPLE_INPUT = [
    [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ],
]

EXPECTED_RESULTS = [
    [
        ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"]
    ],
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUT):
        result = merge_accounts(input_data)
        assert result == EXPECTED_RESULTS[i], \
            "The returned result:\n%s\nDoes not match:\n%s" % (result,
                                                               EXPECTED_RESULTS[i])
        print("The result:")
        pprint(result)
        print("Matches the expected result:")
        pprint(EXPECTED_RESULTS[i])
