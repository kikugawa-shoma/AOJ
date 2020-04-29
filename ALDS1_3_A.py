from collections import deque
formula=input().split()
N=len(formula)

q=deque()
i=0

def calculation(operand):
    if operand=="+":
        q.append(q.pop()+q.pop())
    if operand=="-":
        q.append(-q.pop()+q.pop())
    if operand=="*":
        q.append(q.pop()*q.pop())


while i < N:
    char=formula[i]
    if char=="+" or char=="-" or char == "*":
        calculation(char)
    else:
        q.append(int(char))
    i += 1

print(q.pop())

