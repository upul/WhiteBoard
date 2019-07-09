FROM ubuntu:18.04


# Install pipenv
RUN apt-get update && apt-get install python3-pip -y && pip3 install pipenv


COPY . /app
WORKDIR /app


ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN pipenv install --system --deploy --ignore-pipfile


ENV PYTHONPATH /app
EXPOSE 8080
CMD python3 -m digit_recognizer.api.app