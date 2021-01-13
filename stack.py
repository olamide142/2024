def stack_it_right(data):
    stack = []
    for datum in data[::-1]:
        if len(stack) == 0:
            stack.append(datum)
        elif stack[len(stack)-1] == datum:
            stack[len(stack)-1] += datum
        else:
            stack.append(datum)
            while 1:
                if 0 in stack:
                    stack.pop(0)
                else: break

    if len(stack) != 4:
        for i in range(4 - len(stack)):
            stack.append(0)
    return stack[::-1]


def stack_it_left(data):
    stack = []
    for datum in data:
        if len(stack) == 0:
            stack.append(datum)
        elif stack[len(stack)-1] == datum:
            stack[len(stack)-1] += datum
        else:
            stack.append(datum)
            while 1:
                if 0 in stack:
                    stack.pop(0)
                else: break

    if len(stack) != 4:
        for i in range(4 - len(stack)):
            stack.append(0)
    return stack
