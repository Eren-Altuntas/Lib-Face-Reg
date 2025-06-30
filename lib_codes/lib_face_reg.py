import time
import cv2
import face_recognition
import os
import datetime
import sqlite3

times = datetime.datetime.now()

nowtime = time.localtime().tm_hour 
file = open(os.getcwd()+"/yoklama.txt","a",encoding="utf-8")

db = sqlite3.connect('Library.db')
cr = db.cursor()

while True:
    try:
        # define a video capture object
        vid = cv2.VideoCapture(0)
  
        while True:
      
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
  
            # Display the resulting frame
            cv2.imshow('frame', frame)
            cv2.imwrite("C:/Users/user/Desktop/project/camphoto.jpg",frame)
      
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
 
        camphoto = face_recognition.load_image_file("C:/Users/user/Desktop/project/camphoto.jpg") # Fotoğraf yüklenir.
        camphoto = cv2.cvtColor(camphoto,cv2.COLOR_BGR2RGB) # Fotoğraf RGB'ye çevrilir.
        camphotofaceloc = face_recognition.face_locations(camphoto)[0] # Fotoğraftaki yüzün lokasyonlarını alır.
        camphotoencode = face_recognition.face_encodings(camphoto)[0] # Fotoğraf belirli parametrelere göre kodlanır.
        facephotos = os.listdir("C:/Users/user/Desktop/project/facephotos") # Dosyadaki fotoğraflar listelenir.
        for x in facephotos:
            bookphoto = face_recognition.load_image_file("C:/Users/user/Desktop/project/facephotos/"+x)
            bookphoto = cv2.cvtColor(bookphoto,cv2.COLOR_BGR2RGB)
            bookloc = face_recognition.face_locations(bookphoto)[0]
            encodephoto = face_recognition.face_encodings(bookphoto)[0]
            result = face_recognition.compare_faces([camphotoencode],encodephoto)
            #print(result,x)
            x = x.split(".")
            x = x[0]
            if result == [True]:
                a = str(times.day)
                file.write(x)
                file.write("| ")
                file.write(a)
                file.write("/")
                a = str(times.month)
                file.write(a)
                file.write("/")
                a = str(times.year)
                file.write(a)
                file.write("\n")
                #cv2.rectangle(photo,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),4) # Fotoğrafta belirlenen yüz işaretlenir.
                #cv2.imshow(x,photo)
                #cv2.waitKey(3000)
                # O anki saate göre işlem yapıyor.
                if nowtime >= 1 and nowtime <= 12:
                    print("Günaydın",x,"giriş yapabilirsin!")
                    exit()
                elif nowtime >= 12 and nowtime <= 18:
                    print("İyi günler",x,"giriş yapabilirsin!")
                    exit()
                elif nowtime >= 18 and nowtime <= 22:
                    print("İyi akşamlar",x,"giriş yapabilirsin!")
                    exit()
                elif nowtime >= 22 and nowtime <= 24:
                    print("iyi geceler",x,"giriş yapabilirsin!")
                    exit()
            else:
                print("Yüz tanınamadı! =>",x)

        #cv2.imshow("Elon Musk",test1)
        #cv2.imshow("Elon",test2)
        #cv2.waitKey(5000)
    except IndexError:
        print("Lütfen tekrar deneyiniz!")