import sqlite3
import os

class bd:

    def __init__(self):
        caminhoAtual = os.getcwd()
        print(caminhoAtual)

        self.conection = sqlite3.connect('{}/DataBase.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    def createTables(self):

        #TABLES 
        tables = ['ToDo', 'Doing', 'OnHold', 'Done']

        for i in tables:
            #INSERIR DADOS NA TABELA DE VENDAS
            command = F'Create Table {i} (Id, Atividade, Prioridade, Data_Entrega)'
            
            self.cur.execute(command)
            self.conection.commit()

    def createTableConfigs(self):

        #CRIAR TABELA DE CONFIGURAÇÕES
        command = 'Create Table configs (columnColorToDo, columnColorDoing, columnColorOnHold, columnColorDone)'

        self.cur.execute(command)
        self.conection.commit()

    def addToDo(self, atv, prioridade, data):

        #RECEBE O NOVO ID
        id = self.getLastIdTables('ToDo')

        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO ToDo (Id, Atividade, Prioridade, Data_Entrega) VALUES({}, "{}", "{}", "{}")'.format(id, atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addDoing(self, atv, prioridade, data):
        #RECEBE O NOVO ID
        id = self.getLastIdTables('Doing')

        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO Doing (Id, Atividade, Prioridade, Data_Entrega) VALUES({}, "{}", "{}", "{}")'.format(id, atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addOnHold(self, atv, prioridade, data):
        #RECEBE O NOVO ID
        id = self.getLastIdTables('OnHold')

        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO OnHold (Id, Atividade, Prioridade, Data_Entrega) VALUES({}, "{}", "{}", "{}")'.format(id, atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addDone(self, atv, prioridade, data):

        #RECEBE O NOVO ID
        id = self.getLastIdTables('Done')

        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO Done (Id, Atividade, Prioridade, Data_Entrega) VALUES({},    "{}", "{}", "{}")'.format(id, atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def getLastIdTables(self, table):
        
        listPostIts = []

        if table == 'ToDo':
            listPostIts = self.getToDo()
        
        elif table == 'Doing':
            listPostIts = self.getDoing()
        
        elif table == 'OnHold':
            listPostIts = self.getOnHold()

        elif table == 'Done':
            listPostIts = self.getDone()    

        if len(listPostIts) == 0:
            return 0

        else:
            return listPostIts[-1][0] + 1

    def getToDo(self):
        show = "SELECT * FROM ToDo"
        self.cur.execute(show)

        product = self.cur.fetchall()
        return product

    def getDoing(self):
        show = "SELECT * FROM Doing"
        self.cur.execute(show)

        product = self.cur.fetchall()
        return product

    def getOnHold(self):
        show = "SELECT * FROM OnHold"
        self.cur.execute(show)

        product = self.cur.fetchall()

        return product

    def getDone(self):
        show = "SELECT * FROM Done"
        self.cur.execute(show)

        product = self.cur.fetchall()

        return product

    def dropPostIt(self, id, colun):

        if colun == 0:
            #DELETAR DA COLUNA TO DO
            command = F'DELETE FROM ToDo WHERE Id = {id}'

        elif colun == 1:
            #DELETAR DA COLUNA TO DO
            command = F'DELETE FROM Doing WHERE Id = {id}'

        elif colun == 2:
            #DELETAR DA COLUNA TO DO
            command = F'DELETE FROM OnHold WHERE Id = {id}'

        elif colun == 3:
            #DELETAR DA COLUNA TO DO
            command = F'DELETE FROM Done WHERE Id = {id}'

        self.cur.execute(command)
        self.conection.commit()

    def changePostIt(self, colunAtual, colunDestino, id, atv, prio, data):
        
        #APAGAR DA COLUNA ATUAL
        self.dropPostIt(id, colunAtual)

        if colunDestino == 0:
            #CRIAR POST NA COLUNA DE DESTINO
            self.addToDo(atv, prio, data)

        elif colunDestino == 1:
            #CRIAR POST NA COLUNA DE DESTINO
            self.addDoing(atv, prio, data)

        elif colunDestino == 2:
            #CRIAR POST NA COLUNA DE DESTINO
            self.addOnHold(atv, prio, data)

        elif colunDestino == 3:
            #CRIAR POST NA COLUNA DE DESTINO
            self.addDone(atv, prio, data)

    # --------------------------- CONFIGURAÇÕES -----------------------------
    def setConfigs(self):
        colors = [  'Tomato',
                    'PaleGoldenrod',
                    'PowderBlue',
                    'PaleGreen']

        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO configs (columnColorToDo, columnColorDoing, columnColorOnHold, columnColorDone) VALUES("{}", "{}", "{}", "{}")'.format(colors[0], colors[1], colors[2], colors[3])
        
        self.cur.execute(command)
        self.conection.commit()

    def getConfigs(self):
        show = "SELECT * FROM configs"
        self.cur.execute(show)

        configs = self.cur.fetchall()
        return configs

a = bd()
#a.setConfigs()
#a.createTableConfigs()
#a.createTables()
#print(a.getConfigs()[0][1])
#a.addToDo('LISTA ELTON', 'III', '29/09')
#a.addDoing('LISTA ELTON', 'III', '29/09')
#a.addOnHold('LISTA ELTON', 'III', '29/09')
#a.addDone('LISTA ELTON', 'III', '29/09')

