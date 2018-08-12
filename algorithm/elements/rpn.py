def rpn(expression):
    evaluator = []
    OPERATORS = {
        '+': lambda x, y: y + x,
        '-': lambda x, y: y - x,
        '*': lambda x, y: y * x,
        '/': lambda x, y: y / x
    }
    for token in expression.split(','):
        if token in OPERATORS:
            evaluator.append(OPERATORS[token](
                evaluator.pop(), evaluator.pop()))
        else:
            evaluator.append(int(token))
    assert len(evaluator) == 1
    return evaluator.pop()


if __name__ == '__main__':
    ex1 = '3,2,-'  # 1
    assert rpn(ex1) == 1

    ex2 = '3,11,5,+,-'  # -13
    assert rpn(ex2) == -13

    ex3 = '2,3,11,+,5,-,*'  # 18
    assert rpn(ex3) == 18

    ex4 = '6,3,-,2,^,11,-'  # -2
    #assert rpn(ex1) == 1