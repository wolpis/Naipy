<div align="center">
  <h1>Naipy(네이피)</h1>
</div>

![image](https://user-images.githubusercontent.com/103942316/184539416-9568fad2-24ed-4832-8f01-e2775a89fafe.png)

<div align="center">
  <h2>누구나 쉽게 네이버 API를</h2>
</div>

누구나 쉽게 네이버API를 손쉽게 사용이 가능합니다!
> 현재 지원API : 검색API

## Installation
```
$ pip install naipy
```
## Example
### 검색(이미지)
```py
from naipy import client

nipy = client.Search()
# 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)

print(nipy.image("너구리").link)
# 너구리라는 검색어 데이터의 link를 반환합니다.
```
