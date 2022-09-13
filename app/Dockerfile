FROM python:3.10-bullseye
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install flask psycopg2-binary gunicorn
EXPOSE 5000
COPY ./app.py ./
CMD ["flask", "run"]