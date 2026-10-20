import sys,os,runpy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
os.chdir(ROOT);sys.path.insert(0,str(ROOT));os.environ['PYTHONUTF8']='1'
from app.config import settings
settings.database_url='mysql+asyncmy://root:root@127.0.0.1:3307/mewhelp'
settings.embed_base_url=settings.chat_base_url
settings.embed_model='text-embedding-v4';settings.embed_api_key=settings.chat_api_key
settings.rerank_base_url='https://dashscope.aliyuncs.com/api/v1/services/rerank/text-rerank/text-rerank'
settings.rerank_model='gte-rerank-v2';settings.rerank_api_key=settings.chat_api_key
for name in ['embeddings','rerank']:
 spec=importlib.util.spec_from_file_location('app.core.'+name,Path(__file__).parent/(name+'.py'))
 module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
if len(sys.argv)>1: runpy.run_module(sys.argv[1],run_name='__main__')
else:
 import uvicorn
 uvicorn.run('app.main:app',host='127.0.0.1',port=8000)
