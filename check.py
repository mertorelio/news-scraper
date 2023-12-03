from pymongo import MongoClient
from pprint import pprint

from analytics import create_wordcloud, get_top_words, most_common_word_plot
from mongo_func import push_word_frequency_data
"""
client = MongoClient("mongodb://localhost:27017/")
db = client["mert_bozkurt"]
collection = db["news"]


cursor = collection.find()

for document in cursor:
    print("######################################################################")
    pprint(document)
    print("######################################################################")
"""

#most_common_word_plot(file_name= "news_text.txt", graph_name="most_common.png")
#create_wordcloud("news_text.txt", cloud_image_name="cloud.png")


word_frequency_data = get_top_words("news_text.txt", top_n=20)
push_word_frequency_data(word_frequency_data)
client = MongoClient("mongodb://localhost:27017/")
db = client["mert_bozkurt"]
collection = db["word_frequency"]


cursor = collection.find()

for document in cursor:
    print("######################################################################")
    pprint(document)
    print("######################################################################")