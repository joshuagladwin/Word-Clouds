from os import path
from PIL import Image
import numpy as np
import os
import spacy
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud



d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


nlp = spacy.load('ja_core_news_sm')
doc = open(path.join(d, 'sekaijinkensengen.txt')).read()
doc = nlp(doc)


words = [token.lemma_ for token in doc if token.is_stop != True and 
         token.is_punct != True and token.is_digit != True and token.is_alpha == True and
         token.pos_ == "NOUN"]

word_freq = Counter(words)
common_words = word_freq.most_common(20)
  
#words_to_remove = ['Artikel', 'Absatz', 'Satz', 'Abs.', 'Grund','Gesetz']

# for word in words_to_remove:
#     stopwords.add(word)

words = ' '.join(words)


# def multi_color_func(word=None, font_size=None,
#                       position=None, orientation=None,
#                       font_path=None, random_state=None):
#     colors = [[0, 97, 45],
#               [33, 100, 50],
#               [56, 100, 50],
#               [138, 100, 25],
#               [222, 100, 50],
#               [292, 90, 28],
#               # [0, 0, 0],
#               # [35, 68, 28],
#               # [197, 94, 67],
#               # [348, 79, 81]
#               ]
#     rand = random_state.randint(0, len(colors) - 1)
#     return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])

# mask = np.array(Image.open(path.join(d, "Germany.png")))


# font_path = 'C:/Users/joshu/Documents/Languages/Tools/Fonts/lemon_milk/LEMONMILK-Regular.otf'

# wc = WordCloud(background_color="white", max_words=3000, mask=mask, 
#                 font_path=font_path, stopwords=stopwords,
#                 max_font_size=256, random_state=42,
#                 color_func=multi_color_func, contour_color='gray', contour_width=1)


# wc.generate(words)


# wc.to_file(path.join(d, "Grundrechte.png"))


# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.show()