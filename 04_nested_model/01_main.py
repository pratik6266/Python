from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
  street: str
  city: str
  postal_code: str

class User(BaseModel):
  id: int
  name: str
  address: Address

class Comment(BaseModel):
  id: int
  content: str
  replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
  street = 'Alamganj Road',
  city = 'Sasaram',
  postal_code = '821115'
)

user = User(
  id = 1,
  name = 'Pratik Raj',
  address = address
)

comment = Comment(
  id = 1,
  content = 'Good',
  replies = [
    Comment(id = 2, content = 'Good Again'),
    Comment(id=3, content='Good Third Time')
  ]
)