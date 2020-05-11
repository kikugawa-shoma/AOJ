A = [1,2,3,4,5]
def change1(a):
    a = 100

def cahnge2(A):
    A[3] = 100

print(A)
change1(A[3])
print(A)
cahnge2(A)
print(A)