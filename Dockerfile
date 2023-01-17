FROM python:3.11
COPY . /bookstore
WORKDIR /bookstore
RUN pip install -r /bookstore/requirements.txt
#RUN python etl/pipeline.py
#CMD ["python build/etl/pipeline.py","python","-m","uvicorn", "main:app", "--reload"]
# "--host", "0.0.0.0", "--port", "8000"
