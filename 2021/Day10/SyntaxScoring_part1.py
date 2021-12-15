import sys

with open('input.txt', 'r') as file:
    navigation = list(file.read().split('\n'))

legalpairs = {'(':')', '[':']', '{':'}', '<':'>'}
open = ['(', '[', '{', '<']
erroscore = {')':3, ']':57, '}':1197, '>':25137}
erroscount = {')':0, ']':0, '}':0, '>':0}

for line in navigation:
    stack = []
    for symbol in line:
        if symbol in open:
            stack.append(legalpairs[symbol])
        elif symbol == stack[-1]:
            stack.pop()
        else:
            erroscount[symbol] += 1
            break

totalerrorscore = 0
for erro in erroscount:
    totalerrorscore += erroscount[erro] * erroscore[erro]

print(totalerrorscore)