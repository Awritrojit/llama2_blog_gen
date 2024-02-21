FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/model

EXPOSE 8501

CMD ["streamlit", "run", "local_app.py"]