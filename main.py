import sys
import os
dirpath =os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
import pygame
from pygame.locals import *
from sys import exit
import random
from random import randint
pygame.init()


#CRÉDITOS MÚSICA UTILIZADA: Nameless: The Hackers RPG Soundtrack, Album - BoxCat Games. Licença de uso Comum Creative, link de acesso para visualização da licença: https://creativecommons.org/licenses/by/3.0/legalcode
#obs: somente a música de fundo pode ser mp3, os demais arquivos de somprecisam ser wav
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('./data/BoxCat Games - Mission.mp3')
pygame.mixer.music.play(-1)

#CRÉDITOS SONS UTILIZADOS: THE MUSHROOM KINGDOM https://themushroomkingdom.net/media/smb/wav 
som_colisao = pygame.mixer.Sound('./data/smb_bump.wav')
som_colisao.set_volume(0.4)

som_gameOver = pygame.mixer.Sound('./data/smb_breakblock.wav')
som_gameOver.set_volume(0.4)

som_startGame = pygame.mixer.Sound('./data/smw2_key_get.wav')
som_startGame.set_volume(0.4)

#CRÉDITOS IMAGENS UTILIZADAS E MODIFICADAS: https://commons.wikimedia.org/wiki/File:Twemoji_1f40d.svg licença Creative Commons para uso. Link para acesso da licença https://creativecommons.org/licenses/by/4.0/
img = pygame.image.load('./data/snake2.png')
nova_img = pygame.transform.scale(img, (130,130))

img2 = pygame.image.load('./data/sad_snake2.png')
nova_img2 = pygame.transform.scale(img2, (220,240))

largura = 660
altura = 480
x_cobra = int(largura/2 - 50/2)//20*20
y_cobra = int(altura/2)//20*20

velocidade = 20
x_controle = velocidade
y_controle = 0

x_comida = randint(40, 600)//20*20
y_comida = randint(50, 430)//20*20
pontos = 0
fonte = pygame.font.SysFont('gadugi', 30, True, False)
#parâmetros fonte: qual a fonte, tamanho, negrito, itálico.
#pygame.font.get_fonts() trás a lista de fontes disponíveis


tela = pygame.display.set_mode ((largura, altura))

pygame.display.set_caption('Snake Game 🐍')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 3
game_over = False


#Função para desenhar o corpo da cobra recebendo como parâmetro os valores contidos na lista cobra, e pegando a posição dos elementos x e y da lista
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (255,255,255), (XeY[0], XeY[1], 20, 20))  
    
#Função reiniciar jogo, para ser chamada quando a tecla R for pressionada.
def restart_game():
    global limite, pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_comida,y_comida, game_over
    limite = pygame.draw.rect(tela, (255,0,0), pygame.Rect(20,40,620,420),2)
    pontos = 0
    comprimento_inicial = 3
    x_cobra = int(largura/2 - 50/2)//20*20
    y_cobra = int(altura/2)//20*20
    lista_cobra = []
    lista_cabeca = []
    x_comida = randint(40, 600)//20*20
    y_comida = randint(50, 430)//20*20
    game_over= False
    

def esperar_jogador():
    esperando = True
    while esperando:
        relogio.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                esperando = False
            if event.type == KEYDOWN:
                if event.key == K_s:
                    som_startGame.play()
                    esperando = False   

tela.fill((0,0,0))
mensagem_start1 = 'SNAKE GAME'
mensagem_start2 = f'Press [S] to Start'
mensagem_start3 = 'Developed by Beatriz Nascimento'
mensagem_start4 = f'1-   Use the UP, DOWN, LEFT and RIGHT arrows or the keys [W],[A],[S] and [D]' 
mensagem_start4_2 = f' on your keyboard to move the snake around the screen.'
mensagem_start5 = f'2-   Keep the snake inside the red border square. '
mensagem_start6 = f'3-   Eat the most yellow squares you can by step over them'
mensagem_start6_2 =f' but dont let the snake collide with herself during the process. ENJOY! :)'

fontestart1 = pygame.font.SysFont('gadugi', 50, True, False)
fontestart2 = pygame.font.SysFont('gadugi', 35, True, True)
fontestart3 = pygame.font.SysFont('gadugi', 15, True, True)
fontestart4 = pygame.font.SysFont('arial', 18, False, False)

texto_start1 = fontestart1.render(mensagem_start1, False, (227,235,136))
texto_start2 = fontestart2.render(mensagem_start2, False, (255,255,255))
texto_start3 = fontestart3.render(mensagem_start3, False, (255,255,255))
texto_start4 = fontestart4.render(mensagem_start4, False, (227,235,136))
texto_start4_2 = fontestart4.render(mensagem_start4_2, False, (227,235,136))
texto_start5 = fontestart4.render( mensagem_start5, False, (227,235,136))
texto_start6 = fontestart4.render(mensagem_start6, False, (227,235,136))
texto_start6_2 = fontestart4.render(mensagem_start6_2, False, (227,235,136))

ret_start1 = texto_start1.get_rect()
ret_start2 = texto_start2.get_rect()
ret_start3 = texto_start3.get_rect()
ret_start4 = texto_start4.get_rect()
ret_start4_2 = texto_start4_2.get_rect()
ret_start5 = texto_start5.get_rect()
ret_start6 = texto_start6.get_rect()
ret_start6_2 = texto_start6_2.get_rect()

