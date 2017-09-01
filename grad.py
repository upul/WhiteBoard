import numpy as np

isnode = lambda x: type(x) == Node
getval = lambda x: x.val
active_progenitors = set()


def new_node(value, recipe, progenitors):
    return Node(value, recipe, progenitors)


def new_progenitor(x):
    if isnode(x):
        node = new_node(x.value, (identity, (x,), {}, [(0, x)]), x.progenitors)
    else:
        node = new_node(x, (identity, (x,), {}, []), set())
    node.progenitors = node.progenitors | {node}
    return node


def identity(x): return x


# identity.defvjp(lambda g, ans, vs, gvs, x : g)


class Node(object):
    __slots__ = ['value', 'recipe', 'progenitors']

    def __init__(self, value, recipe, progenitors):
        self.value = value
        self.recipe = recipe
        self.progenitors = progenitors

    def __str__(self):
        return 'Autograd {0} with value {1} and {2} progenitors'.format(
            type(self).__name__, self.value, len(self.progenitors))


class Primitive(object):
    def __init__(self, fun):
        self.fun = fun
        self.vjps = {}

    def __call__(self, *args, **kwargs):
        argvals = list(args)
        progenitors = set()
        parents = []
        for argnum, arg in enumerate(args):
            if isnode(arg):
                argvals[argnum] = arg.value
                parents.append((argnum, arg))
                progenitors.update(arg.progenitors & active_progenitors)
        result_value = self.fun(*argvals, **kwargs)
        if progenitors:
            return new_node(result_value, (self, args, kwargs, parents), progenitors)
        else:
            return result_value


def forward_pass(fun, args, kwargs, argnum=0):
    args = list(args)
    start_node = new_progenitor(args[argnum])
    args[argnum] = start_node
    active_progenitors.add(start_node)
    end_node = fun(*args, **kwargs)
    active_progenitors.remove(start_node)
    return start_node, end_node

if __name__ == '__main__':
    log = Primitive(np.log)
    add = Primitive(np.add)
    def my_func(x):
        return add(log(x), log(x))
    a, b = forward_pass(my_func, (23,), {})
    print(a)
    print(b)
