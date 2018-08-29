# Class Central Web Scraper

## Description
A web scraping application extracting 900+ subjects from Class Central related to Computer Science courses in New York City, US. 

Link: http://class-central.com/subjects

This app enables the extraction of each course URL related within the subject required, as well as the course name and subject name into a csv file (items.json).


## Installation
```
pip install scrapy

scrapy crawl subjects -a subject='Computer Science' -o items.json
```