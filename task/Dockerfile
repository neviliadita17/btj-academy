# FROM ubuntu:latest

# WORKDIR /app
# COPY app.py .

# # Install Python dan pustaka yang diperlukan
# RUN pip install --no-cache-dir -r requirements.txt \
#     pip install Flask \
#     apt-get update && \
#     apt-get install -y python3 && \
#     apt-get clean

# CMD ["python3", "app.py"]


FROM python:3.11-alpine

WORKDIR /app
# COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .
ENV PORT 5000 
EXPOSE $PORT
CMD ["python", "app.py"]

