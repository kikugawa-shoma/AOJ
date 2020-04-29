from collections import deque
import sys

c=sys.stdin

def main():
    q = deque()
    N=int(input())

    for i in range(N):
        order=c.readline()
        if order[6]==" ":
            if order[0]=="i":
                q.appendleft(int(order[7:]))
            else:
                try :
                    q.remove(int(order[7:]))
                except:
                    pass
        else:
            if order[6]=="F":
                q.popleft()
            else:
                q.pop()
    print(*list(q))

if __name__ == "__main__":
    main()
    