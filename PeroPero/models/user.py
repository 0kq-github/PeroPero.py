from pydantic import BaseModel,RootModel
from typing import List


def parseLabel(label:str):
  label_split = label.split(", ")
  ranking = int(label_split[0])
  name = label_split[1]
  accuracy = float(label_split[2].split(" ")[1])
  score = int(label_split[3].split(" ")[1])
  return ranking,name,accuracy,score

class User(BaseModel):
  label: str
  value: str
  name: str
  top: int
  user_id: str

  def __init__(self,label:str,value:str,name:str,top:int,user_id:str) -> None:
    _, _, accuracy, score = parseLabel(label)
    super().__init__(label=label,value=value,name=name,top=top,user_id=user_id,accuracy=float(accuracy),score=float(score))
    self._accuracy = accuracy
    self._score = score
  
  @property
  def accuracy(self):
    return self._accuracy
  
  @property
  def score(self):
    return self._score

  #accuracy: float = float(parseLabel(label)[2])
  #score: int = float(parseLabel(label)[2])




class UserList(RootModel):
  root: List[User]

  def __iter__(self):
    return iter(self.root)
  
  def __getitem__(self,item):
    return self.root[item]