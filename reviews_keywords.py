#!/usr/bin/env python3

"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular
k keywords in order of most to least frequently mentioned. The comparison of strings
is case-insensitive.

Multiple occurrences of a keyword in a review should be considered as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.
"""

# Input
k = [
    2,
    2,
]

keywords = [
    ['anacell', 'cetracular', 'betacellular'],
    ['anacell', 'betacellular', 'cetracular', 'deltacellular', 'eurocell']
]
reviews = [
    [
        'Anacell provides the best services in the city',
        'betacellular has awesome services',
        'Best services provided by anacell, everyone should use anacell',
    ],
    [
        'I love anacell Best services; Best services provided by anacell',
        'betacellular has great services',
        'deltacellular provides much better services than betacellular',
        'cetracular is worse than anacell',
        'Betacellular is better than deltacellular.',
    ],
]


# Time complexity: O(k*r)
def get_keywords(number_of_keywords, keywords, reviews):
    keyword_counts = {}
    for review in reviews:
        for keyword in keywords:
            if keyword.lower() in review.lower():
                if keyword in keyword_counts:
                    keyword_counts[keyword] += 1
                else:
                    keyword_counts[keyword] = 1
    # Sorting the results and reversing it is most likely O(nlogn) at a minimum, but since I do both,
    # it may be considered to be O(2*nlogn) which is still O(nlogn), however the overall time complexity
    # is still O(k*r)
    counts = list(reversed(sorted(sorted([(v, k) for k,v in keyword_counts.items()],key=lambda v: v[1]))))
    if len(counts) == number_of_keywords:
        return [x[1] for x in counts]
    return_counts = []
    for index in range(len(counts) - 1):
        if counts[index][0] > counts[index+1][0]:
            return_counts.append(counts[index][1])
        elif counts[index][0] == counts[index+1][0]:
            return_counts.extend([x[1] for x in sorted([counts[index],counts[index+1]],key=lambda x: x[1])])
        if len(return_counts) >= number_of_keywords:
            break
    return return_counts[:number_of_keywords]


if __name__ == '__main__':
    for index in range(len(keywords)):
        results = get_keywords(k[index], keywords[index], reviews[index])
        print("For %d got results: %s" % (index,results))
