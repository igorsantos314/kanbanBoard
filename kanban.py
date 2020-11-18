import sqlite3
import os

class bd:

    def __init__(self):
        caminhoAtual = os.getcwd()
        print(caminhoAtual)

        self.conection = sqlite3.connect('{}/DataBase.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    def addToDo(self, atv, prioridade, data):
        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO ToDo (Atividade, Prioridade, Data_Entrega) VALUES("{}", "{}", "{}")'.format(atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addDoing(self, atv, prioridade, data):
        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO Doing (Atividade, Prioridade, Data_Entrega) VALUES("{}", "{}", "{}")'.format(atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addOnHold(self, atv, prioridade, data):
        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO OnHold (Atividade, Prioridade, Data_Entrega) VALUES("{}", "{}", "{}")'.format(atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

    def addDone(self, atv, prioridade, data):
        #INSERIR DADOS NA TABELA DE VENDAS
        command = 'INSERT INTO Done (Atividade, Prioridade, Data_Entrega) VALUES("{}", "{}", "{}")'.format(atv, prioridade, data)
        
        self.cur.execute(command)
        self.conection.commit()

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

    def dropPostIt(self, colun, atv):

        if colun == 0:
            #DELETAR DA COLUNA TO DO
            command = 'DELETE FROM ToDo WHERE Atividade = "{}"'.format(atv)

        elif colun == 1:
            #DELETAR DA COLUNA TO DO
            command = 'DELETE FROM Doing WHERE Atividade = "{}"'.format(atv)

        elif colun == 2:
            #DELETAR DA COLUNA TO DO
            command = 'DELETE FROM OnHold WHERE Atividade = "{}"'.format(atv)

        elif colun == 3:
            #DELETAR DA COLUNA TO DO
            command = 'DELETE FROM Done WHERE Atividade = "{}"'.format(atv)

        self.cur.execute(command)
        self.conection.commit()

    def changePostIt(self, colunAtual, colunDestino, atv, prio, data):
        
        #APAGAR DA COLUNA ATUAL
        self.dropPostIt(colunAtual, atv)

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
#print(a.getConfigs()[0][1])
"""a.addToDo('LISTA ELTON', 'III', '29/09')
a.addDoing('LISTA ELTON', 'III', '29/09')
a.addOnHold('LISTA ELTON', 'III', '29/09')
a.addDone('LISTA ELTON', 'III', '29/09')"""

