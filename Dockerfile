FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY ./bot ./bot
COPY ./pyproject.toml ./

RUN pip install .

CMD [ "python", "-m", "bot.main" ]
