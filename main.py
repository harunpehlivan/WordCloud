#required module - pip install wordcloud
from wordcloud import WordCloud, STOPWORDS

#pip install matplotlib
import matplotlib.pyplot as plt

#for removing duplicate words
stopwords = set(STOPWORDS)

#file the contains the words
file = open('textfile.txt', 'r')

#Creating wordcloud data
wordcloud = WordCloud(width=800, height=800, background_color='white',
                      stopwords=stopwords, min_font_size=20).generate(file.read())

#Creating image of wordcloud
plt.imshow(wordcloud)

#Hiding axis 
plt.axis("off")

#Showing the image 
plt.show()