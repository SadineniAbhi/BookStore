FROM python:3.8
RUN git clone https://github.com/SadineniAbhi/BookStore.git
WORKDIR /BookStore
RUN pip install -r requirement.txt

WORKDIR /BookStore/BookStore

CMD [ "python","app.py" ]
