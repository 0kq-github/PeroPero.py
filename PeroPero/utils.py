import httpx
from .models.user import UserList

class PeroPeroUtils:
  def __init__(self,url="https://service.peropero.net:4396") -> None:
    self.url = url
  
  async def getPCTop(self,uid:str,difficulty:int):
    async with httpx.AsyncClient() as client:
      response = await client.post(self.url + "/api/form/getPCTop",json={"uid":uid,"difficulty":difficulty})
      return UserList(response.json())
  
  async def getPhoneTop(self,uid:str,difficulty:int):
    async with httpx.AsyncClient() as client:
      response = await client.post(self.url + "/api/form/getPhoneTop",json={"uid":uid,"difficulty":difficulty})
      return UserList(response.json())
  
