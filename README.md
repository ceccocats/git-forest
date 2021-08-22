# git forest
utilty to easly manage git subtrees

.gitforest file example:
```
tkCommon:
    prefix: "tkCommmon"
    url: "gitlab@git.hipert.unimore.it:tk/core/tkCommon.git"
```

## build
```
python3 setup.py bdist_wheel
python3 -m twine upload dist/*
```

## TODO
- [ ] restart from last pull after merging while doing `git forest pull all`
- [ ] add possibility to pass additional parameters
- [ ] add `subtree add` feature
- [ ] add `subtree split` feature
