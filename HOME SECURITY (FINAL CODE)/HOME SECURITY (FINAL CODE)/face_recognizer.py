import cv2



import threading
import face_recognition
from compare import compare_face
from compare import G_value
from Pi4 import Light




counter = 0

#from Email_Module import readMail
from Email_Module import sendMail_SSL , readMail_SSL , Internet



#checking the internet connection before running
print("Checking internet connection......")
if Internet.connect() == True : 
  print("Device is connected with internet.....")
else : 
  print("Device has no internet connection......")
  exit(-1)


face_cascade_Path = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(face_cascade_Path)
font = cv2.FONT_HERSHEY_SIMPLEX


known_faces_list = []

temp = face_recognition.load_image_file('images/Users.1.1.jpg')
known_faces_list.append(face_recognition.face_encodings(temp)[0])
temp = face_recognition.load_image_file('images/Users.2.2.jpg')
known_faces_list.append(face_recognition.face_encodings(temp)[0])
print("Face encodings are done.....")

face_encodings =[]
counter = 0
reply=''
id = 0
# names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
names = ['JAKIE', 'RDJ'] # add a name into this list
#Video Capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
print("Camera has turned on Waiting for faces....")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_location = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_location)
    threading.Thread(target=compare_face.compare, args=(face_encodings , known_faces_list, names)).start()  

    # Here G_value is a global value present in compare package 
    if G_value.val == 1 : 
        print(names[G_value.index]+ " Detected")
        Light.detect()
        G_value.val = 0 
        G_value.index = -1
  
  
    elif G_value.val == 2 : 
       counter += 1
       
       cv2.imwrite("./temp_faces/Person" + str(counter) + ".jpg",img)
       offset =  sendMail_SSL.sendMail(counter)
       #for the read mail
       print('wait for the user to  reply')
       flag = 0
       
       while flag != 100 : 
           Light.hold()
           reply = readMail_SSL.readMail(offset)
           if reply == 'G' or reply == 'D' :
             break
           else : 
               flag += 1
       #further door lock code will be here  
       if reply == 'G' :   
        Light.detect()
        print(reply + " Unknown person you can enter the room!!")
        
        G_value.val = 0
       elif reply == 'D' : 
         print(reply + " User doesn't want you to enter!!!")
         Light.unknown()
         
         G_value.val = 0
       else : 
           Light.endTime()
           print(" Your time limit has expired!!!")
           G_value.val = 0

          
       reply = ''
       
      



      
    else : 
        print("No face detected!!")

            
            

       

    
    
    # Escape to exit the webcam / program
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
print("\n [INFO] Exiting Program.")

cam.release()
cv2.destroyAllWindows()
