# git forest
utilty to easly manage git subtrees

.gitforest file example:
```
tkCommon:
    prefix: "tkCommmon"
    url: "gitlab@git.hipert.unimore.it:tk/core/tkCommon.git"
```

## usage
once you have your `.gitforest` file compiled you can easly pull and push subtrees:
```
git forest pull tkCommon master
git forest push tkCommon master
```
you can also pull and push to all the repos using `all` instead of repo name:
```
git forest pull all master
git forest push all master
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
