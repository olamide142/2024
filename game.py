# boxes = [
#     [1, 5, 9, 13],
#     [2, 6, 10, 14],
#     [3, 7, 11, 15],
#     [4, 8, 12, 16]
# ]
# a = [boxes[i][0] for i in range(4)]
# b = [boxes[i][1] for i in range(4)]
# c = [boxes[i][2] for i in range(4)]
# d = [boxes[i][3] for i in range(4)]

# print(a,b,c,d)

a = [5, 5, 5, 5]

stack = []

# def stack_it_right(data):
#     for datum in data[::-1]:
#         if len(stack) == 0:
#             stack.append(datum)
#         elif stack[len(stack)-1] == datum:
#             stack[len(stack)-1] += datum
#         else:
#             stack.append(datum)
#     if len(stack) != 4:
#         for i in range(4 - len(stack)):
#             stack.append(0)

#     return stack[::-1]
# print(stack_it_right(a))    



def stack_it_left(data):
    for datum in data:
        if len(stack) 

