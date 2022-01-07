#newsSentimentModel container

FROM python:3.8.12-buster

COPY api /api
COPY newsSentimentModel /newsSentimentModel
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port 8000:8000
