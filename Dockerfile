FROM python:3.12-slim
#FROM tiangolo/meinheld-gunicorn-flask:python3.9

WORKDIR /usr/local/app
COPY ./src .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

#CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:8050", "app:app"]
EXPOSE 8050