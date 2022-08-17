from naipy.http import NaipyRequest
import sys
from naipy.model import ImageNaipy, BlogNaipy, BookNaipy, EncycNaipy, CafearticleNaipy, KinNaipy, WebkrNaipy, ShopNaipy, DocNaipy, DetectNaipy, N2mtNaipy
import random

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
    """
    이미지를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return ImageNaipy(data = data, **data)

  def blog(self, text : str) -> BlogNaipy:
    """
    블로그를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return BlogNaipy(data = data, **data)

  def book(self, text : str) -> BookNaipy:
    """
    도서를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return BookNaipy(data = data, **data)

  def encyc(self, text : str) -> EncycNaipy:
    """
    백과사전를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return EncycNaipy(data = data, **data)

  def cafearticle(self, text : str) -> CafearticleNaipy:
    """
    카페글를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return CafearticleNaipy(data = data, **data)

  def kin(self, text : str) -> KinNaipy:
    """
    네이버 지식인을 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return KinNaipy(data = data, **data)

  def webkr(self, text : str) -> WebkrNaipy:
    """
    웹사이트를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return WebkrNaipy(data = data, **data)

  def shop(self, text : str) -> ShopNaipy:
    """
    쇼핑을 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return ShopNaipy(data = data, **data)

  def doc(self, text : str) -> DocNaipy:
    """
    전문자료를 검색합니다.
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['search', str(current_func_name)]
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    data["item"] = random.choice(data['items'])
    return DocNaipy(data = data, **data)

class Translation(NaipyRequest):
  """
  네이버 번역 라이브러리입니다.<br>(Parameters가 빈칸일시 샘플키로 요청합니다.)
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
    """
    언어를 인식합니다. [언어코드표](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md#%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0)
    """
    current_func_name = sys._getframe().f_code.co_name
    tag = ['papago', str(current_func_name) + 'Langs', 'query=']
    data = self.get_result(tag, text)
    data["type"] = str(current_func_name)
    return DetectNaipy(data = data, **data)

  def translation(self, text : str, target : str) -> N2mtNaipy:
    """
    문장또는 단어를 번역합니다. `target`파라미터는 [언어코드표](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md#%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0)를 참고해주세요!
    """
    source = self.detect(text).langCode
    tag = ['papago', 'n2mt', f'source={source}&target={target}&text=']
    data = self.get_result(tag, text)
    data = data['message']['result']
    return N2mtNaipy(data , **data)
