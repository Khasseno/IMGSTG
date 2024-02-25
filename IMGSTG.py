import sys

from PIL import Image, ImageQt
from UIc.IMGSTG_WELCOME import Ui_MainWindow
from UIc.extracting_information import Ui_Dialog_Extracting
from UIc.adding_information import Ui_Dialog_Adding
from PySide6.QtCore import Qt, QDir
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QFileDialog, QMessageBox, QLabel

from StegoLSB.stego import StegoLSB

class IMGSTG(QMainWindow):
    def __init__(self) -> None:
        super(IMGSTG, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.b_izvlechenie.clicked.connect(self.__show_extraction)
        self.ui.b_vnedrenie.clicked.connect(self.__show_adding)
        
    # ============================== Show Dialogs Fragment
    def __show_extraction(self):
        self.dialog_window = QDialog()
        
        self.dialog_ui_window = Ui_Dialog_Extracting()
        self.dialog_ui_window.setupUi(self.dialog_window)
        self.dialog_window.setFixedSize(self.dialog_window.width(),self.dialog_window.height())
        self.dialog_window.setWindowTitle("Извлечение данных из изображения")
        self.dialog_window.setModal(True)

        
        self.dialog_window.show()
        
        self.dialog_ui_window.b_add_img.clicked.connect(self.__add_img_to_label)
        self.dialog_ui_window.b_extract_data.clicked.connect(self.__check_image_on_lsb)
        
    def __show_adding(self):
        self.dialog_window = QDialog()
        
        self.dialog_ui_window = Ui_Dialog_Adding()
        self.dialog_ui_window.setupUi(self.dialog_window)
        self.dialog_window.setFixedSize(self.dialog_window.width(),self.dialog_window.height())
        self.dialog_window.setWindowTitle("Внедрение данных в изображение")
        self.dialog_window.setModal(True)
        
        self.dialog_window.show()

        self.dialog_ui_window.b_add_img.clicked.connect(self.__add_img_to_label)
        self.dialog_ui_window.b_add_data.clicked.connect(self.__hide_data_in_img)
        self.dialog_ui_window.b_save.clicked.connect(self.__download_stego_img)
    
    
    # ============================== Add Image to Label Fragment
    def __add_img_to_label(self):
        
        self.file_dialog = QFileDialog()
        self.file_dialog.setFilter(QDir.Filter.Files)
        selected_file_path = self.file_dialog.getOpenFileNames(self,
                                                                "Select one file to open",
                                                                "./",
                                                                "Images (*.png *.xpm *.jpg *.jpeg *.tiff)")[0][0]
        picture = QPixmap(selected_file_path)
        
        IMGSTG.__show_img_in_label(self.dialog_ui_window.l_image_add, picture)
        
        self.stego_lsb = StegoLSB(selected_file_path)
      
    @staticmethod  
    def __show_img_in_label(label: QLabel, img: QPixmap):
        margin_b_t = (300 - (img.height() / (img.width() / 200))) // 2
        margin_l_r = (200 - (img.width() / (img.height() / 300))) // 2
        label.setPixmap(img)
        label.setScaledContents(True)
        label.setContentsMargins(margin_l_r,margin_b_t,margin_l_r,margin_b_t)
    
    
    # ============================== Extracting Information Functional
    def __check_image_on_lsb(self):
        if self.dialog_ui_window.l_image_add.pixmap().isNull():
            self.__show_message_box("Нет изображения")
            return None
        
        img = Image.fromqpixmap(self.dialog_ui_window.l_image_add.pixmap()).tobytes()
        stegoImg = StegoLSB(img)
        
        try:
            foundedData = stegoImg.seekData(2)
            self.dialog_ui_window.l_data_extract.setWordWrap(True)
            self.dialog_ui_window.l_data_extract.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
            style = self.dialog_ui_window.l_data_extract.styleSheet()
            self.dialog_ui_window.l_data_extract.setStyleSheet(style + "; color: white; font-size: 15px")
            self.dialog_ui_window.l_data_extract.setText(foundedData)
        except UnicodeDecodeError:
            self.__show_message_box("Изображение не содержит скрытой информации")
    
        
    # ============================== Adding Information Functional
    def __hide_data_in_img(self):
        message = ""
        if self.dialog_ui_window.text.toPlainText().strip() == "":
            message += "Введите данные\n"
        
        if self.dialog_ui_window.l_image_add.pixmap().isNull():
           message += "Выберите изображение\n"
        
        if message:
            self.__show_message_box(message)
            return None
        
        data = (self.dialog_ui_window.text.toPlainText()).encode('utf-8')
        img_with_stego = self.stego_lsb.hideData(data, 2)
        IMGSTG.__show_img_in_label(self.dialog_ui_window.l_image_save, img_with_stego.toqpixmap())
                
    def __download_stego_img(self):
        if self.dialog_ui_window.l_image_save.pixmap().isNull():
            self.__show_message_box("Нет изображения")
            return None
        
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        selected_download_path = self.file_dialog.getSaveFileName(self,
                                                                  "Select one file to open",
                                                                  "./",
                                                                  "Images (*.png *.xpm *.jpg *.tiff)")[0]
        
        if self.dialog_ui_window.l_image_save.pixmap().save(selected_download_path, selected_download_path.split('.')[-1]):
            self.__show_message_box(f"Файл сохранён по пути:\n{selected_download_path}")
       
    # ============================== Helper functions
    def __show_message_box(self, message):
        mbox = QMessageBox(self.dialog_window)
        mbox.setWindowTitle("Внимание!")
        mbox.setStyleSheet("color: black; \
                            font-weight: 100; \
                            text-decoration: none; \
                            background-color: none; \
                            font-family: none")
        mbox.setText(message)
        mbox.show()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMGSTG()
    
    window.setFixedSize(window.width(), window.height())
    
    window.show()
    
    sys.exit(app.exec())