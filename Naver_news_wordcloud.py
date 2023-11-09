import json
import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

nlp = Okt()
word_count = dict()
message = ''

inputFileName = './data/범죄도시_naver_news'
data = json.loads(open(inputFileName+'.json', 'r', encoding='utf-8').read())

for item in data:
    message += re.sub(r'[^\w]', ' ', item['title']) + re.sub(r'[^\w]', ' ',item['description'])

message_N = nlp.nouns(message)
count = Counter(message_N)

for tag, counts in count.most_common(80):
    if(len(str(tag))>1):
        word_count[tag] = counts

font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname = font_path).get_name()
matplotlib.rc('font', family=font_name)

wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)

plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

cloud.to_file(inputFileName + '_cloud.jpg')