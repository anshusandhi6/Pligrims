


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QHBoxLayout,QFileDialog
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import PyPDF2

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadfile_1 = QtWidgets.QPushButton(self.centralwidget)
        self.uploadfile_1.setGeometry(QtCore.QRect(80, 100, 191, 71))
        self.uploadfile_1.setObjectName("uploadfile_1")
        self.uploadfile_2 = QtWidgets.QPushButton(self.centralwidget)
        self.uploadfile_2.setGeometry(QtCore.QRect(770, 100, 191, 71))
        self.uploadfile_2.setObjectName("uploadfile_2")
        self.submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_1.setGeometry(QtCore.QRect(120, 210, 111, 41))
        self.submit_1.setObjectName("submit_1")
        self.submit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_2.setGeometry(QtCore.QRect(830, 210, 111, 41))
        self.submit_2.setObjectName("submit_2")
        self.percent = QtWidgets.QLineEdit(self.centralwidget)
        self.percent.setGeometry(QtCore.QRect(410, 190, 261, 91))
        self.percent.setObjectName("percent")
        self.summ_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.summ_1.setGeometry(QtCore.QRect(30, 340, 371, 321))
        self.summ_1.setObjectName("summ_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(680, 340, 371, 321))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(84, 300, 171, 20))
        self.label.setObjectName("label")
        self.summ_2 = QtWidgets.QLabel(self.centralwidget)
        self.summ_2.setGeometry(QtCore.QRect(810, 300, 171, 20))
        self.summ_2.setObjectName("summ_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(334, 20, 391, 101))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.uploadfile_1.clicked.connect(self.openFileDialog_1)
        self.uploadfile_2.clicked.connect(self.openFileDialog_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uploadfile_1.setText(_translate("MainWindow", "Upload File-1"))
        self.uploadfile_2.setText(_translate("MainWindow", "Upload File-2"))
        self.submit_1.setText(_translate("MainWindow", "Submit"))
        self.submit_2.setText(_translate("MainWindow", "Submit"))
        self.percent.setText(_translate("MainWindow", "                Plagarismn Percentage"))
        self.label.setText(_translate("MainWindow", "      Summary of File-1"))
        self.summ_2.setText(_translate("MainWindow", "      Summary of File-2"))
        self.label_3.setText(_translate("MainWindow", "                             PROJECT - PLIGIRMS"))



    def openFileDialog_1(self):
        option=QFileDialog.Options()
        widget=QWidget()
        file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Files (*.txt, *.docx *.pdf)',options=option)
        f=open(file[0],'rb')
        text = [0]  # zero is a placehoder to make page 1 = index 1

        pdf_reader = PyPDF2.PdfFileReader(f)

        for p in range(pdf_reader.numPages):
            
            page = pdf_reader.getPage(p)
            
            text.append(page.extractText())

        f.close()
        text = ' '.join([str(elem) for elem in text]) 
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
            
            word_frequencies[word] = word_frequencies[word]/max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


        from heapq import nlargest

        select_length = int(len(sentence_tokens)*0.35)
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        summary = ' '.join([str(elem) for elem in summary]) 
        self.summ_1.setText(summary)
        
        


    def openFileDialog_2(self):
        option=QFileDialog.Options()
        widget=QWidget()
        file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Files (*.txt, *.docx *.pdf)',options=option)
        print(file[0])
        f=open(file[0],'rb')
        text = [0]  # zero is a placehoder to make page 1 = index 1

        pdf_reader = PyPDF2.PdfFileReader(f)

        for p in range(pdf_reader.numPages):
            
            page = pdf_reader.getPage(p)
            
            text.append(page.extractText())

        f.close()
        text = ' '.join([str(elem) for elem in text]) 
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
            
            word_frequencies[word] = word_frequencies[word]/max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


        from heapq import nlargest

        select_length = int(len(sentence_tokens)*0.35)
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        summary = ' '.join([str(elem) for elem in summary]) 
        self.textEdit_2.setText(summary)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
