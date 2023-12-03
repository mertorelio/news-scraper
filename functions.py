import requests
from bs4 import BeautifulSoup
import logging

# Loglama konfigürasyonu
logging.basicConfig(filename='logs/log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#------------------------------------------------------------------------------------
def pull_news_link(page_size):
    """
    Allows pulling news links.
    input: page_size ---> 1 page have 10 news
    return: links ---> news_link
    """
    news_links = []
    page = 1

    while page < page_size+1:
        try:
            logging.info(f" Links on page {page} have been scraped")
            response = requests.get(f"https://turkishnetworktimes.com/kategori/gundem/page/{page}/")
            html_content = response.text
        
            soup = BeautifulSoup(html_content, 'html.parser')
            articles = soup.find_all('article', class_='col-12')

            for article in articles:

                link = article.find('a', class_='post-link')['href']
                news_links.append(link)
        except Exception as e:
            logging.error(f"An error occured: {e}")   
        page +=1
        
    return news_links

#----------------------------------------------------------------------------------------------

def news_content_scrapper(url):
    """
    scrapping news content with url

    input: news url
    return: header, summary, text, img_url_list, publish_date, update_date
    
    """
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        #header
        title_element = soup.find('h1', class_='single_title')
        header = title_element.text

        #summary
        excerpt_element = soup.find('h2', class_='single_excerpt')
        summary = excerpt_element.text.strip()
    
        #text 
        text = soup.find('div', class_='yazi_icerik').get_text(strip=True, separator='\n')

        #img
        img_url_list = [img['data-origin-url'] for img in soup.select('.rhd-article-news-img-link')]
    
        #date
        dates = []
        for span in soup.select('.yazibio .tarih'):
        
            date = span.find('time')['datetime']
            dates.append(date)
    
        publish_date = dates[0]
        update_date = dates[1]
        logging.info(f" Data on {url} was scraped")

    except Exception as e:
        logging.error(f"An error occured: {e}")

    return header, summary, text, img_url_list, publish_date, update_date

#-----------------------------------------------------------------------------------------------

def write_text_file(text,file_name):
    """
    write text to .txt file for analysis

    input: text ---> news content text
           file_name --->  file name to save
    
    """
    text = f"\n{text}"

    with open(file_name, 'a') as dosya:
        
        dosya.write(text)

#------------------------------------------------------------------
def chunkify(lst, chunk_size):
    """
    Divide the given list into equal-sized chunks.
    
    Args:
    - lst: The list to be divided
    - chunk_size: The size of each chunk
    
    Returns:
    - A list of divided sublists
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


