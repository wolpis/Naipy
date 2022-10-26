from naipy.client import Translation
import asyncio

t = Translation()

d = asyncio.run(t.dual_translation("안녕하세요", ['en', 'ja']))

print(d)