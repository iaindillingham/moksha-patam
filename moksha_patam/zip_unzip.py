"""
This example demonstrates how to zip two lists into one list of two-tuples
and then unzip this list into two lists.

I needed this example when filtering responses to questions. I wanted to retain
a response when both Rater A and Rater B had labelled it "accept". However,
I wanted two lists -- one for Rater A and one for Rater B -- for computing
inter-rater reliability (not shown).
"""
import collections

# Model a response to a question as a named tuple
Response = collections.namedtuple("Response", ["question", "label"])

# Rater A's responses to three questions
rater_a_responses = [
    Response(1, "accept"),
    Response(2, "accept"),
    Response(3, "ignore"),
]

# Rater B's responses to three questions
rater_b_responses = [
    Response(1, "accept"),  # Same
    Response(2, "accept"),  # Same
    Response(3, "reject"),  # Different
]

# Which responses have been accepted by both Rater A and Rater B?
# This is a list of two-tuples, where t[0] is Rater A and t[1] is Rater B.
both_accept = [
    x
    for x in zip(rater_a_responses, rater_b_responses)
    if x[0].label == "accept" and x[1].label == "accept"
]

assert len(both_accept) == 2

# How do we separate this list into two lists, one for Rater A
# and one for Rater B? In other words, how do we unzip this list?
rater_a_accept, rater_b_accept = zip(*both_accept)

assert len(rater_a_accept) == 2
assert len(rater_b_accept) == 2
