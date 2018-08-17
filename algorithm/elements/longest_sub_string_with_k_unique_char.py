from collections import defaultdict


def longest_sub_string_with_k_unique(str, k):
    unique_chars = defaultdict(int)
    j = 0
    max_len = 0
    for i in range(len(str)):
        unique_chars[str[i]] += 1

        if len(unique_chars) == k:
            max_len = max(max_len, i - j + 1)
        elif len(unique_chars) > k:
            while len(unique_chars) > k:
                end_char = str[j]
                if unique_chars[end_char] == 1:
                    unique_chars.pop(end_char, None)
                else:
                    unique_chars[end_char] -= 1
                j += 1
    return max_len


if __name__ == '__main__':
    print(longest_sub_string_with_k_unique('aabacbebebe', 3))
