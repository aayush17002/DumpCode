def sum_digits(n):
   r = 0
   while (n>0):
       r += n % 10
       n//=10
   return r
T = int(input())
for _ in range(T):
	n = int(input())
	print(sum_digits(n))