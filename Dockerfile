FROM python:3.7-slim

WORKDIR cassavea

EXPOSE 5000

RUN apt update && apt install libgl1-mesa-glx -y

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

RUN pip install flask keras keras-models opencv-python tensorflow

ENV FLASK_APP "cassavea.py"

CMD ["flask", "run", "--host=0.0.0.0"]