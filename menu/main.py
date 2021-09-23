import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QAction
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.w = None  # No external window yet.

        self.setMinimumSize(QSize(700, 400))
        self.setWindowTitle("Vencendo Obstáculos")

        # Add button widget
        button1 = QPushButton('Começar', self)
        button1.clicked.connect(self.new_game_call)
        button1.resize(100, 30)
        button1.move(100, 150)

        button2 = QPushButton('Como jogar', self)
        button2.clicked.connect(self.how_to_play_call)
        # button2.clicked.connect(self.show_new_window)
        button2.resize(100, 30)
        button2.move(300, 150)

        button3 = QPushButton('Sobre o jogo', self)
        button3.clicked.connect(self.about_call)
        button3.resize(100, 30)
        button3.move(500, 150)

        # Create new action
        start_action = QAction(QIcon('newGame.png'), '&Iniciar', self)
        start_action.setShortcut('Ctrl+I')
        start_action.setStatusTip('Start new game')
        start_action.triggered.connect(self.new_game_call)

        # Create new action
        how_to_play_action = QAction(QIcon('howToPlay.png'), '&Como jogar', self)
        how_to_play_action.setShortcut('Ctrl+C')
        how_to_play_action.setStatusTip('Como jogar')
        how_to_play_action.triggered.connect(self.how_to_play_call)

        # Create new action
        about_action = QAction(QIcon('about.png'), '&Sobre o jogo', self)
        about_action.setShortcut('Ctrl+J')
        about_action.setStatusTip('sobre o jogo')
        about_action.triggered.connect(self.about_call)

        # Create exit action
        exit_action = QAction(QIcon('exit.png'), '&Sair', self)
        exit_action.setShortcut('Ctrl+S')
        exit_action.setStatusTip('Sair do jogo')
        exit_action.triggered.connect(self.exit_call)

        # Create menu bar and add action
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(start_action)
        file_menu.addAction(how_to_play_action)
        file_menu.addAction(about_action)
        file_menu.addAction(exit_action)

    def new_game_call(self):
        print('Começar')

    def how_to_play_call(self):
        print('Como jogar')
        self.w = HowToPlayWindow()
        self.w.show()

    def about_call(self):
        print('Sobre o jogo')
        self.w = AboutWindow()
        self.w.show()

    def exit_call(self):
        print('Sair do jogo')
        sys.exit()


class HowToPlayWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(700, 400))
        self.setWindowTitle("Como jogar")

        layout = QVBoxLayout()
        self.label = QLabel("Como jogar")
        layout.addWidget(self.label)
        self.setLayout(layout)


class AboutWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(700, 400))
        self.setWindowTitle("Sobre o jogo")

        layout = QVBoxLayout()
        self.label = QLabel("Sobre o jogo")
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
