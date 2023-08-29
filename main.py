from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import mainfunction
from CropAndCombine import MainAction

i = 0
run = True

while run:
    os.system('cls')

    #get video file to work
    if i == 0:
        print("Digite o nome do arquivo do video a ser particionado (tem que ser .mp4)")
        nome_file = input()
        try:
            videoPrincipal = VideoFileClip("undited videos/"+nome_file+".mp4")
            i += 1
            os.system('cls')
        except:
            print("Arquivo não Encontrado :-:. É necessário somente o nome sem o (.mp4)")
            print("")
            input()
            os.system('cls')
    
    # get time videos
    if i == 1:
        print("Digite [1] para criar partes do video inteiro.")
        print("       [2] para criar partes de somente um trecho.")
        choice = input()
        if choice == "1":
            inicio_time = 1
            fim_time = ((videoPrincipal.duration) // 1) -1
            i += 1
        elif choice == "2":
            os.system('cls')
            print("Digite o tempo que você deseja que começe o video: (exemplo -> 2:30)")
            entrada = input()
            if mainfunction.verificaEntradaDeTempo(entrada):
                inicio_time = mainfunction.transformeTempo(entrada)
                print("Digite o tempo que você deseja que termine o video: (exemplo -> 2:30)")
                entrada = input()
                if mainfunction.verificaEntradaDeTempo(entrada):
                    fim_time = mainfunction.transformeTempo(entrada)
                    if inicio_time >= fim_time:
                        print("O tempo inicial tem que ser maior que o final.")
                        input()
                    else:
                        i += 1
                else:
                    print("Tempo digitado Invalido.")
                    input()
            else:
                print("Tempo digitado Invalido.")
                input()

        else:
            print("Opção invalida.")
            input()
            os.system('cls')
        
    if i == 2: 
        os.system('cls')
        print("Digite qual o tempo que cada parte deverá ter de duração (exemplos -> [1:30] ou [0:45])")
        
        entrada = input()
        if mainfunction.verificaEntradaDeTempo(entrada):
            tempo_cortes = mainfunction.transformeTempo(entrada)
            MainAction(nome_file,videoPrincipal,inicio_time,fim_time,tempo_cortes)

            run = False
        else:
            print("Tempo digitado Invalido.")
            input()
            os.system('cls')

        
        