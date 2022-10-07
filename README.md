<div align="center">
  <h1>Naipy(네이피)[Beta]</h1>
</div>

![image](https://user-images.githubusercontent.com/103942316/184539416-9568fad2-24ed-4832-8f01-e2775a89fafe.png)

<div align="center">
  <h2>누구나 쉽게 네이버 API를</h2>
</div>

[<img src="https://img.shields.io/pypi/v/naipy.svg">](https://pypi.python.org/pypi/naipy)<br>
누구나 손쉽게 네이버API를 사용할 수 있어요!<br>
> **동기 비동기 모두 지원합니다!**<br>
> 현재 지원API : 검색API, 번역API, 언어감지API<br>
> [자세한 사용법은 여기를 참조해주세요!](https://naipy.notion.site/Naipy-3c332c562b5f42059c48b783b5b59528)<br>

## Installation
```
$ pip install naipy
```
## Example
### 검색(이미지)[동기]
```py
from naipy import sync

nipy = sync.Search()
# 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)

print(nipy.image("너구리").link)
# 너구리라는 검색어 데이터의 link를 반환합니다.
```
### 검색(이미지)[비동기]
```py
from naipy import client
import asyncio

async def main():
  c = client.Search()
  # 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)
  r = await c.image("너구리")
  # 너구리라는 검색어 데이터의 link를 반환합니다.
  print(r.link)

asyncio.run(main())
```
