FROM python:3.12-sim
WORKDIR /app
COPY app/.
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python:,"app.py"]
