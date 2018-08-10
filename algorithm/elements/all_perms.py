from itertools import permutations

def all_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        sub_sols = all_permutations(s[0:-1])
        result = []
        for sub_sol in sub_sols:
            for i in range(len(sub_sol)+1):
                result.append(sub_sol[:i] + s[-1] + sub_sol[i:])
        return result

if __name__ == '__main__':
    print(all_permutations('abcd'))
    print([''.join(f) for f in permutations('abcd')])
    #assert all_permutations('abcd') == [''.join(f) for f in permutations('abcd')]