<div align="center">
  <h1>Nipy(니파이)</h1>
</div>

![image](https://user-images.githubusercontent.com/103942316/184535395-075a1a43-6f91-4ec0-a2d1-35c758e92a11.png)

<div align="center">
  <h2>누구나 쉽게 네이버 API를</h2>
</div>

누구나 쉽게 네이버API를 손쉽게 사용이 가능합니다!
> 현재 지원API : 검색API

## Installation
```
$ pip install nipy
```
## Example
### 검색(이미지)
```py
from nipy import client

nipy = client.Search()
# 필수 인자(API)가 들어가는 곳입니다. (샘플키지원)

print(nipy.image("너구리").link)
# 너구리라는 검색어 데이터의 link를 반환합니다.
```
