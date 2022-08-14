from nipy.http import NipyRequest
import sys
from nipy.model import ImageNipy, BlogNipy, BookNipy, EncycNipy, CafearticleNipy, KinNipy, WebkrNipy, ShopNipy, DocNipy

class Search(NipyRequest):
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

  def image(self, text : str) -> ImageNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return ImageNipy(data = data, **data)

  def blog(self, text : str) -> BlogNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return BlogNipy(data = data, **data)

  def book(self, text : str) -> BookNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return BookNipy(data = data, **data)

  def encyc(self, text : str) -> EncycNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return EncycNipy(data = data, **data)

  def cafearticle(self, text : str) -> CafearticleNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return CafearticleNipy(data = data, **data)

  def kin(self, text : str) -> KinNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return KinNipy(data = data, **data)

  def webkr(self, text : str) -> WebkrNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return WebkrNipy(data = data, **data)

  def shop(self, text : str) -> ShopNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return ShopNipy(data = data, **data)

  def doc(self, text : str) -> DocNipy:
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return DocNipy(data = data, **data)
