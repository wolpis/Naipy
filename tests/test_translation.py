from naipy.client import Translation
import pytest
from typing import List

text = "안녕하세요"


# 언어인식
@pytest.mark.asyncio
async def test_detect(trans: Translation):
    r = await trans.detect(text)
    assert r.data


# 번역
@pytest.mark.asyncio
async def test_translation(trans: Translation):
    r = await trans.translation(text, target="en")
    assert r.data


# 동시번역
@pytest.mark.asyncio
async def test_dual_translation(trans: Translation):
    r = await trans.dual_translation(text, targets=["en", "ja"])
    assert r
