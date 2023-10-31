n = int(input())
List = []
while len(List) != n:
    List = list(input().split())
List.sort()
print(*List,sep=' ')