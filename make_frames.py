import os
import cv2
from glob import glob
# import numpy as np

# name_arr = ['119','가슴','경찰','고열','부러지다','구급차','구해주세요','남편',\
#     '누이','동생','딸','쓰러지다','머리','배','보내주세요','손',\
#     '숨을 안 쉬다','신고하세요','아기','아내','아들','아빠','엄마','임산부',\
#     '자상','절단','집','출산','출혈','할머니','할아버지','화상']

# 저장 경로
path = r"D:\wandavision_data"


for file_path in glob(os.path.join(path,"*")):
    # print(file_path)
    for video_file in glob(os.path.join(file_path,"*.mp4")):
        name = video_file[-22:-4]
        video = cv2.VideoCapture(video_file)
        # print(video_file)


        if not video.isOpened():
            print("Could not Open :", video_file)
            exit(0)
        
        # 초당 프레임 단위 확인
        # fps = video.get(cv2.CAP_PROP_FPS)
        # x = fps//2 # 초당 2개씩

        count = 0
        while(video.isOpened()):
            ret, image = video.read()
            if not ret:
                break
            if (int(video.get(1)) % 3 == 0): # x 프레임당 한 장씩 뽑아라
                frame = f'_{count:03}'+'.jpg'
                p = os.path.join(file_path,name+frame) # 이 이미지를 저장할 경로 지정
                cv2.imwrite(p,image)
                print(p)
                count += 1 
                # cv_img = cv2.imread(p)
                # cv2.imshow('frame image', cv_img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()

        video.release()
        