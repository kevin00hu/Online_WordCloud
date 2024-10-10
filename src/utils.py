from wordcloud import WordCloud
from PIL import Image

from .clean_text import clean

#=======================================================#

def generate_wordcloud(string:str, max_words:int=20)->Image:
    """ Generate a word cloud based on input string """

    cleaned_string = clean(string)

    wc = WordCloud(
        background_color='white',  # Set background color to white
        height=500,
        width=500,
        max_words=max_words
    ).generate(cleaned_string)

    return wc.to_image()
