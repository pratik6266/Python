from pydantic import BaseModel, EmailStr 
from fastapi import FastAPI, Depends

app = FastAPI()

class UserSignup(BaseModel):
  username: str
  email: EmailStr
  password: str

class settings(BaseModel):
  app_name: str = 'Chai App'
  admin_ele: str = 'admin@chai.com'

def get_settings():
  return settings()


@app.post('/signup')
def signup(user: UserSignup):
  return {'message': f'User ${user.username} signup successfully'}

@app.get('/settings')
def get_settings_endpoint(setting: settings = Depends(get_settings)):
  return setting