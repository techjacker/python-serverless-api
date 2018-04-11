FROM python:3.6

RUN apt-get update && \
	apt-get -y install dbus python-dbus-dev python3-dbus zip

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
