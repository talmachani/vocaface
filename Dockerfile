# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/vocaface
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

#entry
CMD ["python", "run.py"]