import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound
import pyttsx3

used_codes = []
data_list = []

#try:
f = open("qrbarcode_data2.txt", "r", encoding="utf8")
data_list = f.readlines()
#except FileNotFoundError:
#    pass
#else:
#    f.close()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

for i in data_list:
    used_codes.append(i.rstrip('\n'))

while True:
    success, frame = cap.read()

    for code in pyzbar.decode(frame):
        cv2.imwrite('qrbarcode_image.png', frame)
        my_code = code.data.decode('utf-8')
        if my_code not in used_codes:
            print("인식 성공 : ", my_code)
            playsound("qrbarcode_beep.mp3")

            used_codes.append(my_code)

            f2 = open("qrbarcode_data2.txt", "a", encoding="utf8")
            f2.write(my_code+'\n')
            f2.close()

            engine = pyttsx3.init()

            engine.setProperty('rate', 200)

            engine.say('선택하신 상품은 %s 입니다'%my_code)

            engine.runAndWait()
        elif my_code in used_codes:
            print("이미 인식된 코드 입니다.!!!")
            playsound("qrbarcode_beep.mp3")

            engine = pyttsx3.init()

            engine.setProperty('rate', 200)

            engine.say('선택하신 상품은 %s 입니다'%my_code)

            engine.runAndWait()
        else:
            pass

    cv2.imshow('QRcode Barcode Scan', frame)

    key = cv2.waitKey(1)
    if key==27:
        break
    

