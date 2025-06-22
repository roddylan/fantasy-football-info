FROM python:3.11-slim

WORKDIR /ff-info-service

COPY ./requirements/base.txt /ff-info-service/requirements/base.txt

RUN pip install --no-cache-dir --upgrade -r /ff-info-service/requirements/base.txt

COPY ./app /ff-info-service/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]