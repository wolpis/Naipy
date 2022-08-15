<div align="center">
  <h1>Naipy(네이피)</h1>
</div>

![image](https://user-images.githubusercontent.com/103942316/184539416-9568fad2-24ed-4832-8f01-e2775a89fafe.png)

<div align="center">
  <h2>누구나 쉽게 네이버 API를</h2>
</div>

누구나 손쉽게 네이버API를 사용할 수 있어요!
> **동기 비동기 모두 지원합니다!**
> 현재 지원API : 검색API, 번역API, 언어감지API

## Installation
```
$ pip install naipy
```
## Example
### 검색(이미지)[동기]
```py
from naipy import client

nipy = client.Search()
# 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)

print(nipy.image("너구리").link)
# 너구리라는 검색어 데이터의 link를 반환합니다.
```
### 검색(이미지)[비동기]
```py
from naipy import async_client
import asyncio

async def main():
  # 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)
  naipy = async_client.Search()
  result = await naipy.image("너구리") # 너구리라는 검색어 데이터를 반환합니다.
  link = result.link 
  print(link)
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()  
```
