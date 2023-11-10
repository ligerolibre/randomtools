import sys
import random
from PySide6.QtCore import QTimer
from PySide6 import QtCore, QtWidgets, QtGui

# 위젯 선언
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        print("== Welcome ==")

        # Please do not delete this line!!
        print("Copyright 2023 Seoyoungwoo.")

        self.setWindowTitle("🎤 노래 선정 시스템")
        self.setMinimumSize(600, 600)

        # 시계
        self.clock = QtWidgets.QLabel()
        self.clock.setAlignment(QtCore.Qt.AlignCenter)
        self.clock.setMaximumHeight(20)
        clockFont = self.clock.font()
        clockFont.setPointSize(20)
        self.clock.setFont(clockFont)
        self.timeNow = QTimer()
        self.timeNow.timeout.connect(self.update_time)
        self.timeNow.start(1000)
        self.update_time()

        print("Program Start DateTime :",QtCore.QDateTime.currentDateTime().toString('yyyy년 MM월 dd일 hh:mm:ss'))

        # 노래 리스트
        self.list = ["사건의 지평선", "오르트구름", "바람", "약속", "오늘 혜어졌어요."]
        
        print("뽑기 아이템 항목 :",str(self.list))

        print("[조작 방지 시스템] 조작 방지 시스템이 실행 되었습니다. 뽑기 버튼을 누를 때 마다 조작 여부를 검증합니다.")
        self.safetyText = QtWidgets.QLabel("조작 방지 시스템이 실행되고 있습니다.")
        
        self.safetyText.setAlignment(QtCore.Qt.AlignCenter)
        self.safetyText.setMaximumHeight(20)
        safetyTextFont = self.safetyText.font()
        safetyTextFont.setPointSize(20)
        self.safetyText.setFont(safetyTextFont)
        self.safetyText.setStyleSheet("color: green;")

        self.buttonReset = QtWidgets.QPushButton("초기화")
        self.button = QtWidgets.QPushButton("뽑기")

        self.text = QtWidgets.QLabel("아래 버튼을 눌러 곡을 뽑으세요!",
                                     alignment=QtCore.Qt.AlignCenter)
        font = self.text.font()
        font.setPointSize(30)
        self.text.setFont(font)
        self.text.setStyleSheet("color: blue;")

        font = self.buttonReset.font()
        font.setPointSize(30)
        self.buttonReset.setFont(font)
        self.buttonReset.setStyleSheet("""
            QPushButton {
                background-color: grey;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: darkgrey;
            }
        """)

        font = self.button.font()
        font.setPointSize(30)
        self.button.setFont(font)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: skyblue;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
        """)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.clock)
        self.layout.addWidget(self.safetyText)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.buttonReset)
        self.layout.addWidget(self.button)

        self.buttonReset.clicked.connect(self.reset)
        self.button.clicked.connect(self.check_list)

    def update_time(self):
        current_time = QtCore.QDateTime.currentDateTime()
        display_text = current_time.toString('yyyy년 MM월 dd일 hh:mm:ss')
        self.clock.setText(display_text)

    def countdown_timer (self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000) # update every second
        self.countdown = 6

    def update_countdown(self):
        self.countdown -= 1
        if self.countdown == 0:
            self.timer.stop()
            self.magic()
        else:
            font = self.text.font()
            font.setPointSize(100)
            self.text.setFont(font)
            self.text.setStyleSheet("color: red;")
            self.text.setText(str(self.countdown))

    # 조작 체크
    def check_list(self):
        duplicates = []

        for item in self.list:
            if self.list.count(item) > 1 and item not in duplicates:
                duplicates.append(item)
        
        if len(self.list) == 1:
            self.warning_msg(warnItem = str(self.list))
        elif len(duplicates) > 0:
            self.warning_msg(warnItem = str(duplicates))
        else:
            self.countdown_timer()
    
    # 조작 알림
    def warning_msg(self, warnItem):
        # create a message box with information icon
        msg = QtWidgets.QMessageBox()
        print('[조작방지시스템] 조작 시도 감지됨.', warnItem)
        warnItemText = warnItem.replace("[", "\"").replace("]", "\"").replace("\'", "")
        self.safetyText.setText("조작 시도가 감지 되었습니다. " + warnItemText )
        self.safetyText.setStyleSheet("color: red;") 

        # set the window title and message text
        msg.setText("조작 시도 감지됨.")
        msg.setInformativeText(warnItemText + " 아이템의 확률 조작 시도가 있었습니다.")

        # display the message box
        msg.exec()

    # 랜덤 메시지 생성
    def magic(self):
        font = self.text.font()
        font.setPointSize(60)
        self.text.setFont(font)
        self.text.setStyleSheet("color: green;")
        text = random.choice(self.list)
        self.text.setText(text)
        print(text,QtCore.QDateTime.currentDateTime().toString('yyyy년 MM월 dd일 hh:mm:ss'))

    def reset(self):
        font = self.text.font()
        font.setPointSize(30)
        self.text.setFont(font)
        self.text.setStyleSheet("color: blue;")
        print('== Reset ==')
        self.text.setText("아래 버튼을 눌러 곡을 뽑으세요!")
        self.timer.stop()
        

# 어플리케이션 호출 및 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
