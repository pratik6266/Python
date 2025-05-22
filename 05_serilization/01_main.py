from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
  street: str
  city: str
  zip_code: str

class User(BaseModel):
  id: int
  name: str
  email: str
  is_active: bool = True
  created_at: datetime
  address: Address
  tags: List[str] = []

  model_config = ConfigDict(
    json_encoders={
      datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
    }
  )

user = User(
  id= 1,
  name= 'Pratik',
  email= 'p@p.com',
  created_at= datetime(2024, 3, 15, 14, 30),
  address= Address(
    street= 'Alamganj road',
    city= 'sasaram',
    zip_code= '821115'
  ),
  is_active= False,
  tags= ['premium', 'subscriber']
)

python_dict = user.model_dump_json() #model.dump
print(python_dict)