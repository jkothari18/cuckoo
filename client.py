import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Client(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.html = self.toHtml(self.Callable)
        print("Load done")

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()
