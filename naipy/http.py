import warnings
from typing import Dict, Union
from naipy.error import HTTPException
import aiohttp

class NaipyRequest:
  base_url = "https://openapi.naver.com/v1/"

  def __init__(
    self, 
    client_id : str = None, 
    client_secret : str = None
  ) -> None:
    if not client_id or not client_secret:
      self.client_id = "p7aYK48ehm6TqdhTt_yv"
      self.client_secret = "UJAqwrxSfQ"
      warnings.warn("샘플키로 요청합니다.", UserWarning)
    else:
      self.client_id = client_id
      self.client_secret = client_secret

  async def request(
    self,
    method : str,
    endpoint : str,
    params: Dict[str, Union[str, int]]
  ) -> Dict[str, Union[str, int]]:
    headers = {
      "X-Naver-Client-Id" : self.client_id,
      "X-Naver-Client-Secret" : self.client_secret,
      "Content-Type" : "application/x-www-form-urlencoded"
    }
    url = self.base_url + endpoint
    async with aiohttp.ClientSession(headers = headers) as session:
      async with session.request(method, url=url, headers=headers, params=params) as response:
        rescode = response.status
        if(rescode==200):
          return await response.json()
        else:
          raise HTTPException(f"Error Code : {rescode}")

  async def get_search(self, tag: str, params: Dict[str, Union[str, int]]):
    return await self.request("GET", f"search/{tag}", params)

  async def get_translation(self, tag: str, params: Dict[str, Union[str, int]]):
    return await self.request("POST", f"papago/{tag}", params)
