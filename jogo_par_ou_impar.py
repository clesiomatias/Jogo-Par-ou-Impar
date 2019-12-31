 # -*- coding: utf-8 -*- 
'''Jogo clássico que resolve todas as pendengas da molecada
 desde muitos anos atrás. Baseado no pseudocódigo distribuido 
 em grupos do Facebook pelo Professor Mário Leite'''
 
#Escopo de importações
from turtle import *
from time import sleep
from random import randint

#Escopo de variáveis globais
jogada = 1
acertos1,acertos2,num,res = 0,0,0,0
#aqui separo cada jogador em dois (duas mãos)
jog1_dir,jog1_esq = 0,0
jog2_dir,jog2_esq = 0,0
resp ='s'
resultado, esc1,esc2 = '','',''

# criando janela
def janela():
	global jogada,acertos1,acertos2
	#define o objeto janela
	janela = Screen()
	#limpa qualquer instancia dele
	janela.clear()
	janela.setup(600,400,0,0)
	janela.title('Jogo Par ou Impar by Mário Leite')
	janela.bgcolor('blue')
	#dividindo a tela
	linha = Turtle()
	linha.speed(0)
	linha.ht()
	linha.pu()
	linha.setpos(-150,300)
	linha.pd()
	linha.width(7)
	linha.color('yellow')
	linha.goto(-150,-300)
	linha.pu()
	linha.setpos(150,-300)
	linha.pd()
	linha.goto(150,300)
	linha.pu()
	linha.setpos(150,0)
	linha.pd()
	linha.goto(50,0)
	linha.pu()
	linha.setpos(-50,0)
	linha.pd()
	linha.goto(-150,0)
	#escrevendo o hud
	#----jogador 1
	j1= Turtle()
	j1.ht()
	j1.pu()
	j1.color('white')
	j1.setpos(-280,140)
	j1.write(f'Jogador 1\nAcertos: {acertos1}',font = ("Arial",18,'normal'))
	
	#----jogador 2
	j2= Turtle()
	j2.ht()
	j2.pu()
	j2.color('white')
	j2.setpos(170,-190)
	j2.write(f'Jogador 2\nAcertos: {acertos2}',font = ("Arial",18,'normal'))
	#--- escrevendo a jogada
	jogadas= Turtle()
	jogadas.ht()
	jogadas.pu()
	jogadas.color('yellow')
	jogadas.setpos(-50,170)
	jogadas.write(f'Jogada: {jogada}',font = ("Arial",18,'normal'))
	

#registrando todas as imagens
img = ['d10.gif','d11.gif','d12.gif','d13.gif','d14.gif','d15.gif',
		'e10.gif','e11.gif','e12.gif','e13.gif','e14.gif','e15.gif',
		'd10 - Cópia.gif','d11 - Cópia.gif','d12 - Cópia.gif','d13 - Cópia.gif','d14 - Cópia.gif','d15 - Cópia.gif',
		'e10 - Cópia.gif','e11 - Cópia.gif','e12 - Cópia.gif','e13 - Cópia.gif','e14 - Cópia.gif','e15 - Cópia.gif',]
for i in img:
	register_shape(i)

#função que desenha as mãos do jog1
def mao_jog1(j):
	'''a função recebe uma tupla com dois valores sorteados ,
	um para cada mão,em seguida os desenha segundo a quantidade 
	de "dedos" a mostrar'''
	
	#mão esquerda
	#--definindo imagem
	if j[1]== 0:
		e =img[18]
	elif j[1]== 1:
		e =img[19]
	elif j[1]== 2:
		e =img[20]
	elif j[1]== 3:
		e =img[21]
	elif j[1]== 4:
		e =img[22]
	elif j[1]== 5:
		e =img[23]
	#desenhando a mão
	me = Turtle()
	me.speed(0)
	me.pu()
	me.setpos(70,150)
	me.shape(e)
	#escrevendo o numero 
	met = Turtle()
	met.speed(0)
	met.pu()
	met.ht()
	met.color('red')
	met.setpos(70,90)
	met.write(f'{j[1]}', font=('Arial',24,'normal'))
	
	#mão direita
	#--definindo imagem
	if j[0]== 0:
		d =img[12]
	elif j[0]== 1:
		d =img[13]
	elif j[0]== 2:
		d =img[14]
	elif j[0]== 3:
		d =img[15]
	elif j[0]== 4:
		d =img[16]
	elif j[0]== 5:
		d =img[17]
	#desenhando a mão
	md = Turtle()
	md.speed(0)
	md.pu()
	md.setpos(-70,150)
	md.shape(d)
	#escrevendo o numero 
	mdt = Turtle()
	mdt.speed(0)
	mdt.pu()
	mdt.ht()
	mdt.color('red')
	mdt.setpos(-70,90)
	mdt.write(f'{j[0]}', font=('Arial',24,'normal'))
	
	
