import numpy as np

isnode = lambda x: type(x) == Node
getval = lambda x: x.val


def new_node(value, recipe):
    return Node(value, recipe)


def identity(x): return x


class Node(object):
    __slots__ = ['value', 'recipe']

    def __init__(self, value, recipe):
        self.value = value
        self.recipe = recipe

    def __str__(self):
        return 'Autograd {0} with value {1}'.format(
            type(self).__name__, self.value)


class Primitive(object):
    def __init__(self, fun):
        self.fun = fun
        self.vjps = {}

    def __call__(self, *args, **kwargs):
        argvals = list(args)
        parents = []
        for argnum, arg in enumerate(args):
            if isnode(arg):
                argvals[argnum] = arg.value
                parents.append((argnum, arg))
        result_value = self.fun(*argvals, **kwargs)
        return new_node(result_value, (self, args, kwargs, parents))

    def defvjp(self, vjpfun, argnum=0):
        self.vjps[argnum] = vjpfun

    def vjp(self, argnum, outgrad, args, kwargs):
        return self.vjps[argnum]()


def forward_pass(fun, args, kwargs, argnum=0):
    args = list(args)
    x = args[argnum]
    if isnode(x):
        start_node = new_node(x.value, (identity, (x,), {}, [(0, x)]))
    else:
        start_node = new_node(x, (identity, (x,), {}, [(0, x)]))
    end_node = fun(*args, **kwargs)
    return start_node, end_node


if __name__ == '__main__':
    log = Primitive(np.log)
    add = Primitive(np.add)


    def my_func(x):
        return log(x)


    def y(x):
        return add(my_func(x), my_func(x))


    a, b = forward_pass(my_func, (23,), {})
    print(a)
    print(b)
