from tkinter import *
from kanban import *
from tkinter import messagebox

class kanbanBoard:

    def __init__(self):

        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

        #POSICAO DOS POSTITS
        self.dictPositionsToDo = {  0:(50, 60, 240, 275, 155, 90, 90, (0, 0)), 
                                    1:(50, 60, 240, 275, 255, 190, 190, (0, 1)), 
                                    2:(50, 60, 240, 275, 355, 290, 290, (0, 2)),
                                    3:(50, 60, 240, 275, 455, 390, 390, (0, 3)),
                                    4:(50, 60, 240, 275, 555, 490, 490, (0, 4)),
                                    5:(50, 60, 240, 275, 655, 590, 590, (0, 5)),
                                    6:(50, 60, 240, 275, 755, 690, 690, (0, 6)),
                                    7:(50, 60, 240, 275, 855, 790, 790, (0, 7))}

        self.dictPositionsDoing = { 0:(450, 460, 640, 675, 155, 90, 90, (1, 0)), 
                                    1:(450, 460, 640, 675, 255, 190, 190, (1, 1)), 
                                    2:(450, 460, 640, 675, 355, 290, 290, (1, 2)),
                                    3:(450, 460, 640, 675, 455, 390, 390, (1, 3)),
                                    4:(450, 460, 640, 675, 555, 490, 490, (1, 4)),
                                    5:(450, 460, 640, 675, 655, 590, 590, (1, 5)),
                                    6:(450, 460, 640, 675, 655, 590, 590, (1, 5)),
                                    7:(450, 460, 640, 675, 655, 590, 590, (1, 5))}

        self.dictPositionsOnHold = {    0:(850, 860, 1040, 1075, 155, 90, 90, (2, 0)),
                                        1:(850, 860, 1040, 1075, 255, 190, 190, (2, 1)),
                                        2:(850, 860, 1040, 1075, 355, 290, 290, (2, 2)),
                                        3:(850, 860, 1040, 1075, 455, 390, 390, (2, 3)),
                                        4:(850, 860, 1040, 1075, 555, 490, 490, (2, 4)),
                                        5:(850, 860, 1040, 1075, 655, 590, 590, (2, 5)),
                                        6:(850, 860, 1040, 1075, 755, 690, 690, (2, 6)),
                                        7:(850, 860, 1040, 1075, 855, 790, 790, (2, 7))}                                    

        self.dictPositionsDone = {      0:(1280, 1290, 1470, 1505, 155, 90, 90, (3, 0)),
                                        1:(1280, 1290, 1470, 1505, 255, 190, 190, (3, 1)),
                                        2:(1280, 1290, 1470, 1505, 355, 290, 290, (3, 2)),
                                        3:(1280, 1290, 1470, 1505, 455, 390, 390, (3, 3)),
                                        4:(1280, 1290, 1470, 1505, 555, 490, 490, (3, 4)),
                                        5:(1280, 1290, 1470, 1505, 655, 590, 590, (3, 5)),
                                        6:(1280, 1290, 1470, 1505, 755, 690, 690, (3, 6)),
                                        7:(1280, 1290, 1470, 1505, 855, 790, 790, (3, 7))}

        #PADROES
        self.fontColuns = 'Courier 20 bold'
        self.fontPostIt = 'Courier 12'
        self.heightPostIt = 5
        self.widthPostIt = 25
        self.colorPostIt = 'white'

        #LISTA DE POSTITS
        self.listPostIts = []

        #CHAMAR O QUADRO KANBAN
        self.windowBoard()

    def windowBoard(self):

        self.windowMain = Tk()
        self.windowMain.geometry('1600x900+10+10')
        self.windowMain.resizable(False, False)
        self.windowMain.title('MY KANBAN BOARD - IGOR SANTOS')

        #COLUNAS DO QUADRO
        self.setColunas()

        self.windowMain.mainloop()

    def setColunas(self):

        #backgrounds
        bannerToDo = Label(width=50, height=60, bg='Tomato')
        bannerToDo.place(x=0,y=0)

        bannerDoing = Label(width=55, height=60, bg='PaleGoldenrod')
        bannerDoing.place(x=370,y=0)

        bannerOnHold = Label(width=55, height=60, bg='PowderBlue')
        bannerOnHold.place(x=780,y=0) 
        
        bannerDone = Label(width=55, height=60, bg='PaleGreen')
        bannerDone.place(x=1210,y=0)

        #COLUNAS PADRÕES KANBAN
        lblToDo = Label(text='TO DO', font=self.fontColuns, bg='Tomato')
        lblToDo.place(x=100,y=50)

        lblDoing = Label(text='DOING', font=self.fontColuns, bg='PaleGoldenrod')
        lblDoing.place(x=520,y=50)

        lblOnHold = Label(text='ON HOLD', font=self.fontColuns, bg='PowderBlue')
        lblOnHold.place(x=920,y=50)

        lblDone = Label(text='DONE', font=self.fontColuns, bg='PaleGreen')
        lblDone.place(x=1370,y=50)

        #CRIAR NOVO POSIT
        btCreatePòst = Button(text='>>', font='Courier 12 bold', bg='white', fg='red', width=1, command=self.createPostIt)
        btCreatePòst.place(x=10, y=10)

        self.refreshBoard()

    def dropPostColumn(self):
        #DESTRUIR TODOS OS POSTITS PARA ATUALIZAR
        for p in self.listPostIts:
            p[0].destroy()
            p[1].destroy()
            p[2].destroy()
            p[3].destroy()

    def refreshBoard(self):
        
        #DESTRUIR POST ITS
        self.dropPostColumn()

        #ADCIOINAR POSTIT NA COLUNA DE TO DO
        for pos, postit in enumerate(self.bancoDados.getToDo().__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 8:
                self.setPostIt( self.dictPositionsToDo[pos][0], self.dictPositionsToDo[pos][1], 
                                self.dictPositionsToDo[pos][2], self.dictPositionsToDo[pos][3], 
                                self.dictPositionsToDo[pos][4], self.dictPositionsToDo[pos][5], 
                                self.dictPositionsToDo[pos][6], self.dictPositionsToDo[pos][7],
                                postit[0], postit[1], postit[2])

        #ADCIOINAR POSTIT NA COLUNA DE Doing
        for pos, postit in enumerate(self.bancoDados.getDoing().__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 8:
                self.setPostIt( self.dictPositionsDoing[pos][0], self.dictPositionsDoing[pos][1], 
                                self.dictPositionsDoing[pos][2], self.dictPositionsDoing[pos][3], 
                                self.dictPositionsDoing[pos][4], self.dictPositionsDoing[pos][5], 
                                self.dictPositionsDoing[pos][6], self.dictPositionsDoing[pos][7],
                                postit[0], postit[1], postit[2])

        #ADCIOINAR POSTIT NA COLUNA DE ONHOLD
        for pos, postit in enumerate(self.bancoDados.getOnHold().__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 8:
                self.setPostIt( self.dictPositionsOnHold[pos][0], self.dictPositionsOnHold[pos][1], 
                                self.dictPositionsOnHold[pos][2], self.dictPositionsOnHold[pos][3], 
                                self.dictPositionsOnHold[pos][4], self.dictPositionsOnHold[pos][5], 
                                self.dictPositionsOnHold[pos][6], self.dictPositionsOnHold[pos][7],
                                postit[0], postit[1], postit[2])

        #ADCIOINAR POSTIT NA COLUNA DE DONE
        for pos, postit in enumerate(self.bancoDados.getDone().__reversed__()):

            #APARECER APENAS 8 POSTIT EM ORDEM QUE FOI CRIADA
            if pos < 8:
                self.setPostIt( self.dictPositionsDone[pos][0], self.dictPositionsDone[pos][1], 
                                self.dictPositionsDone[pos][2], self.dictPositionsDone[pos][3], 
                                self.dictPositionsDone[pos][4], self.dictPositionsDone[pos][5], 
                                self.dictPositionsDone[pos][6], self.dictPositionsDone[pos][7],
                                postit[0], postit[1], postit[2])

    def setPostIt(self, posXAtv, posXPrioridade, posXData, posXBt, posY, posYAtv, posYBt, editPostIt, atv, prio, data):
        #CRIAÇÃO DE POST ITS
        lblAtividade = Label(text=atv, font=self.fontPostIt, height=self.heightPostIt, width=self.widthPostIt, bg=self.colorPostIt)
        lblAtividade.place(x=posXAtv, y=posYAtv)

        lblPrioridade = Label(text=prio, font=self.fontPostIt, bg=self.colorPostIt)
        lblPrioridade.place(x=posXPrioridade, y=posY)

        lblData = Label(text=data, font=self.fontPostIt, bg=self.colorPostIt)
        lblData.place(x=posXData, y=posY)

        btEdit = Button(text='', command=lambda : self.changeEditPostIt(editPostIt[0], atv, prio, data))
        btEdit.place(x=posXBt, y=posYBt)

        #ADICIONAR TUPLA DE POSIT NA LISTA
        tuplaPostIt = (lblAtividade, lblPrioridade, lblData, btEdit)

        self.listPostIts.append(tuplaPostIt)

    def createPostIt(self):

        #COR DA JANELA
        colorTheme = 'Bisque'
        fontPostItBold = 'Courier 12 bold'

        windowCreatePostIt = Tk()

        windowCreatePostIt.resizable(False, False)
        windowCreatePostIt.title('Create PostIt')
        windowCreatePostIt['bg'] = colorTheme

        lblWork = Label(windowCreatePostIt, text='WORK', font=fontPostItBold, bg=colorTheme)
        lblWork.pack(pady=5)

        #CAMPO DE ATIVIDADE
        etWork = Entry(windowCreatePostIt, font=fontPostItBold, bg=colorTheme, fg='red')
        etWork.pack()

        lblPrio = Label(windowCreatePostIt, text='PRIORITY', font=fontPostItBold, bg=colorTheme)
        lblPrio.pack(pady=5)

        #CAMPO DE PRIORIDADE
        etPriority = Entry(windowCreatePostIt, font=fontPostItBold, bg=colorTheme, fg='red')
        etPriority.pack()

        lblDate = Label(windowCreatePostIt, text='DATE', font=fontPostItBold, bg=colorTheme)
        lblDate.pack(pady=5)
        
        #CAMPO DE DATA
        etDate = Entry(windowCreatePostIt, font=fontPostItBold, bg=colorTheme, fg='red')
        etDate.pack()

        #LIMPAR OS CAMPOS
        def clearCamps():
            etWork.delete(0, END)
            etPriority.delete(0, END)
            etDate.delete(0, END)

        #ADICIONAR O POSTIT NA COLUNA TO DO POR PADRÃO
        def addPostIt():
            self.bancoDados.addToDo(    etWork.get().upper(),
                                        etPriority.get().upper(),
                                        etDate.get())
            
            messagebox.showinfo('','SUCESS !')

            #LIMPAR OS CAMPOS
            clearCamps()

            #ATUALIZAR COLUNAS
            self.refreshBoard()

            #FECHAR TELA DE ADICIONAR POSTIT
            windowCreatePostIt.destroy()

        #BOTAO DE ADICIONAR O POSTIT
        btCreate = Button(windowCreatePostIt, text='CREATE POSTIT', bg='red', fg='white', command=addPostIt)
        btCreate.pack(pady=5)

        #FOCAR NO CAMPO WORK
        etWork.focus()

        windowCreatePostIt.mainloop()

    def changeEditPostIt(self, colunm, atv, prio, data):

        colorTheme = 'white'

        windowEdit = Tk()
        windowEdit.resizable(False,False)
        windowEdit.geometry('430x40+10+10')
        windowEdit.title('MOVER POST IT TO')
        windowEdit['bg'] = colorTheme

        def setModification():
            if 0 != colunm:
                #MOVER POST IR PARA TO DO
                self.bancoDados.changePostIt(colunm, 0, atv, prio, data)

            elif 1 != colunm:
                #MOVER POST IR PARA DOING
                self.bancoDados.changePostIt(colunm, 1, atv, prio, data)

            elif 2 != colunm:    
                #MOVER POST IR PARA ON HOLD
                self.bancoDados.changePostIt(colunm, 2, atv, prio, data)

            elif 3 != colunm:
                #MOVER POST IR PARA DONE
                self.bancoDados.changePostIt(colunm, 3, atv, prio, data)

            #FECHAR JANELA
            windowEdit.destroy()

            #ATUALIZAR QUADRO
            self.refreshBoard()


        #BOTOES PARA MOVER OS POSTITS
        if 0 != colunm:
            #MOVER POST IR PARA TO DO
            btTodo = Button(windowEdit, text='TO DO', font='Courier 20 bold', bg='Tomato', command=setModification)
            btTodo.pack(side=LEFT)

        if 1 != colunm:
            #MOVER POST IR PARA DOING
            btTodo = Button(windowEdit, text='DOING', font='Courier 20 bold', bg='PaleGoldenrod', command=setModification)
            btTodo.pack(side=LEFT)

        if 2 != colunm:
            #MOVER POST IR PARA ON HOLD
            btTodo = Button(windowEdit, text='ON HOLD', font='Courier 20 bold', bg='PowderBlue', command=setModification)
            btTodo.pack(side=LEFT)
        
        if 3 != colunm:
            #MOVER POST IR PARA DONE
            btTodo = Button(windowEdit, text='DONE', font='Courier 20 bold', bg='PaleGreen', command=setModification)
            btTodo.pack(side=LEFT)

        #BOTAO DE EDICAO
        btEdit = Button(windowEdit, text='Edit', font='Courier 20 bold', bg='red', fg='white', command='')
        btEdit.pack(side=LEFT)

        windowEdit.mainloop()

kanbanBoard()