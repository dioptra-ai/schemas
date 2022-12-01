FROM bitnami/python:3.10.8-debian-11-r11

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["alembic", "upgrade", "head"]