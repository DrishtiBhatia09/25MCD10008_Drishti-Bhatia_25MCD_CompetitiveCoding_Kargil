t = int(input())
for _ in range(t):
    n = int(input())

    if n < 5:
        print(-1)
        continue

    for i in range(1, n + 1, 2):
        if i != 5:
            print(i, end=" ")

    print(5, 4, end=" ")

    for i in range(2, n + 1, 2):
        if i != 4:
            print(i, end=" ")
            
    print()   
