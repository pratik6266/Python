dict = {
  1: 11,
  2: 22,
  3: 33,
}

dict.update({1: 1001})
print(dict.get(1))

print(dict)

for val in dict:
  print(val, " : ", dict.get(val))