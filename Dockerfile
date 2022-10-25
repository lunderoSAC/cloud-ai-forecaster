FROM python:3.8.15-slim-bullseye
WORKDIR /lundero-forecaster/src
ADD /lundero-forecaster /lundero-forecaster
RUN pip install -r requirements.txt
CMD ["python","main.py"]