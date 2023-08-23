import asyncio
from PeroPero import PeroPeroAPI

async def main():
  peropero = PeroPeroAPI()
  song_list = await peropero.getList()
  album_name = song_list[0].jp
  song_name = song_list[0].children[0].jp
  ranking = await song_list[0].children[0].getPCTop(2)
  print("=== Album ===")
  print(album_name)
  print("=== Song ===")
  print(song_name)
  print("=== Ranking ===")
  for user in ranking:
    print(user.top,user.name,user.accuracy,user.score)

if __name__ == "__main__":
  asyncio.run(main())