# !pip install urllib
# !pip install opencv-python

from urllib import parse
import requests
from PIL import Image
import cv2
import numpy as np
import pygame
import os
import random
import shutil
from SpeechToText import *
import pandas as pd


def showImg(img_path, img_path2):
    '''
    https://github.com/saleh1312/python/blob/master/image%20morphing
    1- 2 images must have the same size .
    2- we get the coordianates of the left and right eyes and mouse 
    of 2 images
    '''

    #read image
    img = cv2.imread(img_path)
    img2 = cv2.imread(img_path2)
 
    # img = cv2.resize(img, (3072, 1920), interpolation=cv2.INTER_CUBIC)
    # img2 = cv2.resize(img2, (3072, 1920), interpolation=cv2.INTER_CUBIC)
    img = cv2.resize(img, (3600, 2060), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (3600, 2060), interpolation=cv2.INTER_CUBIC)
 
    #lift , right eyes and mouse 
    pts1 = np.array([[218, 240],[295, 240],[250, 383]],np.float32)
    pts2 = np.array([[248, 245],[345, 270],[281, 366]],np.float32)
    pts11 =np.zeros((3,2),np.float32)
    pts22 =np.zeros((3,2),np.float32)

    dis = 100.0 # iterations 
    piece = 1.0 / dis

    for i in range(0,int(dis)):
        for j in range(0,3):
            disx = (pts1[j,0] - pts2[j,0])*-1
            disy = (pts1[j,1] - pts2[j,1])*-1
            
            #move of first imageå
            movex1 =( disx/dis) * (i+1)
            movey1 =( disy/dis) * (i+1)
            
            #move of second image
            movex2 =disx-movex1
            movey2 =disy-movey1
            
            pts11[j,0] = pts1[j,0] + movex1
            pts11[j,1] = pts1[j,1] + movey1
            
            pts22[j,0] = pts2[j,0] - movex2
            pts22[j,1] = pts2[j,1] - movey2
            
        
        mat1=cv2.getAffineTransform(pts1, pts11)
        mat2=cv2.getAffineTransform(pts2, pts22)
        
        dst1=cv2.warpAffine(img, mat1, (img.shape[1],img.shape[0]),None,None,cv2.BORDER_REPLICATE)
        dst2=cv2.warpAffine(img2, mat2, (img.shape[1],img.shape[0]),None,None,cv2.BORDER_REPLICATE)
        
        dst=cv2.addWeighted(dst1, 1-(piece*(i)), dst2, piece*(i+1), 0)

        cv2.namedWindow("Tensor Therapy", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Tensor Therapy", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("dst", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("Tensor Therapy",dst)
        cv2.waitKey(25)

#init
##Intro
intro_path = './intro.jpg'
previouse_path = './pre.png'
showing_path = './show.png'
showImg(intro_path,intro_path)
shutil.copy(intro_path,showing_path)
sd_url = "http://127.0.0.1:5000/txt2img"
kb_url = "http://a7b0-34-87-180-203.ngrok.io/sentiment"
headers = {
    "Content-Type": "application/json"
}

pygame.mixer.init()
myDeltaSound = pygame.mixer.Sound('music/델타파.mp3')
myDeltaSound.set_volume(0.15)
myDeltaSound.play(-1)
mySound = pygame.mixer.Sound('music/05/Prelude No. 5 - Chris Zabriskie.mp3')
mySound.play(-1)

#음성인식이 안될경우 감정데이터셋의 대화를 랜덤으로 가져온다.
comset = pd.read_csv('감정대화셋.csv')
comset = comset['talk'].to_list()
stt = SpeechToText()


#STT -> 감정분석 -> 이미지 생성 -> 음악재생 - 반복
while True:
    # 1. STT
    stt_text = stt.speech2txt(10)
    if stt_text == "":
        stt_text = comset[random.randint(0,len(comset)-1)]
        # stt_text = "나는 너무 행복해"
        # stt_text = "나는 너무 우울해"
    #stt_text = "오늘 하루 어땠니? 너무 힘들었어 나도 그래 어쩜 이렇게 힘들지 뭐야 이런거야 계속 이렇게 힘들어지면 어떡하지 슬프다 포기할까봐 에이 그래도 큰맘먹고 시작한건데 끝까지 해봐야지"
    # stt_text = "나약했습니다. 이것 역시, 의지의 문제라고, 내게 이러한 병을 안겨준 인간의 기질과도 같은, 그러한 것이라고. 나는 어딘가 휩쓸려 살아갈 수 밖에 없는, 그러한 기질의 인간으로 태어난 것이라고. 그 흔한, 일탈이라고 부르는 것 조차 시도하지 못하는, 순진무구하게 큰, 커다란 우리 안의 보호받은 동물과 같은 존재라고- 그런 생각을 가지게 되었습니다. 그러한 기질마저, 나의 우울로 지워져가고 있을 때 쯤, 비로소 주변인들의 도움으로 정신과를 가게 되었습니다. 그저, 우울, 이라고 불리우는 것을 치료하기 위해, 상담을 받고, 각종 치료를 받으며, 약을 처방받고 그것을 삼킵니다. 괴롭습니다. 나중에 알게 된 것이지만, 제가 처방받은 약에는, 만 25세 이하의 사람에게는- 충동적인 자살충동을 유발한다는, 비공식적인 연구결과가 있더군요. 속설이라 불리우는 것이지만, 그 약을 투여하고 자살한 남자의 애인이, 그러한 내용을 바탕으로 병원과의 법정싸움에서 승소했다는 이야기도 있었습니다"
    print(stt_text)

    # 2. 감정분석
    data = parse.quote(stt_text)
    response = requests.get(kb_url+"?txt="+data, headers=headers)
    res_text = response.text
    if res_text.find("500 Internal Server Error")>-1:
        continue
    print(res_text)
    # res_text = "00|Draw a yellow tone monk who talks on the platform in a portrait style"
    emotion = res_text.split("|")


    # 3. 이미지 생성
    # get text2image
    data = parse.quote(emotion[1])
    response = requests.get(sd_url+"?txt="+data, headers=headers)
    image_path = response.text
    if image_path.find("500 Internal Server Error")>-1:
        continue
    os.rename(showing_path,previouse_path)
    os.rename(image_path,showing_path)
    showImg(previouse_path,showing_path)


    # 4. 음악재생
    list_Files = []
    for (root, directories, files) in os.walk("./music/"+emotion[0]):
        for file in files:
            file_path = os.path.join(root, file)
            if len(file_path)> 4 and (file_path[-4:].lower().find(".wav")>-1 or file_path[-4:].lower().find(".mp3")>-1) : 
                list_Files.append(file_path)
    music_path = list_Files[random.randint(0,len(list_Files)-1)]
    print("music_path : ",music_path)
    
    mySound.fadeout(3000)
    mySound.stop()
    mySound = pygame.mixer.Sound(music_path)
    mySound.play(-1)
    
    
    # key interrupt signal
    try:
        pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break


# cv2.waitKey(0)
cv2.destroyAllWindows()

mySound.fadeout(3000)
mySound.stop()
myDeltaSound.fadeout(3000)
myDeltaSound.stop()
# pygame.mixer.music.fadeout(3000)
# pygame.mixer.music.stop()
# pygame.mixer.music.unload()
# pygame.mixer.music.quit()