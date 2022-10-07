from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
import sys


@dataclass(frozen=True)
class BaseNaipy:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""


@dataclass(frozen=True)
class DetectNaipy(BaseNaipy):
    langCode: Optional[str] = field(repr=True, compare=True, default=None)
    """언어코드"""


@dataclass(frozen=True)
class N2mtNaipy(BaseNaipy):
    srcLangType: Optional[str] = field(repr=True, compare=True, default=None)
    """시작언어"""
    tarLangType: Optional[str] = field(repr=True, compare=True, default=None)
    """도착언어"""
    translatedText: Optional[str] = field(repr=True, compare=True, default=None)
    """번역된 글자"""
    engineType: Optional[str] = field(repr=True, compare=True, default=None)
    """엔진 유형"""
    pivot: Optional[str] = field(repr=True, compare=True, default=None)
    """"""
    dict: Optional[str] = field(repr=True, compare=True, default=None)
    """"""
    tarDict: Optional[str] = field(repr=True, compare=True, default=None)
    """"""

    @property
    def json(self):
        """return JSON"""
        result = {
            "srcLangType": self.srcLangType,
            "tarLangType": self.tarLangType,
            "text": self.translatedText,
        }
        return result


@dataclass(frozen=True)
class SearchNaipy(BaseNaipy):
    lastBuildDate: Optional[str] = field(repr=True, compare=True, default=None)
    """검색 결과를 생성한 시간"""
    total: Optional[int] = field(repr=True, compare=True, default=None)
    """검색 결과 문서의 총 개수"""
    start: Optional[int] = field(repr=True, compare=True, default=None)
    """검색 결과 문서 중, 문서의 시작점"""
    display: Optional[int] = field(repr=True, compare=True, default=None)
    """검색된 검색 결과의 개수"""
    items: List[str] = field(repr=True, compare=True, default=None)
    """데이터 List"""
    item: List[str] = field(repr=True, compare=True, default=None)
    """추출할 리스트"""


@dataclass(frozen=True)
class ImageNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 이미지의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 이미지의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def thumbnail(self) -> str:
        """검색 결과 이미지의 썸네일 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def sizeheight(self) -> str:
        """검색 결과 이미지의 썸네일 높이"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def sizewidth(self) -> str:
        """검색 결과 이미지의 너비"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class BlogNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def bloggername(self) -> str:
        """검색 결과 블로그 포스트를 작성한 블로거의 이름"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def bloggerlink(self) -> str:
        """검색 결과 블로그 포스트를 작성한 블로거의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def postdate(self) -> str:
        """포스트 날짜"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class BookNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def image(self) -> str:
        """썸네일 이미지의 URL"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def author(self) -> str:
        """저자 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def discount(self) -> str:
        """할인 가격 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def publisher(self) -> str:
        """출판사 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def pubdate(self) -> str:
        """출간일 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def isbn(self) -> str:
        """국제표준도서번호"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class EncycNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 사전 정의의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 사전 정의의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def thumbnail(self) -> str:
        """해당 이미지의 썸네일 link url"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class CafearticleNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def cafename(self) -> str:
        """검색 결과 문서가 작성된 카페 이름"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def cafeurl(self) -> str:
        """검색 결과 문서가 적성된 카페의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class KinNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class WebkrNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]


@dataclass(frozen=True)
class ShopNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """검색 결과 문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트 link"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def image(self) -> str:
        """썸네일 이미지의 URL"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def lprice(self) -> str:
        """최저가"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def hprice(self) -> str:
        """최고가"""
        if self.item == "":
            return None
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def mallName(self) -> str:
        """쇼핑몰의 상호"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def productId(self) -> int:
        """해당 상품에 대한 ID"""
        return int(self.item[f"{sys._getframe().f_code.co_name}"])

    @property
    def productType(self) -> int:
        """상품군 정보"""
        return int(self.item[f"{sys._getframe().f_code.co_name}"])

    @property
    def brand(self) -> str:
        """해당 상품의 브랜드 명"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def maker(self) -> str:
        """해당 상품의 제조사 명"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def category(self) -> List[str]:
        """해당 상품의 제조사 명"""
        result = []
        for i in range(4):
            result += self.item[f"{sys._getframe().f_code.co_name}{i+1}"]
        return result


@dataclass(frozen=True)
class DocNaipy(SearchNaipy):
    @property
    def title(self) -> str:
        """문서의 제목"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def link(self) -> str:
        """검색 결과 문서의 하이퍼텍스트"""
        return self.item[f"{sys._getframe().f_code.co_name}"]

    @property
    def description(self) -> str:
        """검색 결과 문서의 내용을 요약한 패시지 정보"""
        return self.item[f"{sys._getframe().f_code.co_name}"]
