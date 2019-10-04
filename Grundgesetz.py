from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from spacy.lang.de.stop_words import STOP_WORDS

from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'Grundgesetz.txt')).read()

# read the mask image
eagle_mask = np.array(Image.open(path.join(d, "Eagle.png")))

stopwords = set(STOP_WORDS)
stopwords.add("Artikel")

wc = WordCloud(background_color="white", max_words=3000, mask=eagle_mask,
               stopwords=stopwords, contour_width=3, contour_color='black')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "Grundgesetz.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(eagle_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()