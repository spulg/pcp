"""
input in the form of a list of tuples [[ab, b], [b, bb], [a, a], [b, b]]
"""


# generates all possible permutations of indices without memoization of previous length strings
def naive_pcp(tuples, depth=20):

    n = len(tuples)
    first_iteration = True
    indices = [[]]
    while depth > 1:
        depth -= 1
        if first_iteration:
            # otherwise first iteration will go over [[4], [3], [2], [1], [0]]
            indices = [[i] for i in range(n)]
            first_iteration = False
        else:
            indices = increment_depth(indices, list(range(n)))

        for index in indices:
            top_str = ""
            bot_str = ""
            for i in index:
                top_str += tuples[i][0]
                bot_str += tuples[i][1]
                if top_str == bot_str:
                    return [k + 1 for k in index]


"""
keep_old: add new sequences and don't throw away old ones of shorter length

The call [[0], [1], [2]], [0, 1, 2] yields 
[[2, 2], [1, 2], [0, 2], [2, 1], [1, 1], [0, 1], [2, 0], [1, 0], [0, 0]]
"""


def increment_depth(sequences: list, alphabet: list, keep_old=False):
    if keep_old:
        new_sequences = sequences
    else:
        new_sequences = []

    for seq in sequences:
        for a in alphabet:
            new_sequences = [[a] + seq] + new_sequences
    return new_sequences
