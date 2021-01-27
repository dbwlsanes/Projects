def avg(n):
    total = 0
    for i in range(len(n)):
        total += float(n[i])
    return total/len(n)

a = input("numbers: ").split()

print(avg(a))
