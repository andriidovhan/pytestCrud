FROM python:3.6

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "pytest", "tests/user_tests.py", "-v" ]