ret_start1.center = (320,30)
tela.blit(texto_start1,ret_start1)
ret_start2.center = (320, 90)
tela.blit(texto_start2,ret_start2)
ret_start3.center = (320, 400)
tela.blit(texto_start3,ret_start3)
ret_start4.center = (320, 200)
tela.blit(texto_start4,ret_start4)
ret_start4_2.center = (320, 220)
tela.blit(texto_start4_2,ret_start4_2)
ret_start5.center = (320, 260)
tela.blit(texto_start5,ret_start5)
ret_start6.center = (320, 300)
tela.blit(texto_start6,ret_start6)
ret_start6_2.center = (320, 320)
tela.blit(texto_start6_2,ret_start6_2)

tela.blit(nova_img, (500,20))

pygame.display.update()
esperar_jogador()


while True:
    relogio.tick(5+(pontos*0.2))
    tela.fill((0,0,0))
    limite = pygame.draw.rect(tela, (255,0,0), pygame.Rect(20,40,620,420),2)
    mensagem = f'Score: {pontos}'
    texto_formatado1 = fonte.render(mensagem, False, (227,235,136))
    #Parâmetros do texto formatado: texto da mensagem, pixelado ou não, cor
    while game_over:
        fonte2 = pygame.font.SysFont('arial',45, True, False)
        fonte3 = pygame.font.SysFont('arial',40, False, False)
        fonte4 = pygame.font.SysFont('arial',30, True, True)
        mensagem2 = f'GAME OVER! :( '
        mensagem3 = f'Your score: {pontos}'
        mensagem4 = 'Press [R] to restart.'
        texto_formatado2 = fonte2.render(mensagem2, False, (255,255,255))
        texto_formatado3 = fonte3.render(mensagem3, False, (232,225,13))
        texto_formatado4 = fonte4.render(mensagem4, False, (255,255,255))

        ret_texto2 = texto_formatado2.get_rect()
        ret_texto3 = texto_formatado3.get_rect()
        ret_texto4 = texto_formatado4.get_rect()
        tela.fill((244,22,22))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    som_startGame.play()
                    restart_game()

        ret_texto2.center = (320, 80)
        tela.blit(texto_formatado2,ret_texto2)
        ret_texto3.center = (320, altura//3)
        tela.blit(texto_formatado3,ret_texto3)
        ret_texto4.center = (320, altura//2)
        tela.blit(texto_formatado4,ret_texto4)

        tela.blit(nova_img2, (410,230))
        pygame.display.update()

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

#Coordenada de movimentos (constante, alterando a direção) a partir do teclado:
#AWSD e setas direcionais
#bug/feature - Necessário rever lógica com uma validação para as direções, cobra colide consigo mesma se as teclas direcionais são apertadas muito rapido em algumas situações.
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade: 
                   pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0


#Coordenada de movimentos,movimentando-se 20 cada vez que a tecla for pressionada(não está sendo utilizado)
        '''if pygame.key.get_pressed()[K_a]:
            x_cobra = x_cobra - 20
        if pygame.key.get_pressed()[K_d]:
            x_cobra = x_cobra + 20
        if pygame.key.get_pressed()[K_w]:
            y_cobra = y_cobra - 20
        if pygame.key.get_pressed()[K_s]:
            y_cobra = y_cobra + 20'''

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(255,255,255), (x_cobra,y_cobra,20,20))
    comida  = pygame.draw.rect(tela,(241,255,74), (x_comida,y_comida,20,20))


    lista_comida =[x_comida,y_comida]

    if cobra.colliderect(comida):
        x_comida = randint(40, 600)//20*20
        y_comida = randint(50, 430)//20*20
        pontos = pontos + 1
        som_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

#Comando para dar fim de jogo quando a cobra colidir com a delimitação vermelha na tela

    if x_cobra + comprimento_inicial> 640:
        som_gameOver.play()
        game_over = True
    if x_cobra + comprimento_inicial < 20:
        som_gameOver.play()
        game_over = True
    if y_cobra + comprimento_inicial < 40:
        som_gameOver.play()
        game_over = True
    if y_cobra +comprimento_inicial > 460:
        som_gameOver.play()
        game_over = True

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    #while lista_comida.count(lista_cobra):
        #comida = pygame.draw.rect(tela,(241,255,74), (x_comida,y_comida,20,20))

    #else:

#Comando para dar fim de jogo quando a cobra colidir com ela mesma.

    if lista_cobra.count(lista_cabeca) > 1:
        som_gameOver.play()
        game_over = True
                    
        
#Comando para a cobra não colidir com a tela e atravessar (não está sendo utilizado, apenas para aprendizado e anotação)
    '''if x_cobra + comprimento_inicial> largura:
    #x_cobra = 0
    #if x_cobra + comprimento_inicial < 0:
        #x_cobra = largura-comprimento_inicial
    #if y_cobra + comprimento_inicial < 0:
        #y_cobra = altura-comprimento_inicial
    #if y_cobra + comprimento_inicial > altura:
        #y_cobra = 0'''

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

#Coordenada para objeto se manter em movimento constante de acordo com a condicional        
        #if y >= altura:
            #y = 0
        #y = y + 5
        #pygame.draw.circle(tela,(0,0,255), (300,260),40)
        #pygame.draw.line(tela,(255,255,0), (390,0), (390, 600),5)

    tela.blit(texto_formatado1,(280,0))
    pygame.display.update()
        
       

    
