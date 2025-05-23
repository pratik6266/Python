from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
  price: float
  in_stock: bool = True

payload = {
  'id': 101,
  'name': 'Pratik Raj',
  'price': 200.10,
  'in_stock': False
}

data = User(**payload)
print(data)