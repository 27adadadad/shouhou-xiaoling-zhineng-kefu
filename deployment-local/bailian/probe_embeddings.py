import sys,asyncio,importlib.util
from types import SimpleNamespace as S
spec=importlib.util.spec_from_file_location("candidate",sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Fake:
 async def create(self,model,input):
  print("BATCH",len(input))
  if len(input)>10: raise ValueError("batch limit 10")
  return S(data=[S(embedding=[1.0]) for x in input])
m._CLIENT=S(embeddings=Fake())
try: print("VECTORS",len(asyncio.run(m.embed_texts(["test"]*21))))
except Exception as e:print("ERROR",type(e).__name__);raise SystemExit(1)
