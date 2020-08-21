import os
from cv2 import cv2

mainFolder = 'Images'
myFolders = os.listdir(mainFolder)
print(f'Count of folders:- {myFolders}')
for folder in myFolders:
    path = mainFolder +'/' + folder
    # print(f'Name of folders:- {path}')
    images = []
    myList = os.listdir(path)
    print(f'Total images inside folders:- {len(myList)}.')
    for image_number in myList:
        current_image = cv2.imread(f'{path}/{image_number}')
        current_image = cv2.resize(current_image, (0, 0), None, 0.2, 0.2)
        images.append(current_image)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated.')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('Panorama Not Generated.') 
cv2.waitKey(0)