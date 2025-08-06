n,h = map(int, input().split())
heights = list(map(int, input().split()))
counter = 0

for i in range(n):
    if heights[i] > h:
        counter += 2
    else:
        counter += 1

print(counter)
