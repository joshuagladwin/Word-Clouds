from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import spacy
from spacy.lang.de.stop_words import STOP_WORDS


from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

nlp = spacy.load('de_core_news_sm')

# Read the whole text.
text = open(path.join(d, 'Grundrechte.txt')).read()

text = nlp(text)

processed_text = ''

for word in text:
    processed_text += (word.lemma_ +' ')
    
stopwords = set(STOP_WORDS)
stopwords.add("Artikel")
stopwords.add("Abs")
stopwords.add("Satz")


def multi_color_func(word=None, font_size=None,
                     position=None, orientation=None,
                     font_path=None, random_state=None):
    colors = [[0, 97, 45],
              [33, 100, 50],
              [56, 100, 50],
              [138, 100, 25],
              [222, 100, 50],
              [292, 90, 28],
              # [0, 0, 0],
              # [35, 68, 28],
              # [197, 94, 67],
              # [348, 79, 81]
              ]
    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])

mask = np.array(Image.open(path.join(d, "Germany.png")))


font_path = 'C:/Users/joshu/Documents/Languages/Tools/Fonts/lemon_milk/LEMONMILK-Regular.otf'

wc = WordCloud(background_color="white", max_words=3000, mask=mask, 
               font_path=font_path, stopwords=stopwords,
               max_font_size=256, random_state=42,
               color_func=multi_color_func, contour_color='gray', contour_width=1)


wc.generate(processed_text)


wc.to_file(path.join(d, "Grundgesetz1.png"))


plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()