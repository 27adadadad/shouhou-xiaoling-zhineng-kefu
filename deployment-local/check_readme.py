from pathlib import Path
import sys,re
p=Path(sys.argv[1]);s=p.read_text(encoding="utf-8")
checks={"bailian_entry":"deployment-local/bailian/run.py" in s,"port_3307":"3307" in s,"provenance":"课程配套源码" in s,"regression_boundary":"回归原因尚未定位" in s,"image":"docs/images/chat-page.png" in s,"balanced_fences":s.count("```")%2==0}
for k,v in checks.items():print(k,v)
raise SystemExit(0 if all(checks.values()) else 1)
