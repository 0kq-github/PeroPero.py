from ..utils import PeroPeroUtils
from pydantic import BaseModel,RootModel,Field
from typing import List

class Song(BaseModel):
  disabled: bool
  _id: str
  zh: str
  zht: str
  en: str
  jp: str
  kor: str
  level: int
  value: str

  async def getPCTop(self,difficulty:int):
    return await PeroPeroUtils().getPCTop(self.value,difficulty)
  
  async def getPhoneTop(self,difficulty:int):
    return await PeroPeroUtils().getPhoneTop(self.value,difficulty)


class Album(BaseModel):
  _id: str
  zh: str
  zht: str
  en: str
  jp: str
  kor: str
  value: str
  children: List[Song]
  created: str
  updatedAt: str
  v: int = Field(..., alias="__v")


class AlbumList(RootModel):
  root: List[Album]

  def __iter__(self):
    return iter(self.root)
  
  def __getitem__(self,item):
    return self.root[item]