FROM python:3.13.2

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app:app"]
