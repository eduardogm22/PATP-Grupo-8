from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 777)
        MainWindow.setStyleSheet("background-color: rgb(35, 39, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_produtos = QtWidgets.QWidget()
        self.page_produtos.setObjectName("page_produtos")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_produtos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_editar_3 = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editar_3.sizePolicy().hasHeightForWidth())
        self.btn_editar_3.setSizePolicy(sizePolicy)
        self.btn_editar_3.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_editar_3.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_editar_3.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_editar_3.setObjectName("btn_editar_3")
        self.horizontalLayout.addWidget(self.btn_editar_3)
        self.btn_add_2 = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_2.sizePolicy().hasHeightForWidth())
        self.btn_add_2.setSizePolicy(sizePolicy)
        self.btn_add_2.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_add_2.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_add_2.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_add_2.setObjectName("btn_add_2")
        self.horizontalLayout.addWidget(self.btn_add_2)
        self.btn_remove_2 = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remove_2.sizePolicy().hasHeightForWidth())
        self.btn_remove_2.setSizePolicy(sizePolicy)
        self.btn_remove_2.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_remove_2.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_remove_2.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_remove_2.setObjectName("btn_remove_2")
        self.horizontalLayout.addWidget(self.btn_remove_2)
        self.btn_editar_2 = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editar_2.sizePolicy().hasHeightForWidth())
        self.btn_editar_2.setSizePolicy(sizePolicy)
        self.btn_editar_2.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_editar_2.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_editar_2.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_editar_2.setObjectName("btn_editar_2")
        self.horizontalLayout.addWidget(self.btn_editar_2)
        self.label = QtWidgets.QLabel(self.page_produtos)
        self.label.setStyleSheet("background-color: #2a3137;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 40pt \"Times New Roman\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.page_produtos)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.stackedWidget.addWidget(self.page_produtos)
        self.page_cadastro = QtWidgets.QWidget()
        self.page_cadastro.setObjectName("page_cadastro")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_cadastro)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cadastro_prod = QtWidgets.QLabel(self.page_cadastro)
        self.label_cadastro_prod.setMaximumSize(QtCore.QSize(1500, 70))
        self.label_cadastro_prod.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 30pt \"Times New Roman\";")
        self.label_cadastro_prod.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cadastro_prod.setObjectName("label_cadastro_prod")
        self.verticalLayout_2.addWidget(self.label_cadastro_prod)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.page_cadastro)
        self.label_3.setMinimumSize(QtCore.QSize(110, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.page_cadastro)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.page_cadastro)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_cadastro)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.page_cadastro)
        self.label_8.setMinimumSize(QtCore.QSize(110, 0))
        self.label_8.setMaximumSize(QtCore.QSize(100, 25))
        self.label_8.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_cadastro)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_cadastro)
        self.label_5.setMinimumSize(QtCore.QSize(110, 0))
        self.label_5.setMaximumSize(QtCore.QSize(100, 25))
        self.label_5.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_cadastro)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.page_cadastro)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 25))
        self.label_6.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_cadastro)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_salvar = QtWidgets.QPushButton(self.page_cadastro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy)
        self.btn_salvar.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_salvar.setMaximumSize(QtCore.QSize(400, 60))
        self.btn_salvar.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_salvar.setObjectName("btn_salvar")
        self.horizontalLayout_3.addWidget(self.btn_salvar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_cadastro)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_editar_3.setText(_translate("MainWindow", "Pesquisar"))
        self.btn_add_2.setText(_translate("MainWindow", "Adicionar"))
        self.btn_remove_2.setText(_translate("MainWindow", "Remover"))
        self.btn_editar_2.setText(_translate("MainWindow", "Editar"))
        self.label.setText(_translate("MainWindow", "Estoque Ideau"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Código"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Descrição"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Medida"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Fornecedor"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Fabricação"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Validade"))
        self.label_cadastro_prod.setText(_translate("MainWindow", "Cadastro de Produtos"))
        self.label_3.setText(_translate("MainWindow", "Descrição"))
        self.label_4.setText(_translate("MainWindow", "Medida"))
        self.label_8.setText(_translate("MainWindow", "Fornecedor"))
        self.label_5.setText(_translate("MainWindow", "Fabricação"))
        self.label_6.setText(_translate("MainWindow", "Validade"))
        self.btn_salvar.setText(_translate("MainWindow", "Adicionar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
