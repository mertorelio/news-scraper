from pymongo import MongoClient
from datetime import datetime

def push_news_data(news_data):
    """
    news_data = {
    "url": "",
    "header": "",
    "summary": "",
    "text": "",
    "img_url_list": [""],
    "publish_date": "YYYY-mm-dd",
    "update_date": "YYYY-mm-dd",
}   
    """
    client = MongoClient("mongodb://localhost:27017/")
    
    db = client["mert_bozkurt"]
    news_collection = db["news"]

    news_collection.insert_one(news_data)

    client.close()

def push_word_frequency_data( word_frequency_data):
    
    """
    word_frequency_data = {"word": "", "count": 0}
    """
    word_frequency_data = {"word": "", "count": 0}
    client = MongoClient("mongodb://localhost:27017/")
    
    db = client["mert_bozkurt"]
    word_frequency_collection = db["word_frequency"]
    word_frequency_collection.insert_one(word_frequency_data)


    client.close()

def push_stats_data(stats_data):
    """
    stats_data = {
    "elapsed_time": "",
    "count": 0,
    "date": "",
    "success_count": 0,
    "fail_count": 0,
}
    """

    client = MongoClient("mongodb://localhost:27017/")

    db = client["mert_bozkurt"]
    stats_collection = db["stats"]

    stats_collection.insert_one(stats_data)


    client.close()





