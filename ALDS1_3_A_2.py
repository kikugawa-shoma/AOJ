from collections import deque
formula=input().split()
N=len(formula)

q=deque()
i=0

def calculation(operator):
    a=q.pop()
    b=q.pop()
    q.append(str(eval("".join([b,operator,a]))))

while i < N:
    char=formula[i]
    if char=="+" or char=="-" or char == "*":
        calculation(char)
    else:
        q.append(char)
    i += 1

print(q.pop())

