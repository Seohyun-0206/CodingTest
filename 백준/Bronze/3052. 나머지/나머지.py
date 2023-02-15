n = []
for i in range(10):
    n.append(int(input()) % 42)

num = set(n)
print(len(num))