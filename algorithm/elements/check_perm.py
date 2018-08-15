from collections import defaultdict


def is_permutation(s1, s2):
    if s1 is None or s2 is None:
        return False

    if len(s1) != len(s2):
        return False

    s1_dict = defaultdict(int)
    s2_dict = defaultdict(int)

    for s in s1_dict:
        s1_dict[s] += 1
    for s in s2_dict:
        s2_dict[s] += 1
    return s1_dict == s2_dict
