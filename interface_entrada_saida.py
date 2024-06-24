from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ES(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 499)
        Dialog.setStyleSheet("background-color: rgb(35, 39, 45);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_pesquisar_produto = QtWidgets.QLabel(Dialog)
        self.label_pesquisar_produto.setMinimumSize(QtCore.QSize(291, 51))
        self.label_pesquisar_produto.setMaximumSize(QtCore.QSize(291, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_pesquisar_produto.setFont(font)
        self.label_pesquisar_produto.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_pesquisar_produto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pesquisar_produto.setObjectName("label_pesquisar_produto")
        self.horizontalLayout_5.addWidget(self.label_pesquisar_produto)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_entrada_3 = QtWidgets.QLabel(Dialog)
        self.label_entrada_3.setMinimumSize(QtCore.QSize(120, 30))
        self.label_entrada_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_entrada_3.setFont(font)
        self.label_entrada_3.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_entrada_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_entrada_3.setObjectName("label_entrada_3")
        self.horizontalLayout.addWidget(self.label_entrada_3)
        self.digitar_id_es = QtWidgets.QLineEdit(Dialog)
        self.digitar_id_es.setMinimumSize(QtCore.QSize(520, 30))
        self.digitar_id_es.setMaximumSize(QtCore.QSize(520, 30))
        self.digitar_id_es.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_id_es.setText("")
        self.digitar_id_es.setObjectName("digitar_id_es")
        self.horizontalLayout.addWidget(self.digitar_id_es)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_entrada = QtWidgets.QLabel(Dialog)
        self.label_entrada.setMinimumSize(QtCore.QSize(120, 30))
        self.label_entrada.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_entrada.setFont(font)
        self.label_entrada.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_entrada.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_entrada.setObjectName("label_entrada")
        self.horizontalLayout_2.addWidget(self.label_entrada)
        self.digitar_entrada = QtWidgets.QLineEdit(Dialog)
        self.digitar_entrada.setMinimumSize(QtCore.QSize(520, 30))
        self.digitar_entrada.setMaximumSize(QtCore.QSize(520, 30))
        self.digitar_entrada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_entrada.setObjectName("digitar_entrada")
        self.horizontalLayout_2.addWidget(self.digitar_entrada)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_entrada_2 = QtWidgets.QLabel(Dialog)
        self.label_entrada_2.setMinimumSize(QtCore.QSize(120, 30))
        self.label_entrada_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_entrada_2.setFont(font)
        self.label_entrada_2.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_entrada_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_entrada_2.setObjectName("label_entrada_2")
        self.horizontalLayout_3.addWidget(self.label_entrada_2)
        self.digitar_saida = QtWidgets.QLineEdit(Dialog)
        self.digitar_saida.setMinimumSize(QtCore.QSize(520, 30))
        self.digitar_saida.setMaximumSize(QtCore.QSize(520, 30))
        self.digitar_saida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_saida.setObjectName("digitar_saida")
        self.horizontalLayout_3.addWidget(self.digitar_saida)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.btn_fluxo_salvar = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fluxo_salvar.sizePolicy().hasHeightForWidth())
        self.btn_fluxo_salvar.setSizePolicy(sizePolicy)
        self.btn_fluxo_salvar.setMinimumSize(QtCore.QSize(400, 60))
        self.btn_fluxo_salvar.setMaximumSize(QtCore.QSize(400, 60))
        self.btn_fluxo_salvar.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_fluxo_salvar.setObjectName("btn_fluxo_salvar")
        self.horizontalLayout_4.addWidget(self.btn_fluxo_salvar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_pesquisar_produto.setText(_translate("Dialog", "Fluxo de Produtos"))
        self.label_entrada_3.setText(_translate("Dialog", "Produto"))
        self.digitar_id_es.setPlaceholderText(_translate("Dialog", "Id ou descrição"))
        self.label_entrada.setText(_translate("Dialog", "Entrada"))
        self.digitar_entrada.setPlaceholderText(_translate("Dialog", "Deixar em branco caso esteja cadastrando saída de produtos."))
        self.label_entrada_2.setText(_translate("Dialog", "Saída"))
        self.digitar_saida.setPlaceholderText(_translate("Dialog", "Deixar em branco caso esteja cadastrando entrada de produtos."))
        self.btn_fluxo_salvar.setText(_translate("Dialog", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ES()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())