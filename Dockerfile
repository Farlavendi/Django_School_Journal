FROM python:3.13.1-slim

WORKDIR /src

#RUN apt update
#RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
#COPY poetry.lock ./
#COPY pyproject.toml ./



RUN pip install -r requirements.txt --no-cache-dir
#RUN pip install poetry
#RUN poetry install
EXPOSE 5000

COPY . .

CMD ["python", "src/manage.py", "runserver"]