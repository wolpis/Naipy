import urllib.request
import warnings
from typing import List
import json
from naipy.error import ConverError

class NaipyRequest:
  base_url = "https://openapi.naver.com/v1/"
  
  def __init__(
    self, 
    client_id : str = None, 
    client_secret : str = None
  ) -> None:
    if not client_id or not client_id:
      self.client_id = "p7aYK48ehm6TqdhTt_yv"
      self.client_secret = "UJAqwrxSfQ"
      warnings.warn("샘플키로 요청합니다.", UserWarning)
    else:
      self.client_id = client_id
      self.client_secret = client_secret

      
  def request(
    self,
    tag : List[str],
    text : str
  ):
    encText = urllib.parse.quote(text)
    URL = self.base_url + tag[0] + "/" + tag[1] + "?query=" + encText
    request = urllib.request.Request(URL)
    request.add_header("X-Naver-Client-Id", self.client_id)
    request.add_header("X-Naver-Client-Secret", self.client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
      response_body = response.read()
      result = json.loads(response_body)
      return result

    else:
      raise ConverError(f"Error Code : {rescode}")  

  def get_result(self, tag: List[str], text):
    return self.request(tag, text)