#função que desenha sa mãos do jogador 2	
def mao_jog2(j):
	'''a função recebe uma tupla com dois valores sorteados ,
	um para cada mão,em seguida os desenha segundo a quantidade 
	de "dedos" a mostrar'''
	
	#mão esquerda
	#--definindo imagem
	if j[1]== 0:
		e =img[6]
	elif j[1]== 1:
		e =img[7]
	elif j[1]== 2:
		e =img[8]
	elif j[1]== 3:
		e =img[9]
	elif j[1]== 4:
		e =img[10]
	elif j[1]== 5:
		e =img[11]
	#desenhando a mão
	me = Turtle()
	me.speed(0)
	me.pu()
	me.setpos(70,-150)
	me.shape(e)
	#escrevendo o numero 
	met = Turtle()
	met.speed(0)
	met.pu()
	met.ht()
	met.color('red')
	met.setpos(70,-90)
	met.write(f'{j[1]}', font=('Arial',24,'normal'))
	
	#mão direita
	#--definindo imagem
	if j[0]== 0:
		d =img[0]
	elif j[0]== 1:
		d =img[1]
	elif j[0]== 2:
		d =img[2]
	elif j[0]== 3:
		d =img[3]
	elif j[0]== 4:
		d =img[4]
	elif j[0]== 5:
		d =img[5]
	#desenhando a mão
	md = Turtle()
	md.speed(0)
	md.pu()
	md.setpos(-70,-150)
	md.shape(d)
	#escrevendo o numero 
	mdt = Turtle()
	mdt.speed(0)
	mdt.pu()
	mdt.ht()
	mdt.color('red')
	mdt.setpos(-70,-90)
	mdt.write(f'{j[0]}', font=('Arial',24,'normal'))	


#função do sorteia jogada recebe qual jogador está jogando
def sorteia_jogada(j):
	global jog1_dir, jog1_esq,jog2_dir,jog2_esq
	d = randint(0,5)
	e = randint(0,5)
	if j == 1:
		jog1_dir = d
		jog1_esq = e
	else:
		jog2_dir = d
		jog2_esq = e
	return d,e
		
#chamando janela


#loop do jogo
while True:
	janela()
	
	#sorteando um numero aleatório para definir a escolha
	num = randint(0,1000)
	if num%2==0:
		esc1 = 'PAR'
		esc2 = 'IMPAR'
	else:
		esc1 = 'IMPAR'
		esc2 = 'PAR'
	#Escrevendo as escolhas na HUD
	escolha1= Turtle()
	escolha1.ht()
	escolha1.pu()
	escolha1.color('#39ff14')
	escolha1.setpos(-280,40)
	escolha1.write(f'Escolheu:\n{esc1}',font = ("Arial",18,'normal'))
	#----
	escolha2= Turtle()
	escolha2.ht()
	escolha2.pu()
	escolha2.color('#39ff14')
	escolha2.setpos(170,40)
	escolha2.write(f'Escolheu:\n{esc2}',font = ("Arial",18,'normal'))
	
	#pausa dramática :)
	sleep(1.5)
	
	#sorteando e "mostrando as mãos"
	mao_jog1(sorteia_jogada(1))
	mao_jog2(sorteia_jogada(2))
	
	#mais uma pausa dramática :):)
	sleep(0.5)
	
	#mostra resultado
	res = (jog1_dir + jog1_esq) + (jog2_dir + jog2_esq)
	rres= Turtle()
	rres.ht()
	rres.pu()
	rres.color('#ff3300')
	rres.setpos(-40,-10)
	rres.write(f'Resultado:\n      {res}',font = ("Arial",14,'normal'))
	
	#define e mostra o vencedor
	if res%2==0:
		if esc1 == 'PAR':
			acertos1+=1
			ganhou= Turtle()
			ganhou.ht()
			ganhou.pu()
			ganhou.color('white')
			ganhou.setpos(-280,-10)
			ganhou.write(f'Deu {esc1}\nJogador 1 Venceu!',font = ("Arial",18,'normal'))
		else:
			acertos2+=1
			ganhou= Turtle()
			ganhou.ht()
			ganhou.pu()
			ganhou.color('white')
			ganhou.setpos(170,-10)
			ganhou.write(f'Deu {esc2}\nJogador 2 Venceu!',font = ("Arial",18,'normal'))
	else:
		if esc1 == 'IMPAR':
			acertos1+=1
			ganhou= Turtle()
			ganhou.ht()
			ganhou.pu()
			ganhou.color('white')
			ganhou.setpos(-280,-100)
			ganhou.write(f'Deu {esc1}\nJogador 1 \nVenceu!',font = ("Arial",18,'normal'))
		else:
			acertos2+=1
			ganhou= Turtle()
			ganhou.ht()
			ganhou.pu()
			ganhou.color('white')
			ganhou.setpos(170,-100)
			ganhou.write(f'Deu {esc2}\nJogador 2 \nVenceu!',font = ("Arial",18,'normal'))
	
	
	#limpando a janela e dando escolha de jogar novamente
	resp = textinput('Jogar novamente? ','[S,N]').upper()
	
	#== conferindo se foi digitado uma escolha valida
	while True:
		if resp in 'SN':
			break
		else:
			resp = textinput('Jogar novamente? ','[S,N]').upper()
	
	#continuando segundo  a resposta
	if resp == 'S':
		jogada+=1	
		continue
	else:
		estatisticas_tela = Turtle()
		estatisticas_tela.color('white')
		estatisticas_tela.shape('square')
		estatisticas_tela.shapesize(50)
		estatisticas= Turtle()
		estatisticas.ht()		
		estatisticas.pu()
		estatisticas.setpos(-250,0)
		estatisticas.write(f'ESTATÍSTICAS DO JOGO\nACERTOS JOGADOR 1 : {acertos1} - TOTAL: {(acertos1/jogada*100):.2f}%\nACERTOS JOGADOR 2: {acertos2} - TOTAL: {(acertos2/jogada*100):.2f}%',font = ("Arial",18,'normal'))
		break	
	
mainloop()

