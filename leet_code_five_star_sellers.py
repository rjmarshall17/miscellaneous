#!/usr/bin/env python3

from typing import List
from copy import deepcopy

"""
Third-party companies that sell their products on Amazon.com are able to analyze the customer reviews for
their products in real time. Imagine that Amazon is creating a category called "five-star sellers" that will
only display products sold by companies whose average percentage of five-star reviews per-product is at or
above a certain threshold. Given the number of five-star and total reviews for each product a company sells,
as well as the threshold percentage, what is the minimum number of additional fivestar reviews the company
needs to become a five-star seller?

For example, let's say there are 3 products (n = 3) where productRatings = [[4,4], [1,2], [3, 6]], and the
percentage ratings Threshold = 77. The first number for each product in productRatings denotes the number of
fivestar reviews, and the second denotes the number of total reviews. Here is how we can get the seller to
reach the threshold with the minimum number of additional five-star reviews:

Before we add more five-star reviews, the percentage for this seller is ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
If we add a five-star review to the second product, the percentage rises to ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
If we add another five-star review to the second product, the percentage rises to ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
If we add a five-star review to the third product, the percentage rises to ((4/4) + (3/4) + (4/7))/3 = 77.38%
At this point, the threshold of 77% has been met. Therefore, the answer is 3 because that is the minimum number
of additional five-star reviews the company needs to become a five-star seller.

Function Description

Complete the function fiveStarReviews in the editor below.

fiveStarReviews has the following parameters:

int productRatings[n][2]: a 2-dimensional array of integers where the ith element contains two values, the
first one denoting fivestar[i] and the second denoting total[i]

int ratingsThreshold: the threshold percentage, which is the average percentage of five-star reviews the 
products need for the company to be considered a five-star seller

Returns:

int: the minimum number of additional five-star reviews the company needs to meet the threshold ratingsThreshold

Constraints

1 <= n <=200
0 <= fivestar < total <= 100
1 <= ratingsThreshold < 100
The array productRatings contains only non-negative integers.
"""

EXAMPLE_INPUTS = [
    ([[4,4], [1,2], [3,6]], 0.77),
    ([[9, 10]], 0.91),
    ([[1,3], [1,4]], 0.6),
]

EXPECTED_RESULTS = [
    3,
    2,
    6,
]


# The time complexity for this function is O(n*k) where n is the number of
# ratings and k is the number of additional five star ratings that would
# be needed to reach the provided threshold.
def five_star_reviews(ratings: List[List[int]], ratings_threshold: float) -> int:
    # Copying the incoming list to a new list has a time complexity of O(n) and space is O(n)
    product_ratings = deepcopy(ratings)
    add_stars = 0

    ratings_threshold = ratings_threshold * 100 if ratings_threshold < 1 else ratings_threshold
    current_percentage = (sum([x[0] / x[1] for x in product_ratings]) / len(product_ratings)) * 100
    # print("The current percentage is: %s and the threshold is: %s" % (current_percentage,
    #                                                                   ratings_threshold))
    if isinstance(product_ratings[0], tuple):
        product_ratings = [list(x) for x in product_ratings]
    # print("The product_ratings are: %s" % product_ratings)
    # Use a list and index into it since the time complexity of get/set
    # is O(1) and the space is O(1)
    rating_index = 0
    # The time complexity of the while loop is: O(n*k) where n = the number of
    # ratings and k is the number of additional five star ratings that are
    # needed to reach the threshold. The space here is O(1).
    while current_percentage < ratings_threshold:
        if rating_index >= len(product_ratings):
            rating_index = 0
        # If the ratings for this product are already all five star, then skip it.
        # We only add five star ratings to products that are not already 100%.
        # The time complexity of the following may not be that straightforward.
        # The get is O(1) but the comparison will require computing the percentage
        # of five star ratings to the total number of ratings. According to wikipedia,
        # the worst case time complexity for division is: O(n**2). And then we need
        # to do a float comparison which may have a time complexity of O(n) where
        # n is the number of bits needed to store the float values. In this case
        # I would assume that the time complexity of the following is O(n**2).
        if product_ratings[rating_index][0] / product_ratings[rating_index][1] >= 1:
            rating_index += 1
            continue
        product_ratings[rating_index][0] += 1
        product_ratings[rating_index][1] += 1
        add_stars += 1
        rating_index += 1
        current_percentage = (sum([x[0] / x[1] for x in product_ratings]) / len(product_ratings)) * 100
        # print("product_ratings are: %s current percentage: %s" % (product_ratings, current_percentage))
    return add_stars


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = five_star_reviews(input_data[0], input_data[1])
        print("The result was: %d" % result)
        print("  ratings: %s" % input_data[0])
        print("threshold: %s" % input_data[1])
        assert result == EXPECTED_RESULTS[i], \
            "The result (%d) does not match the expected result of: %d" % (result,
                                                                           EXPECTED_RESULTS[i])
