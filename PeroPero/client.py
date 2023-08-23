import httpx
from .models.song import AlbumList
from .utils import PeroPeroUtils

class PeroPeroAPI:
  def __init__(self,url="https://service.peropero.net:4396") -> None:
    self.url = url
    self._song_list:AlbumList = None
  
  async def getList(self):
    if self._song_list:
      return self._song_list
    return await self.fetchList()

  async def fetchList(self):
    async with httpx.AsyncClient() as client:
      response = await client.post(self.url + "/api/album/getList")
      self._song_list = AlbumList(response.json())
      return self._song_list
  
  async def getPCTop(self,uid:str,difficulty:int):
    return await PeroPeroUtils().getPCTop(uid,difficulty)

  async def getPhoneTop(self,uid:str,difficulty:int):
    return await PeroPeroUtils().getPhoneTop(uid,difficulty)