import pytest

from naipy.sync import Search

# 검색어
text = "너구리"

# 이미지 검색
def test_image(sync_search: Search):
    r = sync_search.image(text)
    assert r.data


# 블로그 검색
def test_blog(sync_search: Search):
    r = sync_search.blog(text)
    assert r.data


# 도서 검색
def test_book(sync_search: Search):
    r = sync_search.book(text)
    assert r.data


# 백과사전 검색
def test_encyc(sync_search: Search):
    r = sync_search.encyc(text)
    assert r.data


# 카페글 검색
def test_cafearticle(sync_search: Search):
    r = sync_search.cafearticle(text)
    assert r.data


# 지식인 검색
def test_kin(sync_search: Search):
    r = sync_search.kin(text)
    assert r.data


# 웹사이트 검색
def test_webkr(sync_search: Search):
    r = sync_search.webkr(text)
    assert r.data


# 삼품 검색
def test_shop(sync_search: Search):
    r = sync_search.shop(text)
    assert r.data


# 전문자료 검색
def test_doc(sync_search: Search):
    r = sync_search.doc(text)
    assert r.data
