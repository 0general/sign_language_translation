import os
import cv2
from glob import glob
import pandas as pd

# 경로 지정
t_path = "/content/drive/MyDrive/wandavision/7965/home/storage/train_set.csv" # train set 경로
v_path = "/content/drive/MyDrive/wandavision/7965/home/storage/val_set.csv" 

t_df = pd.read_csv(t_path)
v_df = pd.read_csv(v_path)

# 저장 경로
save_path = "/content/drive/MyDrive/wandavision/7965/home/storage/sen"
file_path = "/content/drive/MyDrive/wandavision/7965/sign_language/rawdata"


for df in [t_df,v_df]:
    for i in range(df.shape[0]):
        x = df.iloc[i]['Filename']
        video_path = os.path.join(file_path,x+'.mp4')

        save = os.path.join(save_path,x)
        try:
            if not os.path.exists(save):
                os.makedirs(save)
        except OSError:
            print("Error: Creating directory. "+x)

        video = cv2.VideoCapture(video_path)

        if not video.isOpened():
            print("Could not Open :", video_path)
            exit(0)
        
        # 초당 프레임 단위 확인
        fps = video.get(cv2.CAP_PROP_FPS)
        # x = fps//2 # 초당 2개씩
        x = fps

        count = 0
        while(video.isOpened()):
            ret, image = video.read()
            if not ret:
                break
            if int(video.get(1)) == 0: 
                continue
            if (int(video.get(1)) % x == 0): # x 프레임당 한 장씩 뽑아라
                frame = f'{count:03}'+'.jpg'
                p = os.path.join(save,x+frame) # 이 이미지를 저장할 경로 지정
                cv2.imwrite(p,image)
                # cv2_imshow(image) # 이미지 확인
                count += 1
        video.release()
        