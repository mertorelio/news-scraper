from analytics import create_wordcloud, get_top_words, most_common_word_plot
from functions import chunkify, pull_news_link, news_content_scrapper, write_text_file
import time
import concurrent.futures
import logging
from bson import ObjectId
from mongo_func import push_news_data, push_word_frequency_data

#Logging Configuration
logging.basicConfig(filename='logs/log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Pull news link for scrapping with timer
start_time_pull = time.time()
news_links = pull_news_link(50)
end_time_pull = time.time()
elapsed_time_pull = end_time_pull - start_time_pull
print(f"Link pull time : {elapsed_time_pull}")

#Divide links into  partss
result = chunkify(news_links, 25)

a = time.time()
thread_no = 1
for i in result: #list of link list
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(news_links)) as executor:
        thread_time_start = time.time()
        try:
            for link in i:

                #thread exacutor
                futures = [executor.submit(news_content_scrapper, link) ]

                for future in concurrent.futures.as_completed(futures):
                    
                    #each news content future    
                    header, summary, text, img_url_list, publish_date, update_date = future.result()
                    news_data = {
                            "_id": ObjectId(),
                            "url": f"{link}",
                            "header": f"{header}",
                            "summary": f"{summary}",
                            "text": f"{text}",
                            "img_url_list": img_url_list,
                            "publish_date": f"{publish_date}",
                            "update_date": f"{update_date}",
                            } 
                    
                    push_news_data(news_data)
                    write_text_file(text,file_name="news_text.txt")

                thread_time_end = time.time()
                thread_time = thread_time_end - thread_time_start
                logging.info(f" Thread {thread_no}is completed in {thread_time} second.")
                thread_no+=1
            
        except Exception as e:
            logging.error(f"An error occured: {e}")  
        
    logging.info("5 SECOND COOLDOWN")
    time.sleep(5)

b = time.time()
c = b - a
print(f"Content pull time : {c}")

#most common word plot
most_common_word_plot(file_name= "news_text.txt", graph_name="most_common.png")
create_wordcloud("news_text.txt", cloud_image_name="cloud.png")

#most commond 20 word,push to mongodb
word_frequency_data = get_top_words("news_text.txt", top_n=20)
push_word_frequency_data(word_frequency_data)
