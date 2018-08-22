class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __hash__(self):
        return hash(self.first_name)

    def __lt__(self, other):
        return self.first_name < other.first_name \
            if self.first_name != other.first_name \
            else self.last_name < other.last_name

    def __repr__(self):
            return '(' + self.first_name + ', ' + self.last_name + ')'


def remove_first_name_duplicate(A):
    A.sort()
    write_idx = 1
    for cnd in A[1:]:
        if cnd != A[write_idx -1]:
            A[write_idx] = cnd
            write_idx += 1
    
    del A[write_idx:]

def remove_first_name_with_extra_storage(A):
    unique_names = set()
    for name in A:
        unique_names.add(name)
    
    return list(unique_names)

if __name__ == '__main__':
    data = [Name('Ian', 'Botham'), Name('David', 'Gower'), Name('Ian', 'Bell')]
    remove_first_name_duplicate(data)
    print(data)

    data = [Name('Ian', 'Botham'), Name('David', 'Gower'), Name('Ian', 'Bell')]
    print(remove_first_name_with_extra_storage(data))
    #print(data)
