from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import time


janela = Tk()

janela.title("Caixa Automático ")
janela.geometry('705x370')
janela.configure(bg='green') #background (fundo)
janela.resizable(True,True) # Responsividade
janela.maxsize(width=705,height=370)
janela.minsize(width=705,height=370)

#Variaveis Globais
saldoAtual = 5000
saqueTotal= 0
saque_pagar = True
deposito_celular = True

#Função saldo
def saldo():
    conclusao['text']=f' Seu saldo  R$ {saldoAtual}'
    janela.update()
    time.sleep(2)
    normalizar()

def saque():
    global saque_pagar
    conclusao['text'] = 'Quanto deseja sacar?'
    saque_pagar = True
    botoesValores()

def botoesValores():
    botao1['text']= '10'
    botao1 ['command']= saque10
    botao2['text']='20'
    botao2['command']= saque20
    botao3['text'] = '40'
    botao2['command'] = saque40
    botao4['text'] = '50'
    botao4['command'] = saque50
    botao5['text'] = '100'
    botao5['command'] = saque100
    botao6['text'] = 'Confirmar'
    botao6['command'] = ConfirmarSaque
    janela.update()

#As 5 Funções de saque
def saque10():
    global saqueTotal
    saqueTotal +=10
    conclusao['text'] = f'Valor R${saqueTotal}'
    janela.update()

def saque20():
    global saqueTotal
    saqueTotal +=20
    conclusao['text'] = f'Valor  R${saqueTotal}'
    janela.update()

def saque40():
    global saqueTotal
    saqueTotal +=40
    conclusao['text'] = f'Valor R${saqueTotal}'
    janela.update()

def saque50():
    global saqueTotal
    saqueTotal +=50
    conclusao['text'] = f'Valor  R${saqueTotal}'
    janela.update()

def saque100():
    global saqueTotal
    saqueTotal +=100
    conclusao['text'] = f'Valor do saque R${saqueTotal}'
    janela.update()

def saque1000():
    global saqueTotal
    saqueTotal +=1000
    conclusao['text'] = f'Valor do saque R${saqueTotal}'
    janela.update()

#Vamos criar uma condição para comparar os valores manipulados
def ConfirmarSaque():
    global saqueTotal, saldoAtual, saque_pagar #chamamos as variáveis globais
    if saqueTotal > saldoAtual:
        conclusao['text']='Saque insuficiente \U0001F613!'
        saqueTotal=0
    else:
        saldoAtual -= saqueTotal
        if saque_pagar:
            conclusao ['text']=f'Saque de  R$ {saqueTotal} concluido com sucesso \U0001F911!'
        else:
            conclusao['text'] = f'Pagamento de  R$ {saqueTotal} concluido com sucesso \U0001F911!'
        saqueTotal=0
    janela.update()
    time.sleep(2)
    normalizar()

def normalizar():
    conclusao['text']='Deseja realizar alguma operação?'
    botao1['text'] = 'Saldo'
    botao1['command'] =saldo
    botao2['text'] = 'Saque'
    botao2['command'] = saque
    botao3['text'] = 'Depósito'
    botao2['command'] = deposito
    botao4['text'] = 'Pagar Conta'
    botao4['command'] = pagar
    botao5['text'] = 'Desb.Celular'
    botao5['command'] = desbloquear
    botao6['text'] = 'Sair'
    botao6['command'] = sair
    janela.update()

def pagar():
    global saque_pagar
    conclusao['text'] = 'Qual valor do pagamento?'
    saque_pagar = False
    botoesValores()

caixa = None
def deposito():
    global deposito_celular, caixa
    if deposito_celular:
        conclusao['text'] = 'Qual valor do seu deposito!'
    else:
        conclusao['text'] = 'Digite seu número'
    botao1['state'] = DISABLED
    botao2['state'] = DISABLED
    botao3['state'] = DISABLED
    botao4['state'] = DISABLED
    botao5['state'] = DISABLED
    botao6['text'] = 'Confirmar'
    botao6['command'] = confirmar_deposito
    caixaTexto = Entry(janela, font='arial 15')
    caixaTexto.grid(column=1, row=5)
    caixa = caixaTexto
#Função para a confirmação do deposito
def confirmar_deposito():
    global caixa, saldoAtual, deposito_celular
    if caixa.get().isnumeric(): # numerico
        valorDeposito = int(caixa.get())
        if  deposito_celular:
            saldoAtual += valorDeposito
            conclusao['text'] = f'Valor R$ {valorDeposito} deposito com sucesso!'
        else:
            conclusao['text'] = f'Valor de R$ {valorDeposito}foi cadastrado com sucesso !'
    else:
         if deposito_celular:
            conclusao['text'] = 'Valor inválido'
         else:
            conclusao ['text'] = 'Número inválido'
    deposito_celular =True # Volta ao estado normal que é verdadeiro
    caixa.destroy()# destroy vai destruir a caixa para não ficar na interface
    janela.update()# Atualizar a janela
    botao1['state'] = NORMAL
    botao2['state'] = NORMAL
    botao3['state'] = NORMAL
    botao4['state'] = NORMAL
    botao5['state'] = NORMAL
    normalizar()# Volta LABEL E OS BOTOES

def desbloquear():
    global deposito_celular
    deposito_celular= False
    deposito()

def sair():
    quit()


#input nome, botoes

nome= ' Sayonnara \U0001F603'

introducao = Label(janela, text=f'Bem vindo(a) ao caixa eletrônico, senhor (a){nome.title()}', font='arial 12' , bg='white' )
introducao.grid(column=1, row=0, padx=5, pady=10)

img =ImageTk.PhotoImage(Image.open('download (1).png'))
imagem = Label(janela, image=img)
imagem.grid(column=1, row=2 )

botao1 = Button(janela, text=f'Saldo',command=saldo,height=2, width=15,bg='white')
botao1.grid(column=0, row=1, padx=10, pady=1)

botao2 = Button(janela, text=f'Saque', command=saque,height=2, width=15,bg='white')
botao2.grid(column=0, row=2, padx=10, pady=1)

botao3 = Button(janela, text=f'Depósito ',command= deposito,height=2, width=15,bg='white')
botao3.grid(column=0, row=3, padx=10, pady=1)

botao4= Button(janela, text=f'Pagar Conta',command=pagar, height=2, width=15,bg='white')
botao4.grid(column=2, row=1, padx=10, pady=1)

botao5 = Button(janela, text=f'Desb.Celular',command=desbloquear,height=2, width=15,bg='white')
botao5.grid(column=2, row=2, padx=10, pady=1)

botao6 = Button(janela, text=f'Sair ',command=sair,height=2, width=15,bg='white')
botao6.grid(column=2, row=3, padx=10, pady=1)

conclusao=Label(janela, text =f'O que deseja fazer?', font='arial 12',bg='white' )
conclusao.grid(column=1, row=4,padx=10, pady=20)

janela.mainloop()

