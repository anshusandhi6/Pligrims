#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QHBoxLayout,QFileDialog,QMessageBox
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import PyPDF2
import os.path

# importing libraries

import nltk
import gensim
import numpy as np
import pandas as pd
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
summer = ' '

location_1 = ''
location_2 = ''

tokenized_1 = []

tokenized_2 = []

extension_1 = ' '
extension_2 = ' '


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(1088, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.uploadfile_1 = QtWidgets.QPushButton(self.centralwidget)
        self.uploadfile_1.setGeometry(QtCore.QRect(80, 100, 191, 71))
        self.uploadfile_1.setObjectName('uploadfile_1')
        self.uploadfile_2 = QtWidgets.QPushButton(self.centralwidget)
        self.uploadfile_2.setGeometry(QtCore.QRect(770, 100, 191, 71))
        self.uploadfile_2.setObjectName('uploadfile_2')
        self.submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_1.setGeometry(QtCore.QRect(120, 210, 111, 41))
        self.submit_1.setObjectName('submit_1')
        self.submit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_2.setGeometry(QtCore.QRect(830, 210, 111, 41))
        self.submit_2.setObjectName('submit_2')
        self.percent = QtWidgets.QLineEdit(self.centralwidget)
        self.percent.setGeometry(QtCore.QRect(410, 190, 261, 91))
        self.percent.setObjectName('percent')
        self.summ_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.summ_1.setGeometry(QtCore.QRect(30, 340, 371, 321))
        self.summ_1.setObjectName('summ_1')
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(680, 340, 371, 321))
        self.textEdit_2.setObjectName('textEdit_2')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(84, 300, 171, 20))
        self.label.setObjectName('label')
        self.summ_2 = QtWidgets.QLabel(self.centralwidget)
        self.summ_2.setGeometry(QtCore.QRect(810, 300, 171, 20))
        self.summ_2.setObjectName('summ_2')
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(334, 20, 391, 101))
        self.label_3.setObjectName('label_3')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.uploadfile_1.clicked.connect(self.openFileDialog_1)
        self.uploadfile_2.clicked.connect(self.openFileDialog_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'
                                  ))
        self.uploadfile_1.setText(_translate('MainWindow',
                                  'Upload File-1'))
        self.uploadfile_2.setText(_translate('MainWindow',
                                  'Upload File-2'))
        self.submit_1.setText(_translate('MainWindow', 'Submit'))
        self.submit_2.setText(_translate('MainWindow', 'Submit'))
        self.percent.setText(_translate('MainWindow',
                             '                Plagarismn Percentage'))
        self.label.setText(_translate('MainWindow',
                           '      Summary of File-1'))
        self.summ_2.setText(_translate('MainWindow',
                            '      Summary of File-2'))
        self.label_3.setText(_translate('MainWindow',
                             '                             PROJECT - PLIGIRMS'
                             ))

    def pdf_extract(self):
        global tokenized_1
        global tokenized_2
        if len(tokenized_1) == 0:

            f1 = open(location_1, 'rb')
            nltk.download('punkt')
            read1 = PyPDF2.PdfFileReader(f1)
            pdf_text_1 = [0]
            for p in range(read1.numPages):

                page = read1.getPage(p)

                pdf_text_1.append(page.extractText())

            for data in pdf_text_1:

                token_1 = sent_tokenize(str(data))

                for line in token_1:

                    tokenized_1.append(line)
        else:

            f2 = open(location_2, 'rb')

            nltk.download('punkt')
            read2 = PyPDF2.PdfFileReader(f2)

            # extracting texts from file 2

            pdf_text_2 = [0]

            for p in range(read2.numPages):

                page = read2.getPage(p)

                pdf_text_2.append(page.extractText())

            for data in pdf_text_2:

                token_2 = sent_tokenize(str(data))

                for line in token_2:

                    tokenized_2.append(line)

    def doc_extract(self):
        global tokenized_1
        global tokenized_2
        if len(tokenized_1) == 0:

            f1 = open(location_1)

            for data in f1:

                token_1 = sent_tokenize(str(data))

                for line in token_1:

                    tokenized_1.append(line)
        else:

            f2 = open(location_2)

            for data in f2:

                token_2 = sent_tokenize(str(data))

                for line in token_2:

                    tokenized_2.append(line)

    def caller(self):

        global extension_1
        global extension_2
        global location_1
        global location_2
        global tokenized_1
        global tokenized_1

        if len(location_2) == 0:
            aextension = location_1.split('.')
            extension_1 = aextension[1]
            if extension_1 == 'pdf':

                self.pdf_extract()
            else:

                self.doc_extract()
        else:

            bextension = location_2.split('.')
            extension_2 = bextension[1]
            if extension_2 == 'pdf':
                self.pdf_extract()
            else:

                self.doc_extract()
        print(location_1)
        print(" er")
        print(location_2)
        if len(location_1) != 0 and len(location_2) != 0:
            
            if location_1 == location_2:
                fname = '100'
                self.percent.setText(fname)
                tokenized_1.clear()
                tokenized_2.clear()
                location_1 = ''
                location_2 = ''
                extension_1 = ''
                extension_2 = ''
            else:
                word_tokenized_1 = [[word.lower() for word in
                                    word_tokenize(str(text))]
                                    for text in tokenized_1]
                dictionary = gensim.corpora.Dictionary(word_tokenized_1)
                corpus = [dictionary.doc2bow(words) for words in
                          word_tokenized_1]
                tf_idf = gensim.models.TfidfModel(corpus)

                sims = gensim.similarities.Similarity('',
                        tf_idf[corpus], num_features=len(dictionary))

                for line in tokenized_1:

                    word_tokenized_2 = [w.lower() for w in
                            word_tokenize(line)]

                    query_doc_bow = dictionary.doc2bow(word_tokenized_2)
                query_doc_tf_idf = tf_idf[query_doc_bow]

                sum_of_sims = np.sum(sims[query_doc_tf_idf],
                        dtype=np.float32)

                fname = str(sum_of_sims / len(sims[query_doc_tf_idf])
                            * 100)
                self.percent.setText(fname)
                tokenized_1.clear()
                tokenized_2.clear()
                location_1 = ''
                location_2 = ''
                extension_1 = ''
                extension_2 = ''

    def openFileDialog_1(self):
        global location_1
        option = QFileDialog.Options()
        widget = QWidget()
        file = QFileDialog.getOpenFileName(widget, 'Open Single File',
                'Default File', '',
                options=option)
        f = open(file[0], 'rb')
        location_1 = file[0]
        aextension = location_1.split('.')
        extension = aextension[1]
        if extension == "pdf":
            f = open(file[0], 'rb')
            text = [0]  # zero is a placehoder to make page 1 = index 1

            pdf_reader = PyPDF2.PdfFileReader(f)

            for p in range(pdf_reader.numPages):

                page = pdf_reader.getPage(p)

                text.append(page.extractText())

            f.close()
            text = ' '.join([str(elem) for elem in text])
        elif extension == "txt" :
            f = open(file[0])
            text = f.read()

        else :
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter a valid File")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()
        doc = nlp(text)
        tokens = [token.text for token in doc]
        from string import punctuation
        punctuation = punctuation + '\n'
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1

        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():

            word_frequencies[word] = word_frequencies[word] \
                / max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = \
                            word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += \
                            word_frequencies[word.text.lower()]

        from heapq import nlargest

        select_length = int(len(sentence_tokens) * 0.35)
        summary = nlargest(select_length, sentence_scores,
                           key=sentence_scores.get)
        summary = ' '.join([str(elem) for elem in summary])
        self.summ_1.setText(summary)

        self.caller()

    def openFileDialog_2(self):
        global location_2
        option = QFileDialog.Options()
        widget = QWidget()
        file1 = QFileDialog.getOpenFileName(widget, 'Open Single File',
                'Default File', '', options=option)
        f = open(file1[0], 'rb')
        location_2 = file1[0]
        aextension1 = location_2.split('.')
        extension1 = aextension1[1]
        if extension1 == "pdf":
            f = open(file1[0], 'rb')
            location_2 = file1[0]
            text = [0]  # zero is a placehoder to make page 1 = index 1

            pdf_reader = PyPDF2.PdfFileReader(f)

            for p in range(pdf_reader.numPages):

                page = pdf_reader.getPage(p)

                text.append(page.extractText())

            f.close()
            text = ' '.join([str(elem) for elem in text])
        elif extension1 == "txt" :
            f = open(file1[0])
            location_2 = file1[0]
            text = f.read()

        else :
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter a valid File")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()

        
        doc = nlp(text)
        tokens = [token.text for token in doc]
        from string import punctuation
        punctuation = punctuation + '\n'
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1

        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():

            word_frequencies[word] = word_frequencies[word] \
                / max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = \
                            word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += \
                            word_frequencies[word.text.lower()]

        from heapq import nlargest

        select_length = int(len(sentence_tokens) * 0.35)
        summary = nlargest(select_length, sentence_scores,
                           key=sentence_scores.get)
        summary = ' '.join([str(elem) for elem in summary])
        self.textEdit_2.setText(summary)
        self.caller()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
