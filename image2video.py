
import cv2
import numpy as np
import glob
 

class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

def write_iter(img,index):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(index),(100,100), font, 4,(0,255,0),2,cv2.LINE_AA)
    return img

img_array = []

for index,filename in enumerate(sorted(glob.glob('*[0-9].png'))):
    x=MyImage(filename)
    print(str(x))
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    write_iter(img, index)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)
# out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'X264'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


# #  rename -e 's/\d+/sprintf("%03d",$&)/e' -- *.png




# import cv2
# import numpy as np
# import glob
# from matplotlib import pyplot as plt 


# img=cv2.imread("my_result_at_iteration_599.png")
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,str(12),(100,100), font, 4,(0   ,255,0),2,cv2.LINE_AA)

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()