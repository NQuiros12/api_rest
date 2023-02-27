FROM python:3.11
WORKDIR /bookstore
COPY ./requirements.txt /bookstore
RUN pip install --no-cache-dir -r /bookstore/requirements.txt
COPY . /bookstore
#CMD ["python build/etl/pipeline.py","python","-m","uvicorn", "main:app", "--reload"] 
#"--host", "0.0.0.0", "--port", "8000"
