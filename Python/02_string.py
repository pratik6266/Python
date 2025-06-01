chai = "Lemon Chai  "
print(chai)

first_char = chai[0]
print(first_char)

slice_chai = chai[:6]
print(slice_chai)

# [:2] will start from 0
# [2:] will go to the very end
# [1: 8: 2] will go from 1 to 7 as last value is never included in python and with a skip value of 2 where default skip value is 1

# print(chai.lower())
# print(chai.upper())
# print(chai.strip())
# print(chai.replace("Lemon", "Masala"))
# chai = "Masala, Lemon, Ginger"
# print(chai.split(', '))


quantity = 8
chai_type = "Masala"
print(f"I ordered {quantity} cups of {chai_type} chai")