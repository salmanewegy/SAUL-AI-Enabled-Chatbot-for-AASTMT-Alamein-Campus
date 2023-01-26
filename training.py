from multiprocessing.dummy import active_children
import random 
import json
import pickle 
import numpy as np
#import tensorflow
import tensorflow 
from tensorflow import keras
print('tensorflow version', tensorflow.__version__)
import farasa 
from farasa.pos import FarasaPOSTagger
from farasa.ner import FarasaNamedEntityRecognizer
from farasa.diacratizer import FarasaDiacritizer
from farasa.segmenter import FarasaSegmenter
from farasa.stemmer import FarasaStemmer

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json', encoding="utf8").read())
#with open('intents.json') as json_data:
#    intents = json.load(json_data)
