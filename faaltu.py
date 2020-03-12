#from werkzeug.datastructures import FileStorage

#fi = FileStorage(filename='car.jpg',stream = open('cars.jpg','rb'))
#            
#print(fi.filename)
#
#print(fi.stream)
#
#import base64
#
#with open("foo.png", "rb") as img_file:
#    image_str = base64.encodebytes(img_file.read())
#    
#print(image_str.decode())
#print(type(image_str))

#print(type(image_str))
#with open('f',"wb") as f:
#    f.write(base64.decodebytes(image_str))
    
#print(my_string.decode())
#image_str=image_str.decode()
#print(type(image_str))  
#
#print(type(image_str.encode()))
#
#with open('f',"wb") as f:
#    f.write(base64.b64decode(image_str.encode()))


import requests
import os

response=requests.get('https://i.ytimg.com/vi/yqQu7eudl2s/maxresdefault.jpg')
#print(response.content)

#file = os.path.join(app.config['UPLOAD_FOLDER'], filename)

with open("image.jpg","wb") as f:
    f.write(response.content) 
