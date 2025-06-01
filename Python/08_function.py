def square(n):
  return pow(n, 2)

print(square(4))

def fac(n):
  if n == 0 or n == 1:  
    return 1
  return n * fac(n-1)

def sum_all(*args):    # * make the function to expect multiple value as paramter
  return sum(args)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3))

print(fac(5))