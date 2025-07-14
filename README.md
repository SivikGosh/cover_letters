# Cover Letters Bot

Holding and editing cover letters.

### Install and use

Clone repo, install environment:
```bash
$ git clone git@github.com:SivikGosh/cover_letters.git

$ cd cover_letters/
$ python3.13 -m venv venv
$ source venv/bin/activate

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

Show dependency tree (only available with [dev] build):
```bash
$ pipdeptree
```

---

<img src='https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white'><img src='https://img.shields.io/badge/3.13-1a202c?style=flat-square'>
<img src='https://img.shields.io/badge/Aiogram_Dialog-009cfb?style=flat-square'><img src='https://img.shields.io/badge/2.4-1a202c?style=flat-square'>
