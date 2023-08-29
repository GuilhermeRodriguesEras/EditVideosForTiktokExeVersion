from moviepy.editor import *
from moviepy.video.fx.all import crop
import os
import random

def CropForMe(video1,video2):

    video1_x1_val = video1.size[0] * 0.2
    video1_x2_val = video1.size[0] * 0.8

    edited_video1 = video1.fx(crop, x1 = video1_x1_val, x2 = video1_x2_val)

    video2_y1_val = video2.size[1]  * 0.4
    video2_y2_val = video2.size[1]  * 0.9

    edited_video2 = video2.fx(crop, y1 = video2_y1_val, y2= video2_y2_val)

    return edited_video1, edited_video2

def Combine(video1,video2):

    width, height = 1080, 1350 
    video1_with_new_size = video1.resize(newsize=(width, height))
    video2_with_new_size = video2.resize(newsize=(width, height))

    arrangement = [[video1_with_new_size], [video2_with_new_size.without_audio()]]

    return clips_array(arrangement)

def listaTempos(inicio_time:int,fim_time:int,tempo_cortes:int):
    run = True
    lista = [inicio_time]
    while run: 
        if inicio_time + tempo_cortes >= fim_time:
            lista.append(fim_time)
            run = False
        else:
            lista.append(inicio_time+tempo_cortes)
            inicio_time += tempo_cortes
        
    return lista

def listaDeVideosParaDistrair():
    lista_arquivos = os.listdir("distract videos")
    return lista_arquivos

def sorteioVideoRandom(lista):
    num = random.randint(0,len(lista)-1)
    return VideoFileClip(f"distract videos/{lista[num]}")

def MainAction(name,videoprincipal ,inicio_time, fim_time, tempo_cortes):

    tempos = listaTempos(inicio_time,fim_time, tempo_cortes)

    for i in range(len(tempos)-1):
        #inicio -> tempo[i] | fim -> tempo[i+1]
        start_time1, end_time1 = tempos[i], tempos[i+1]
        start_time2, end_time2 = 0, (end_time1 - start_time1)
        
        video1 = videoprincipal.subclip(start_time1, end_time1)

        distractvideo = sorteioVideoRandom(listaDeVideosParaDistrair())
        video2 = distractvideo.subclip(start_time2, end_time2)

        part1, part2 = CropForMe(video1,video2)

        combined_video = Combine(part1,part2)

        output_path = f"final videos/{name}-Parte-{i+1}.mp4"
        combined_video.write_videofile(output_path, codec="libx264")
