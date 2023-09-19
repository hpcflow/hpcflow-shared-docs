import json
from pathlib import Path
import re

def pad_version(version,pad_length=3):
    p=""
    for n in re.findall(r'\d+', version):
        p=p+str(n.zfill(pad_length))
    if 'a' not in version:
        p=p+'999'   # stable versions before pre-releases (with `reverse=True`)
    return p

docs_dir = Path(__file__).parent.resolve()
all_vers = sorted(
    (i.name for i in docs_dir.glob('*') if i.is_dir() and not i.is_symlink()),
    key=lambda i: pad_version(i),
    reverse=True,
)

vers_switcher = []
dev_named = False
stable_named = False
for idx, vers in enumerate(all_vers):
    is_dev = bool(re.search(r"(v[0-9]+\.[0-9]+\.[0-9]+((?:a|b|rc).*)?)", vers).groups()[1])
    if not is_dev and not stable_named:
        stable_named = True
        name = f"stable ({vers})"
        if idx == 0:
            dev_named = True # don't label dev if there is no dev version beyond stable
    elif is_dev and not dev_named:
        dev_named = True
        name = f"dev ({vers})"
    else:
        name = vers
    vers_switcher.append({"name": name, "version": vers.lstrip('v'), "url": "/docs/"+vers+"/"})

with docs_dir.joinpath('switcher.json').open('w') as fh:
    json.dump(vers_switcher, fh, indent=4)
    fh.write("\n")
