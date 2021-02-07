#importing libraries
import nltk
import gensim
import numpy as np
import pandas as pd
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

#reading files


import PyPDF2



#getting the two pdf files
f1 = open("sample 2.pdf",'rb')



#reading both files
read1 = PyPDF2.PdfFileReader(f1)




#extracting texts from file 1
pdf_text_1 = [0]

for p in range(read1.numPages):

  page = read1.getPage(p)

  pdf_text_1.append(page.extractText())







#importing word and ssentence tokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

#sentence tokenization of both files
tokenized_1 =[]

tokenized_2 =[]

for data in pdf_text_1:

  token_1 =sent_tokenize(str(data))

  for line in token_1:

    tokenized_1.append(line)


print(type(tokenized_1))