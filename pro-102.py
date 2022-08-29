import cv2
import dropbox
import time
import random 

startTime = time.time()
def takepic():
    num = random.randint(0,100)
    image  = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = image.read()
        imageName = "image"+str(num)+".jpg"
        cv2.imwrite(imageName,frame)
        result = False
    print("Image captured")
        
    image.released()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accesstoken = "sl.BNF9IAMtnZnKU1j-VTq4dhHpTtjH_0dldx_U8O-w_xk6PmnhkDWGUwnz_uq5QIZxAPGKzVs61n4Ao934CLBWKz3qDO71fckW8-SW34RAIDx9HcMLMyAh9RmIGNqdqk-_byOmG2mj0nf-"
    file = imageName
    filefrom = file
    fileto = "/newfolder/"+"imageName"
    dbx = dropbox.Dropbox(accesstoken)
    with open(filefrom,"rb") as f:
        dbx.files_upload(f.read(),fileto,mode  = dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
      while True:
          if((time.time()-startTime) >=5):

              images = takepic()
              uploadFile(images)
              
main()