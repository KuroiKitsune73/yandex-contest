n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    l, r = map(int, input().split())
    min_val = min(a[l:r+1])
    for j in range(l, r+1):
        if a[j] != min_val:
            print(a[j])
            break
    else:
        print("NOT FOUND")