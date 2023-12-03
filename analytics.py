import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
from collections import Counter
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

stop_words_turkish = set(stopwords.words('turkish'))
def most_common_word_plot(file_name, graph_name):
    # Read the content of the file
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean the content by removing non-alphanumeric characters
    cleaned_content = re.sub(r'\W', ' ', content)

    # Convert the text to lowercase and split it into words
    words = cleaned_content.lower().split()

    # Remove Turkish stopwords and words with less than 3 characters
    words = [word for word in words if word not in stop_words_turkish and len(word) > 2]

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Find the most common 10 words
    most_common_words = word_counts.most_common(10)

    # Create a bar plot for the most common words
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(most_common_words)), [word[1] for word in most_common_words],
            color=plt.cm.Paired(range(len(most_common_words))), width=0.5)

    plt.xticks(range(len(most_common_words)), [word[0] for word in most_common_words], rotation=45)
    plt.xlabel('Words', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Bar Plot of the 10 Most Common Words', fontsize=16)
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig(graph_name, bbox_inches='tight')

    # Show the plot
    plt.show()


def create_wordcloud(file_name, cloud_image_name):
    # Read the content of the file
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean the content by removing non-alphanumeric characters
    cleaned_content = re.sub(r'\W', ' ', content)

    # Convert the text to lowercase and split it into words
    words = cleaned_content.lower().split()

    # Remove Turkish stopwords and words with less than 3 characters
    words = [word for word in words if word not in stop_words_turkish and len(word) > 2]

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Create a WordCloud
    wordcloud = WordCloud(width=800,
                          height=400,
                          stopwords=stop_words_turkish,
                          contour_width=3,
                          contour_color='steelblue',
                          colormap="viridis",
                          background_color='white').generate_from_frequencies(word_counts)

    # Show the WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Save the WordCloud as an image file
    plt.savefig(cloud_image_name, bbox_inches='tight')
    plt.show()
def get_top_words(file_path, top_n=20):
    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}

    # Clean the text (keeping only alphanumeric characters, removing others)
    cleaned_text = re.sub(r'\W', ' ', text)

    # Convert the text to lowercase and split it into words
    words = cleaned_text.lower().split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Select the top words
    top_words = word_counts.most_common(top_n)

    # Create the word_frequency_data dictionary
    word_frequency_data = {}
    for word, count in top_words:
        word_frequency_data[word] = count

    return word_frequency_data
    
