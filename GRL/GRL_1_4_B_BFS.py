"""
�ȥݥ����륽����

�ޤ����ϼ�����0�ΥΡ��ɤ򥭥塼���ɲ�
���θ奭�塼����
���Ρ��ɤ���Ф���
�����ΥΡ��ɤ����դ���������ΥΡ��ɤ����꼡���򸺤餹��
���⤷���餷��������꼡����0�ˤʤä��饭�塼���ɲ�
�򷫤��֤���
"""
from collections import deque
V,E = map(int,input().split())
C = [[] for _ in range(V)]
indeg = [0]*V
for _ in range(E):
    tmp = list(map(int,input().split()))
    indeg[tmp[1]] += 1
    C[tmp[0]].append(tmp[1])

q = deque()
deleted = [False]*V
ans = []
for i in range(V):
    if indeg[i] == 0:
        ans.append(i)
        q.append(i)

while q:
    node = q.pop()
    deleted[node] = True
    for adj in C[node]:
        indeg[adj] -= 1
        if indeg[adj] == 0:
            q.append(adj)
            ans.append(adj)
for node in ans:
    print(node)