def edit_distance(s1, s2):
    pass

if __name__ == '__main__':
    s1, s2 = 'cat', 'cut'
    assert edit_distance(s1, s2) == 1

    s1, s2 = 'sunday', 'saturday'
    assert edit_distance(s1, s2) == 3

    s1, s2 = 'geek', 'gesek'
    assert edit_distance(s1, s2) == 1

