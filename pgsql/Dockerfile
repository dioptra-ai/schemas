FROM bitnami/python

MAINTAINER "Jacques Arnoux <jacques@dioptra.ai>"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY alembic.ini .
COPY alembic ./alembic
COPY models ./models

ENTRYPOINT ["alembic", "upgrade", "head"]