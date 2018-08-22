from collections import namedtuple


def find_closest_repetition(words):
    NeighborInfo = namedtuple('NeighborInfo',
                              ('best_dist', 'last_index'))
    word_info = {}
    for i in range(len(words)):
        if words[i] not in word_info:
            word_info[words[i]] = NeighborInfo(float('inf'), i)
        else:
            cct_neighber_info = word_info[words[i]]
            if cct_neighber_info.best_dist > (i - cct_neighber_info.last_index):
                word_info[words[i]] = NeighborInfo(
                    (i - cct_neighber_info.last_index), i)
            else:
                word_info[words[i]] = NeighborInfo(
                    cct_neighber_info.best_dist, i)
    return min([x.best_dist for x in word_info.values()])


if __name__ == '__main__':
    words = ['All', 'work', 'and', 'know', 'play',
             'makes', 'for', 'no', 'work', 'no', 'fun', 'and',
             'no', 'no', 'results']
    assert find_closest_repetition(words) == 1
