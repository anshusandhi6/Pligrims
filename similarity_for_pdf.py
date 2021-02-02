import nltk

import gensim

import numpy as np

import pandas as pd

import PyPDF2




f1 = open("sample 1.pdf",'rb')

f2 = open("sample 2.pdf",'rb')



read1 = PyPDF2.PdfFileReader(f1)

read2 = PyPDF2.PdfFileReader(f2)



pdf_text_1 = [0]

for p in range(read1.numPages):

  page = read1.getPage(p)

  pdf_text_1.append(page.extractText())



pdf_text_2 = [0]

for p in range(read2.numPages):

  page = read2.getPage(p)

  pdf_text_2.append(page.extractText())





from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

tokenized_1 =[]

tokenized_2 =[]

for data in pdf_text_1:

  token_1 =sent_tokenize(str(data))

  for line in token_1:

    tokenized_1.append(line)



  



for data in pdf_text_2:

  token_2 = sent_tokenize(str(data))

  for line in token_2:

    tokenized_2.append(line)





word_tokenized_1 = [[word.lower() for word in word_tokenize(str(text))] for text in tokenized_1]





dictionary = gensim.corpora.Dictionary(word_tokenized_1)




corpus = [dictionary.doc2bow(words) for words in word_tokenized_1]





tf_idf = gensim.models.TfidfModel(corpus)




sims = gensim.similarities.Similarity('',tf_idf[corpus],

                                        num_features=len(dictionary))



for line in tokenized_1:

    word_tokenized_2 = [w.lower() for w in word_tokenize(line)]

    query_doc_bow = dictionary.doc2bow(word_tokenized_2)



query_doc_tf_idf = tf_idf[query_doc_bow]





sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))

print('Percentage similarity between the two documents is: ' + str((sum_of_sims/len(sims[query_doc_tf_idf]))*100))

