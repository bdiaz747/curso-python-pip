FROM python:3.10

WORKDIR /app
COPY requirementes.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

