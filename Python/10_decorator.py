import time

def timer(func):
  def wrapper(*args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(end - start)  
    return result
  return wrapper


@timer
def example(n):
  time.sleep(n)

example(2)