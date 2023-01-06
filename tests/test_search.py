import pytest

from naipy.client import Search

# 검색어
text = "너구리"

# 이미지 검색
@pytest.mark.asyncio
async def test_image(search: Search):
    r = await search.image(text)
    assert r.data


# 블로그 검색
@pytest.mark.asyncio
async def test_blog(search: Search):
    r = await search.blog(text)
    assert r.data


# 도서 검색
@pytest.mark.asyncio
async def test_book(search: Search):
    r = await search.book(text)
    assert r.data


# 백과사전 검색
@pytest.mark.asyncio
async def test_encyc(search: Search):
    r = await search.encyc(text)
    assert r.data


# 카페글 검색
@pytest.mark.asyncio
async def test_cafearticle(search: Search):
    r = await search.cafearticle(text)
    assert r.data


# 지식인 검색
@pytest.mark.asyncio
async def test_kin(search: Search):
    r = await search.kin(text)
    assert r.data


# 웹사이트 검색
@pytest.mark.asyncio
async def test_webkr(search: Search):
    r = await search.webkr(text)
    assert r.data


# 삼품 검색
@pytest.mark.asyncio
async def test_shop(search: Search):
    r = await search.shop(text)
    assert r.data


# 전문자료 검색
@pytest.mark.asyncio
async def test_doc(search: Search):
    r = await search.doc(text)
    assert r.data
