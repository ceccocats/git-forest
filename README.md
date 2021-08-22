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