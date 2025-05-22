from pydantic import BaseModel
from typing import List

class Lession(BaseModel):
  lession_id: int
  topic: str

class Module(BaseModel):
  module_id: int
  name: str
  lessions: List[Lession]

class Course(BaseModel):
  course_id: int
  course_name: str
  module = List[Module]