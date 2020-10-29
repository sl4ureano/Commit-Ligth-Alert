# Commit-Ligth-Alert
Alert blink1 when your git repository receive a commit

## Install
Just run
```shell
$ python -m venv virtualenv/
$ source ./virtualenv/bin/activate
$ pip install
```


## How to use
```python
GITHUB_USER = 'YOUR GITHUB USER'
GITHUB_REPOSITORY = 'YOUR GITHUB REPO'
GITHUB_TOKEN = 'YOUR GITHUB TOKEN'
BLIKN_INTERVAL = 5
commit = ClassCommit(GITHUB_USER,
  GITHUB_REPOSITORY,
  GITHUB_TOKEN, 
  BLIKN_INTERVAL)
commit.Main()
```
