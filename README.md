[<img src='https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white'><img src='https://img.shields.io/badge/3.13-23283d?style=flat-square'>](https://www.python.org/)
[<img src='https://img.shields.io/badge/Aiogram_Dialog-009cfb?style=flat-square'><img src='https://img.shields.io/badge/2.4-23283d?style=flat-square'>](https://pypi.org/project/aiogram-dialog/)
[<img src='https://img.shields.io/badge/Python Dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black'><img src='https://img.shields.io/badge/1.1-23283d?style=flat-square'>](https://pypi.org/project/python-dotenv/)
[<img src='https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white'>](https://docs.python.org/3/library/sqlite3.html)
[<img src='https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white'>](https://www.docker.com/)


# Cover Letters Bot

Holding and editing cover letters in [Telegram](https://telegram.org/). Bot is available by name [@coverletters_bot](https://t.me/coverletters_bot).

<br>

## 🛠 Develop Mode

### Install and use
Clone the repo and enter into the root folder
```bash
git clone git@github.com:SivikGosh/cover_letters.git
cd cover_letters/
```

Create an environment
```bash
python3.13 -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip3 install .[div]
```

Add your bot token
```bash
cp .env.example .env  # then open the .env file and replace value of TOKEN variable
```

Start bot
```bash
python3.13 -m bot.main
```

### Build

Build a Docker image
```bash
docker build --no-cache -t cover_letters .
```

Run a container
```bash
docker run -e TOKEN='your_bot_token' --name cover_letters -d cover_letters
```

### Some tools

Pre-commit
```bash
pre-commit install
```

Dependencies tree
```bash
pipdeptree
```

<br>

## 🚀 Production Mode

### Install and use
```bash
docker run -e TOKEN='your_bot_token' --name cover_letters -d sivikgosh/cover_letters
```

<br>

<div align="right">

## Author's contact
<a href='https://t.me/sivikgosh' target='_blank'><img src='https://img.shields.io/badge/SivikGosh-white?style=flat-square&logo=Telegram&logoColor=26A5E4'></a>

</div>
