# import the modules
import os
import time
import shutil
from os import listdir
from pathlib import Path
 
def checkImgDate():

    p = Path(input("Enter file path: "))
    i = 0
    if p.exists():
        print('OK....')
        for images in os.listdir(p):
            bypass = 0
            # check if the image ends with Iphone image file extension
            if (images.endswith(".png") or images.endswith(".jpg")\
                or images.endswith(".jpeg") or images.endswith(".JPG") or images.endswith(".JPEG") or images.endswith(".MOV") or images.endswith(".PNG")):

                # record pictures absolute path in variable
                pimg = str(p) + '/' + str(images)
                
                ##### Reading the stamp using YYYY__MM format
                #ti_c = os.path.getctime(pimg)
                ti_m = os.path.getmtime(pimg)
                #c_ti = time.ctime(ti_c)
                m_ti = time.ctime(ti_m)
                #print(c_ti)
                #t_obj = time.strptime(c_ti)
                t_obj = time.strptime(m_ti)
                T_stamp = time.strftime("%Y__%m", t_obj)
                
                # Loop through current directory to enumerate
                for root, dirs, files in os.walk(p, topdown=False):
                    for name in dirs:
                        # check if folder is existing, then move file
                        if str(T_stamp) == str(name):
                            npimg = os.path.join(root, T_stamp) + '/' + images
                            #move file
                            dest = shutil.move(pimg, str(npimg))
                            print(name + " : " + images)
                            bypass = 1
                #if folder doesn't exist then create and move file
                if bypass == 0:
                    newfold = os.path.join(root, T_stamp)        
                    npimg = newfold + '/' + images
                    #create relevant folder
                    os.mkdir(newfold)
                    print(T_stamp + " has been created...")
                    #move file
                    dest = shutil.move(pimg, str(npimg))
                    print(T_stamp + " : " + images)
                i = i + 1

        print(str(i) + ' image files have been processed')
    else:

        print('This directory does not exist...')

if __name__ == "__main__":
	checkImgDate()

