from typing import List

import pytest

from naipy.sync import Translation

text = "안녕하세요"


# 언어인식
def test_detect(sync_trans: Translation):
    r = sync_trans.detect(text)
    assert r.data


# 번역
def test_sync_translation(sync_trans: Translation):
    r = sync_trans.translation(text, target="en")
    assert r.data
