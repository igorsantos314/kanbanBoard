from tkinter import *
from kanban import *
from tkinter import messagebox, ttk

class kanbanBoard(Frame):

    def __init__(self):

        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

        #POSICAO DOS POSTITS
        self.dictPositionsToDo = {  0:(50, 60, 190, 226, 155, 90, 90, (0, 0)), 
                                    1:(50, 60, 190, 226, 255, 190, 190, (0, 1)), 
                                    2:(50, 60, 190, 226, 355, 290, 290, (0, 2)),
                                    3:(50, 60, 190, 226, 455, 390, 390, (0, 3)),
                                    4:(50, 60, 190, 226, 555, 490, 490, (0, 4)),
                                    5:(50, 60, 190, 226, 655, 590, 590, (0, 5)),
                                    6:(50, 60, 190, 226, 755, 690, 690, (0, 6)),
                                    7:(50, 60, 190, 226, 855, 790, 790, (0, 7))}

        #posXAtv, posXPrioridade, posXData, posXBt, posY, posYAtv, posYBt

        self.dictPositionsDoing = { 0:(370, 380, 510, 546, 155, 90, 90, (1, 0)), 
                                    1:(370, 380, 510, 546, 255, 190, 190, (1, 1)), 
                                    2:(370, 380, 510, 546, 355, 290, 290, (1, 2)),
                                    3:(370, 380, 510, 546, 455, 390, 390, (1, 3)),
                                    4:(370, 380, 510, 546, 555, 490, 490, (1, 4)),
                                    5:(370, 380, 510, 546, 655, 590, 590, (1, 5)),
                                    6:(370, 380, 510, 546, 655, 590, 590, (1, 5)),
                                    7:(370, 380, 510, 546, 655, 590, 590, (1, 5))}

        self.dictPositionsOnHold = {    0:(700, 710, 840, 876, 155, 90, 90, (2, 0)),
                                        1:(700, 710, 840, 876, 255, 190, 190, (2, 1)),
                                        2:(700, 710, 840, 876, 355, 290, 290, (2, 2)),
                                        3:(700, 710, 840, 876, 455, 390, 390, (2, 3)),
                                        4:(700, 710, 840, 876, 555, 490, 490, (2, 4)),
                                        5:(700, 710, 840, 876, 655, 590, 590, (2, 5)),
                                        6:(700, 710, 840, 876, 755, 690, 690, (2, 6)),
                                        7:(700, 710, 840, 876, 855, 790, 790, (2, 7))}                                    

        self.dictPositionsDone = {      0:(1030, 1040, 1170, 1206, 155, 90, 90, (3, 0)),
                                        1:(1030, 1040, 1170, 1206, 255, 190, 190, (3, 1)),
                                        2:(1030, 1040, 1170, 1206, 355, 290, 290, (3, 2)),
                                        3:(1030, 1040, 1170, 1206, 455, 390, 390, (3, 3)),
                                        4:(1030, 1040, 1170, 1206, 555, 490, 490, (3, 4)),
                                        5:(1030, 1040, 1170, 1206, 655, 590, 590, (3, 5)),
                                        6:(1030, 1040, 1170, 1206, 755, 690, 690, (3, 6)),
                                        7:(1030, 1040, 1170, 1206, 855, 790, 790, (3, 7))}

        #PADROES
        self.fontColuns = 'Courier 20 bold'
        self.fontPostIt = 'Courier 12'
        self.heightPostIt = 4
        self.widthPostIt = 22
        self.colorPostIt = 'Black'

        #CORES DOS POSTITS
        self.myConfigs = self.bancoDados.getConfigs()[0]

        self.colorToDo   = self.myConfigs[0]
        self.colorDoing  = self.myConfigs[1]
        self.colorOnHold = self.myConfigs[2]
        self.colorDone   = self.myConfigs[3]

        #LISTA DE POSTITS
        self.listPostIts = []

        self.curPosition = 0

        #CHAMAR O QUADRO KANBAN
        self.windowBoard()

    def windowBoard(self):

        self.windowMain = Tk()
        self.windowMain.geometry('1280x700+10+10')
        self.windowMain.resizable(False, False)
        self.windowMain.title('MY KANBAN BOARD - BY:IGOR SANTOS')

        #COLUNAS DO QUADRO
        self.setColunas()

        #PRESSIONAR F2 PARA CRIAR POST IT
        self.windowMain.bind("<F2>", self.keyPressed)
        self.windowMain.bind("<F3>", self.keyPressed)
        self.windowMain.bind("<F6>", self.keyPressed)
        self.windowMain.bind("<F8>", self.keyPressed)

        self.windowMain.mainloop()

    def keyPressed(self, event):
        l = event.keysym

        #enter
        if l == 'F2':
            #CRIAR NOVO POSIT
            self.createPostIt()

        elif l == 'F3':
            #APAGAR BOTOES DE EDICAO
            self.dropButtons()

        elif l == 'F6':
            self.upperList()

        elif l == 'F8':
            self.downList()

    def setColunas(self):

        #backgrounds
        bannerToDo = Label(width=40, height=60, bg=self.colorToDo)
        bannerToDo.place(x=0,y=0)

        bannerDoing = Label(width=40, height=60, bg=self.colorDoing)
        bannerDoing.place(x=320,y=0)

        bannerOnHold = Label(width=40, height=60, bg=self.colorOnHold)
        bannerOnHold.place(x=640,y=0)
        
        bannerDone = Label(width=40, height=60, bg=self.colorDone)
        bannerDone.place(x=960,y=0)

        #COLUNAS PADRÕES KANBAN
        lblToDo = Label(text='TO DO', font=self.fontColuns, bg=self.colorToDo)
        lblToDo.place(x=100,y=50)

        lblDoing = Label(text='DOING', font=self.fontColuns, bg=self.colorDoing)
        lblDoing.place(x=440,y=50)

        lblOnHold = Label(text='ON HOLD', font=self.fontColuns, bg=self.colorOnHold)
        lblOnHold.place(x=750,y=50)

        lblDone = Label(text='DONE', font=self.fontColuns, bg=self.colorDone)
        lblDone.place(x=1080,y=50)

        #CRIAR NOVO POSIT
        #btCreatePòst = Button(text='', font='Courier 12', bg='white', fg='red', command=self.createPostIt)
        #btCreatePòst.place(x=10, y=10)

        self.refreshBoard()

    def dropPostColumn(self):
        #DESTRUIR TODOS OS POSTITS PARA ATUALIZAR
        for p in self.listPostIts:
            p[0].destroy()
            p[1].destroy()
            p[2].destroy()
            p[3].destroy()

    def refreshBoard(self):

        #RESETA A POSICAO DO CURSO
        self.curPosition = 0

        #DESTRUIR POST ITS
        self.dropPostColumn()

        #ARMAZENAR TODOS OS POSTIT DE CADA COLUNA
        listPostItToDo = self.bancoDados.getToDo()
        listPostItDoing = self.bancoDados.getDoing()
        listPostItOnHold = self.bancoDados.getOnHold()
        listPostItDone = self.bancoDados.getDone()

        #SETAR POSTIT EM CADA COLUNA
        self.addPostItToDo(listPostItToDo)
        self.addPostItDoing(listPostItDoing)
        self.addPostItOnHold(listPostItOnHold)
        self.addPostItDone(listPostItDone)

    def addPostItToDo(self, toDo):
        #ADICIONAR POSTIT NA COLUNA DE TO DO
        for pos, postit in enumerate(toDo.__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 6:
                self.setPostIt( self.dictPositionsToDo[pos][0], self.dictPositionsToDo[pos][1], 
                                self.dictPositionsToDo[pos][2], self.dictPositionsToDo[pos][3], 
                                self.dictPositionsToDo[pos][4], self.dictPositionsToDo[pos][5], 
                                self.dictPositionsToDo[pos][6], self.dictPositionsToDo[pos][7],
                                postit[0], postit[1], postit[2], postit[3])

    def addPostItDoing(self, doing):
        #ADICIONAR POSTIT NA COLUNA DE Doing
        for pos, postit in enumerate(doing.__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 6:
                self.setPostIt( self.dictPositionsDoing[pos][0], self.dictPositionsDoing[pos][1], 
                                self.dictPositionsDoing[pos][2], self.dictPositionsDoing[pos][3], 
                                self.dictPositionsDoing[pos][4], self.dictPositionsDoing[pos][5], 
                                self.dictPositionsDoing[pos][6], self.dictPositionsDoing[pos][7],
                                postit[0], postit[1], postit[2], postit[3])

    def addPostItOnHold(self, onHold):
        #ADICIONAR POSTIT NA COLUNA DE ONHOLD
        for pos, postit in enumerate(onHold.__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 6:
                self.setPostIt( self.dictPositionsOnHold[pos][0], self.dictPositionsOnHold[pos][1], 
                                self.dictPositionsOnHold[pos][2], self.dictPositionsOnHold[pos][3], 
                                self.dictPositionsOnHold[pos][4], self.dictPositionsOnHold[pos][5], 
                                self.dictPositionsOnHold[pos][6], self.dictPositionsOnHold[pos][7],
                                postit[0], postit[1], postit[2], postit[3])

    def addPostItDone(self, done):
        #ADICIONAR POSTIT NA COLUNA DE DONE
        for pos, postit in enumerate(done.__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 6:
                self.setPostIt( self.dictPositionsDone[pos][0], self.dictPositionsDone[pos][1], 
                                self.dictPositionsDone[pos][2], self.dictPositionsDone[pos][3], 
                                self.dictPositionsDone[pos][4], self.dictPositionsDone[pos][5], 
                                self.dictPositionsDone[pos][6], self.dictPositionsDone[pos][7],
                                postit[0], postit[1], postit[2], postit[3])

    def setPostIt(self, posXAtv, posXPrioridade, posXData, posXBt, posY, posYAtv, posYBt, editPostIt, id, atv, prio, data):
        
        posXBt -= 175

        #BOTAO DE EDICAO E NOME ATV
        btEditAtv = Button(text=atv, bg=self.colorPostIt, fg='white', font=self.fontPostIt, height=self.heightPostIt, width=self.widthPostIt, command=lambda : self.changeEditPostIt(editPostIt[0], id, atv, prio, data))
        btEditAtv.place(x=posXAtv, y=posYAtv)

        lblPrioridade = Label(text=prio, fg='white', font=self.fontPostIt, bg=self.colorPostIt)
        lblPrioridade.place(x=posXPrioridade, y=posY)

        lblData = Label(text=data, fg='white', font=self.fontPostIt, bg=self.colorPostIt)
        lblData.place(x=posXData, y=posY)

        ticket = Label(bg=self.getColorPrio(prio), font='Courier 4', height=12, width=1)
        ticket.place(x=posXBt, y=posYBt)

        #ADICIONAR TUPLA DE POSIT NA LISTA
        tuplaPostIt = (lblPrioridade, lblData, btEditAtv, ticket)

        self.listPostIts.append(tuplaPostIt)

    def getColorPrio(self, p):

        if p == 'IV':
            return 'Red'

        elif p == 'III':
            return 'Yellow'

        elif p == 'II':
            return 'LimeGreen'

        elif p == 'I':
            return 'Blue'

    def downList(self):
        self.curPosition += 1

        #DESTRUIR POST ITS
        self.dropPostColumn()

        #PEGA A LISTA DO BANCO DE DADOS 
        listPostItToDo = self.bancoDados.getToDo()
        listPostItDoing = self.bancoDados.getDoing()
        listPostItOnHold = self.bancoDados.getOnHold()
        listPostItDone = self.bancoDados.getDone()

        #DIVIDE EM PARTES DE 6
        listSixPostItToDo = self.divideListPostIt(listPostItToDo)
        listSixPostItDoing = self.divideListPostIt(listPostItDoing)
        listSixPostItOnHold = self.divideListPostIt(listPostItOnHold)
        listSixPostItDone = self.divideListPostIt(listPostItDone)

        #VERIFICA SE A QUANTIDADE 
        if len(listPostItToDo) > (self.curPosition * 6):
            self.addPostItToDo(listSixPostItToDo[self.curPosition])

        if len(listPostItDoing) > (self.curPosition * 6):
            self.addPostItDoing(listSixPostItDoing[self.curPosition])

        if len(listPostItOnHold) > (self.curPosition * 6):
            self.addPostItOnHold(listSixPostItOnHold[self.curPosition])

        if len(listPostItDone) > (self.curPosition * 6):
            self.addPostItDone(listSixPostItDone[self.curPosition])

    def upperList(self):

        if self.curPosition == 0:
            self.refreshBoard()
        
        else:
            self.curPosition -= 2
            self.downList()

    def divideListPostIt(self, postit):
        
        newList = []
        iteracoes = round((len(postit)/6) + 0.5)
        postit = postit[::-1]

        for i in range(iteracoes):
            newList.append( postit[i*6:(i+1)*6] )

        return newList

    def createPostIt(self):

        #COR DA JANELA
        colorTheme = 'Bisque'
        fontPostItBold = 'Courier 12 bold'

        #PANEL DE TELA EMBUTIDA
        panel = Label(width=55, height=20, bg='SpringGreen')
        panel.place(x=430, y=100)

        lblTitle = Label(text='NEW POST-IT', font='Courier 17 bold', fg='Black', bg='SpringGreen')
        lblTitle.place(x=580, y=110)

        #CAMPO PARA O NOME DA ATIVIDADE
        lblAtividade = Label(text='Atividade:', font='Courier 12', bg='SpringGreen')
        lblAtividade.place(x=450, y=150)

        etAtividade = Entry(font='Courier 12', fg='Red')
        etAtividade.place(x=450, y=170)

        #CAMPO PARA A PRIORIDADE DA ATIVIDADE
        lblPrioridade = Label(text='PRIORIDADE:', font='Courier 12', bg='SpringGreen')
        lblPrioridade.place(x=450, y=210)

        comboPrioridade = ttk.Combobox(width=12, font='Courier 12') 

        comboPrioridade['values'] = ['I', 'II', 'III', 'IV']
        comboPrioridade.place(x=450, y=230)

        #CAMPO PARA O DIA
        lblDia = Label(text='Dia:', font='Courier 12', bg='SpringGreen')
        lblDia.place(x=450, y=270)

        comboDia = ttk.Combobox(width=12, font='Courier 12') 

        comboDia['values'] = [i for i in range(1, 32)]
        comboDia.place(x=450, y=290)

        #CAMPO PARA O MES
        lblMes = Label(text='Mes:', font='Courier 12', bg='SpringGreen')
        lblMes.place(x=450, y=330)

        comboMes = ttk.Combobox(width=12, font='Courier 12') 

        comboMes['values'] = [i for i in range(1, 13)]
        comboMes.place(x=450, y=350)

        def detroyItens():

            #DESTRUIR TODOS OS OBJETOS
            panel.destroy()

            lblTitle.destroy()
            lblAtividade.destroy()
            lblPrioridade.destroy()
            lblDia.destroy()
            lblMes.destroy()

            etAtividade.destroy()

            comboPrioridade.destroy()
            comboDia.destroy()
            comboMes.destroy()

            btClose.destroy()
            btSave.destroy()

            #DESTRUIR BOTOES DE EDICAO
            self.dropButtons()

        def save():
            #DATA FORMATADA
            data = F'{comboDia.get()}/{comboMes.get()}'

            self.bancoDados.addToDo(    etAtividade.get().upper(),
                                        comboPrioridade.get().upper(),
                                        data)
            
            messagebox.showinfo('','SUCESS !')

            #ATUALIZAR COLUNAS
            self.refreshBoard()

            #DESTRUIR A TELA PARA SE SOBREPOR AOS BOTOES
            detroyItens()

            #CALL EM TELA DE ADD POSTIT
            self.createPostIt()

        btClose = Button(text='Close', bg='Tomato', command=detroyItens)
        btClose.place(x=730, y=400)

        btSave = Button(text='Save', bg='SpringGreen', command=save)
        btSave.place(x=800, y=400)

    def dropButtons(self):
        #APAGAR BOTOES DE EDICAO PARA RECRIAR
        try:
            self.btTodo.destroy()
        except:
            pass

        try:
            self.btDoing.destroy()
        except:
            pass

        try:
            self.btOnHold.destroy()
        except:
            pass

        try:
            self.btDone.destroy()
        except:
            pass

        try:
            self.btEdit.destroy()
        except:
            pass

        try:
            self.btDel.destroy()
        except:
            pass

    def locationButtons(self, colunm):
            
        #SETAR POSICAO DE BOTOES DE ACORDO COM A COULUNA
        if colunm == 0:
            return [(10, 10),(110, 10)]

        elif colunm == 1:
            return [(330, 10),(430, 10)]

        elif colunm == 2:
            return [(650, 10),(750, 10)]
        
        elif colunm == 3:
            return [(970, 10),(1070, 10)]

    def changeEditPostIt(self, colunm, id, atv, prio, data):
    
        #COLUNM COLUNA ORIGEM
        colorTheme = 'white'

        #LIMPAR BOTOES DE EDICAO
        self.dropButtons()

        #print(colunm, atv, prio, data)
        def setModification(toMove):
            if 0 == toMove:
                #MOVER POST IR PARA TO DO
                self.bancoDados.changePostIt(colunm, 0, id, atv, prio, data)

            elif 1 == toMove:
                #MOVER POST IR PARA DOING
                self.bancoDados.changePostIt(colunm, 1, id, atv, prio, data)

            elif 2 == toMove:    
                #MOVER POST IR PARA ON HOLD
                self.bancoDados.changePostIt(colunm, 2, id, atv, prio, data)

            elif 3 == toMove:
                #MOVER POST IR PARA DONE
                self.bancoDados.changePostIt(colunm, 3, id, atv, prio, data)

            elif toMove == 5:
                #APAGAR O POSTIT
                self.bancoDados.dropPostIt(id, colunm)

            #LIMPAR BOTOES DE EDICAO
            self.dropButtons()

            #ATUALIZAR QUADRO
            self.refreshBoard()

        #RETORNA DUAS TUPLAS COM POSICOES X E Y
        posicoes = self.locationButtons(colunm)

        #BOTAO DE DELETAR E EDITAR
        self.btEdit = Button(text='EDIT', font='Courier 12 bold', width=7, bg='white', fg='black', command=lambda:self.editPostIt(colunm, id, atv, prio, data))
        self.btEdit.place(x=posicoes[0][0], y=posicoes[0][1])

        self.btDel = Button(text='DEL', font='Courier 12 bold', width=7, bg='red', fg='white', command=lambda:setModification(5))
        self.btDel.place(x=posicoes[1][0], y=posicoes[1][1])
        
        #BOTOES PARA MOVER OS POSTITS
        if 0 != colunm:
            #MOVER POST IR PARA TO DO
            self.btTodo = Button(text='TO DO', font='Courier 12 bold', width=7, bg=self.colorToDo, command=lambda:setModification(0))
            self.btTodo.place(x=10, y=10)

        if 1 != colunm:
            #MOVER POST IR PARA DOING
            self.btDoing = Button(text='TO DOING', font='Courier 12 bold', width=7, bg=self.colorDoing, command=lambda:setModification(1))
            self.btDoing.place(x=330, y=10)

        if 2 != colunm:
            #MOVER POST IR PARA ON HOLD
            self.btOnHold = Button(text='TO ON HOLD', font='Courier 12 bold', width=7, bg=self.colorOnHold, command=lambda:setModification(2))
            self.btOnHold.place(x=650, y=10)
        
        if 3 != colunm:
            #MOVER POST IR PARA DONE
            self.btDone = Button(text='TO DONE', font='Courier 12 bold', width=7, bg=self.colorDone, command=lambda:setModification(3))
            self.btDone.place(x=970, y=10)

        #SETAR POSICOES
        
    def editPostIt(self, colunm, id, atv, prio, data):
        
        #DIVIDIR A DATA ENTRE DIA E MES
        newData = data.split('/')
        d = newData[0]
        m = newData[1]

        #PANEL DE TELA EMBUTIDA
        panel = Label(width=55, height=20, bg='white')
        panel.place(x=430, y=100)

        lblTitle = Label(text='EDIT POST-IT', font='Courier 17 bold', bg='White', fg='Red')
        lblTitle.place(x=580, y=110)

        #CAMPO PARA O NOME DA ATIVIDADE
        lblAtividade = Label(text='Atividade:', font='Courier 12', bg='white')
        lblAtividade.place(x=450, y=150)

        etAtividade = Entry(font='Courier 12', fg='Red')
        etAtividade.place(x=450, y=170)

        etAtividade.insert(0, atv)

        #CAMPO PARA A PRIORIDADE DA ATIVIDADE
        lblPrioridade = Label(text='Atividade:', font='Courier 12', bg='white')
        lblPrioridade.place(x=450, y=210)

        comboPrioridade = ttk.Combobox(width=12, font='Courier 12') 

        comboPrioridade['values'] = ['I', 'II', 'III', 'IV', 'V']
        comboPrioridade.place(x=450, y=230)
        comboPrioridade.insert(0, prio)

        #CAMPO PARA O DIA
        lblDia = Label(text='Dia:', font='Courier 12', bg='white')
        lblDia.place(x=450, y=270)

        comboDia = ttk.Combobox(width=12, font='Courier 12') 

        comboDia['values'] = [i for i in range(1, 32)]
        comboDia.place(x=450, y=290)
        comboDia.insert(0, d)

        #CAMPO PARA O MES
        lblMes = Label(text='Mes:', font='Courier 12', bg='white')
        lblMes.place(x=450, y=330)

        comboMes = ttk.Combobox(width=12, font='Courier 12') 

        comboMes['values'] = [i for i in range(1, 13)]
        comboMes.place(x=450, y=350)
        comboMes.insert(0, m)

        def detroyItens():

            #DESTRUIR TODOS OS OBJETOS
            panel.destroy()

            lblTitle.destroy()
            lblAtividade.destroy()
            lblPrioridade.destroy()
            lblDia.destroy()
            lblMes.destroy()

            etAtividade.destroy()

            comboPrioridade.destroy()
            comboDia.destroy()
            comboMes.destroy()

            btClose.destroy()
            btSave.destroy()

            #DESTRUIR BOTOES DE EDICAO
            self.dropButtons()

        def save():
            pass

        btClose = Button(text='Close', bg='Tomato', command=detroyItens)
        btClose.place(x=730, y=400)

        btSave = Button(text='Save', bg='SpringGreen', command='')
        btSave.place(x=800, y=400)

kanbanBoard()