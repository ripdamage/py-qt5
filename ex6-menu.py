#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        secondMenu = menubar.addMenu('&Second')
        
        exitAction = QAction(QIcon('assets/exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        dummyAction = QAction(QIcon('assets/web.png'), '&Dummy', self)        
        dummyAction.setShortcut('Ctrl+D')
        dummyAction.setStatusTip('Dummy action')

        self.statusBar()

        fileMenu.addAction(exitAction)

        secondMenu.addAction(dummyAction)

        # Native menu is probably tricky in OSX
        menubar.setNativeMenuBar(False)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 
