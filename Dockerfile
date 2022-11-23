FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /

RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

ADD entrypoint.sh /
RUN chmod a+x /entrypoint.sh
ADD src /src
ADD action.yaml /

ENTRYPOINT ["/entrypoint.sh"]

