# Cover Letters Bot

Holding and editing cover letters.

Python 3.13.

### Install and use

Clone repo, install environment:
```bash
$ git clone git@github.com:SivikGosh/cover_letters.git
$ cd cover_letters/
$ python3.13 -m venv venv
$ source venv/binactivate
(venv) $ pip3 install .  # or pip install .[dev] for develop build
(venv) $ cp .env.example .env
```

Add bot token to **TOKEN** variable in **.env** file.

Start bot:
```bash
(venv) $ python3.13 -m bot.main
```

### Some tools

Install pre-commit:
```bash
$ pip install .[dev]
$ pre-commit install
```

Show dependency tree (only awailable with [dev] build):
```bash
$ pipdeptree
```
