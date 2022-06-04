import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from textblob import TextBlob




def clean(sentence):
    cleaned = ''
    for i in sentence:
        if i.isalpha() or i == ' ':
            cleaned += i.lower()
    return ' '.join(cleaned.split()) 


def lemma_format(sentence):
  words = word_tokenize(sentence.lower())
  not_stop_words = []
  for word in words:
    if word not in stopwords.words('english'):
      not_stop_words.append(word)
      
  tags = pos_tag(not_stop_words)
  pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}  
  lemma_form = []
  for word, tag in tags:
    if tag[0] in pos_dict:
      lemma_form.append((word, pos_dict[tag[0]]))

  final_text = ''
  wnl = WordNetLemmatizer()
  for word, tag in lemma_form:
    final_text = final_text + ' ' + wnl.lemmatize(word, pos=tag)
     
  return final_text 


def get_polar(text):
    text = text.lower() 
    offensive_bad_words = ['cunt', 'slut', 'whore', 'hoe', 'bitch'] #
    polarity = TextBlob(text).sentiment.polarity
    if [True for word in offensive_bad_words if word in text]:
        polarity += -0.6
    return polarity