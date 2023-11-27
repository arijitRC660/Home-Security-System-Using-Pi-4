import face_recognition
import numpy as np
from compare import G_value

#method that will compare faces
def compare(face_encodings , known_faces_list, names) :
    index = 0
    name = ""
    for face_encodings in face_encodings:
            matches = face_recognition.compare_faces(known_faces_list, face_encodings)
            face_distance = face_recognition.face_distance(known_faces_list, face_encodings)
            index = np.argmin(face_distance)
            if matches[index]:
                name = names[index]

                
                G_value.val = 1
                G_value.index = index

            else : 
                
                G_value.val = 2



    
