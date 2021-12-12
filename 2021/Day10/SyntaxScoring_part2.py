import sys

with open('sample.txt', 'r') as file:
    navigation = list(file.read().split('\n'))

legalpairs = {'(':')', '[':']', '{':'}', '<':'>'}
open = ['(', '[', '{', '<']
erroscore = {')':1, ']':2, '}':3, '>':4}

completion = []
for line in navigation:
    flag = None
    stack = []
    for symbol in line:
        if symbol in open:
            stack.append(legalpairs[symbol])
        elif symbol == stack[-1]:
            stack.pop()
        else:
            flag = symbol
            break
    if flag is None:
        completion.append(stack)
    
totalscores = []
for line in completion:
    line.reverse()
    score = 0
    for symbol in line:
        score = score * 5 + erroscore[symbol]
    totalscores.append(score)
totalscores.sort()

middle = len(totalscores) // 2

print(totalscores[middle])