FROM ubuntu:latest
ADD scraper.py
RUN pip install requests
RUN pip install bs4
RUN pip install time
RUN pip install pandas
RUN pip install redis
CMD["scraper.py"]