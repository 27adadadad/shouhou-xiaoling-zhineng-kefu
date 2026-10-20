import sys,asyncio,importlib.util,httpx
from app.config import settings
settings.rerank_base_url="https://dashscope.aliyuncs.com/api/v1/services/rerank/text-rerank/text-rerank"
spec=importlib.util.spec_from_file_location("candidate",sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
async def fake(url,json,headers,timeout):
 print("URL",url);print("NATIVE_INPUT","input" in json)
 return httpx.Response(200,json={"output":{"results":[{"index":0,"relevance_score":0.9}]}},request=httpx.Request("POST",url))
m._post=fake
try: print("RANKED",asyncio.run(m.rerank("退货",["退货政策"],1)))
except Exception as e: print("ERROR",type(e).__name__);raise SystemExit(1)
