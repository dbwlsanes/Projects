def fibo(n, m):
    global a
    global b
    global fib
    c = n+m
    a = b
    b = c
    
a = 0
b = 1
fib = [a]

n = int(input("정수를 입력하세요: "))

while b<=n:
    fibo(a,b)
    fib.append(a)

print(fib)
