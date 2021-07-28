from PIL import Image
import sys
from PyQt5 import QtCore,QtGui,QtWidgets

class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(498,198)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-30,90,581,80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout2.setContentsMargins(0,0,0,0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.pushButton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.horizontalLayout2.addWidget(self.pushButton2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout2.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20,40,81,20))
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(20,10,61,20))
        self.label2.setObjectName("label2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90,0,211,31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit2 = QtWidgets.QTextEdit(Form)
        self.textEdit2.setGeometry(QtCore.QRect(90,30,211,31))
        self.textEdit2.setObjectName("textEdit2")
        self.pushButton2.clicked.connect(self.kirp)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self,Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form","Form"))
        self.pushButton2.setText(_translate("Form","Kırp"))
        self.pushButton.setText(_translate("Form","Sil"))
        self.label.setText(_translate("Form","Boyutlar"))
        self.label2.setText(_translate("Form","Foto İsmi"))

    def kirp(self):
        image2 = Image.open(self.textEdit.toPlainText())
        kirpilacakalan = (self.textEdit2.toPlainText())
        image = image2.crop(kirpilacakalan).save('atam.jpg')
        image.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

