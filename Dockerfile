FROM python:3.9-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONPATH=/app/src

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY ./app /app

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
