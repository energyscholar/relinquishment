#!/bin/bash
# FAIL if any path named in the manifests/status files is not in git ls-files,
# or if any entry names the epub scratch dir.
cd "$(git rev-parse --show-toplevel)" || exit 1
git ls-files > /tmp/.tracked.$$
python3 -I - /tmp/.tracked.$$ <<'P'
import json,re,sys
tracked=set(open(sys.argv[1]).read().split('\n'))
bad=[]
for p in json.load(open('build/manifest.json'))['files']:
    if p not in tracked or p.startswith("build/epub"+"-tmp/"): bad.append(('build/manifest.json',p))
pat=re.compile(r'((?:manuscript/staging|staging|build/epub[-]tmp)/[\w./+-]+)')
for f in ['build/MANIFEST-STATUS.md','build/puzzle-status.txt','build/review-artifacts.yaml','build/puzzle-tracker.yaml']:
    for m in pat.findall(open(f).read()):
        m=m.rstrip('.')
        if m not in tracked: bad.append((f,m))
for f,p in bad: print(f"UNTRACKED {f}: {p}")
print("FAIL" if bad else "PASS", len(bad))
sys.exit(1 if bad else 0)
P
rc=$?; rm -f /tmp/.tracked.$$; exit $rc
