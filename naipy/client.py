from naipy.http import NaipyRequest
import sys
from naipy.model import ImageNaipy, BlogNaipy, BookNaipy, EncycNaipy, CafearticleNaipy, KinNaipy, WebkrNaipy, ShopNaipy, DocNaipy, DetectNaipy, N2mtNaipy

class Search(NaipyRequest):
  """
  네이버 검색 라이브러리입니다.<br>(Parameters가 빈칸일시 샘플키로 요청합니다.)
  #### client_id
  [네이버개발자센터](https://developers.naver.com/main/)에서 발급받은 `Client ID`를 입력합니다.
  #### client_secret
  [네이버개발자센터](https://developers.naver.com/main/)에서 발급받은 `Client Secret`를 입력합니다.
  """

  def __init__(
    self, 
    client_id : str = None, 
    client_secret : str = None
  ) -> None:
    super().__init__(
      client_id = client_id,
      client_secret = client_secret
    )

  def image(self, text : str) -> ImageNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return ImageNaipy(data = data, **data)

  def blog(self, text : str) -> BlogNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return BlogNaipy(data = data, **data)

  def book(self, text : str) -> BookNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return BookNaipy(data = data, **data)

  def encyc(self, text : str) -> EncycNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return EncycNaipy(data = data, **data)

  def cafearticle(self, text : str) -> CafearticleNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return CafearticleNaipy(data = data, **data)

  def kin(self, text : str) -> KinNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return KinNaipy(data = data, **data)

  def webkr(self, text : str) -> WebkrNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return WebkrNaipy(data = data, **data)

  def shop(self, text : str) -> ShopNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return ShopNaipy(data = data, **data)

  def doc(self, text : str) -> DocNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return DocNaipy(data = data, **data)

class Translation(NaipyRequest):
  """
  네이버 검색 라이브러리입니다.<br>(Parameters가 빈칸일시 샘플키로 요청합니다.)
  #### client_id
  [네이버개발자센터](https://developers.naver.com/main/)에서 발급받은 `Client ID`를 입력합니다.
  #### client_secret
  [네이버개발자센터](https://developers.naver.com/main/)에서 발급받은 `Client Secret`를 입력합니다.
  """
  def __init__(
    self, 
    client_id : str = None, 
    client_secret : str = None
  ) -> None:
    super().__init__(
      client_id = client_id,
      client_secret = client_secret
    )

  def detect(self, text : str) -> DetectNaipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['papago', str(current_func_name) + 'Langs', 'query=']
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return DetectNaipy(data = data, **data)

  def translation(self, text : str, target : str) -> N2mtNaipy:
    source = self.detect(text).langCode
    tag = ['papago', 'n2mt', f'source={source}&target={target}&text=']
    data = self.get_result(tag, text)
    data = data['message']['result']
    return N2mtNaipy(data , **data)
