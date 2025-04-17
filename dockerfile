FROM python:3.10-slim
WORKDIR /fastapi
COPY requirements.txt /fastapi
COPY config_nomes_colunas.csv /fastapi
RUN pip install -r requirements.txt
COPY ./app /fastapi/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]