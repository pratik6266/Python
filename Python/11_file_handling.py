file = open('youtube.txt', 'w')

try:
  file.write("Hello There")  
finally:
  file.close()

