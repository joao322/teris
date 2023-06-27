from random import choice

import customtkinter as ctk

janela = ctk.CTk()
frame = ctk.CTkFrame(janela)
frame.pack()


class Game():
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global canvas
        
        self.rotacao = 0
        self.play_pos = list()
        self.poder_cair = 6
        self.delei = 6
        
        self.lista = list()
        self.pontos_deletado = list()
        self.ja_colidiu = False
        self.reboot_on = False
        
        self.cores = {2: '#FF0000', 4: '#00FF00', 6: '#0000FF', 8: '#FFFF00', 10: '#00FFFF', 12: '#E9D1A0', 14: '#FFA500'}
        
        # o = Obijeto numero igual a cor, p = pos x 0 y 0
        self.obigeto = {'i': [['o2p00', 'o2p10', 'o2p20', 'o2p30'], ['o2p00', 'o2p01', 'o2p02', 'o2p03']],
                        'j': [['o4p00', 'o4p01', 'o4p11', 'o4p21'], ['o4p10', 'o4p11', 'o4p12', 'o4p02'], ['o4p00', 'o4p10', 'o4p01', 'o4p02'], ['o4p00', 'o4p10', 'o4p20', 'o4p21']],
                        'l': [['o6p01', 'o6p00', 'o6p10', 'o6p20'], ['o6p00', 'o6p01', 'o6p02', 'o6p12'], ['o6p00', 'o6p10', 'o6p11', 'o6p12'], ['o6p20', 'o6p21', 'o6p01', 'o6p11']],
                        'o': [['o8p00', 'o8p01', 'o8p10', 'o08p11']],
                        's': [['o10p10', 'o10p20', 'o10p01', 'o10p11'], ['o10p00', 'o10p01', 'o10p11', 'o10p12']],
                        't': [['o12p00', 'o12p10', 'o12p11', 'o12p20'], ['o12p01', 'o12p10', 'o12p11', 'o12p12'], ['o12p01', 'o12p11', 'o12p10', 'o12p21'], ['o12p00', 'o12p01', 'o12p11', 'o12p02']],
                        'z': [['o14p00', 'o14p10', 'o14p11', 'o14p21'], ['o14p10', 'o14p11', 'o14p01', 'o14p02']]
                        }

        canvas = ctk.CTkCanvas(frame, width=200, height=400, bg='black')
        canvas.grid()
        # Criando a matriz do jogo  
        self.matriz = [list(0 for i in range(0, 40)) for i in range(0, 20)]
        
        self.tamnho_x = len(self.matriz)
        self.tamnho_y = len(self.matriz[0])
        
        self.novo_bloco()
        janela.bind("<Key>", self.inputs)
        janela.after(2000 // 5, self.update)

    def inputs(self, key):
        print(key.keycode)
        if key.keycode == 114 and all(x < self.tamnho_x - 1  and self.matriz[x +1 ][y] in [0, 9] for x, y in self.play_pos):
            self.limpar_tela()
            
            for x, y in self.play_pos:
                self.matriz[x + 1][y] = 9
                            
        elif key.keycode == 113 and all(x > 0   and self.matriz[x -1 ][y] in [0, 9] for x, y in self.play_pos):
            self.limpar_tela()
            
            for x, y in self.play_pos:
                self.matriz[x -1][y] = 9
                
        elif key.keycode == 116:
            self.poder_cair = 0
            self.cair_bloco()
            
        elif key.keycode == 111 and not self.ja_colidiu and self.delei >= 10:
            
            pre_rotacao = self.rotacao
            self.delei = 0
            if self.rotacao + 1 < len(self.obigeto[self.celecionado]):
                pre_rotacao += 1
                
            else:
                pre_rotacao = 0
                
            try:
                ponto_inicial = self.play_pos[0]
                
                if any((ponto_inicial[0] + int(o[-2]) > self.tamnho_x -1 or ponto_inicial[0] + int(o[-2]) < 0  or
                    ponto_inicial[1] + int(o[-1]) >= self.tamnho_y -1) or self.matriz[ponto_inicial[0] + int(o[-2])][ponto_inicial[1] + int(o[-1])] not in [0, 9]
                       for o in self.obigeto[self.celecionado][pre_rotacao]):
                    
                    pre_rotacao -= 1
                    
                self.limpar_tela() 
                self.rotacao = pre_rotacao
                
                for o in self.obigeto[self.celecionado][self.rotacao]:
                    self.matriz[int(o[-2]) + self.play_pos[0][0]
                        ][self.play_pos[0][1] + int(o[-1])] = 9
                
            except IndexError:
                pass
        else:
            frame.pack_forget()
    def cair_bloco(self):
        
        if self.play_pos == []:
            self.novo_bloco()
            self.play_pos = [0,0]
            
                
        try:  
            if all(y < self.tamnho_y - 1 and self.matriz[x][y + 1] in [0, 9]  for x, y in self.play_pos): 
                self.limpar_tela()
               
                for o in self.play_pos:
                    self.matriz[o[0]][o[1] + 1] = 9
            else:
                self.ja_colidiu = True
                ids = self.obigeto[self.celecionado][0][0]
                ids = ids.find('p')
                
                for x,y in self.play_pos:
                    self.matriz[x][y] = int(self.obigeto[self.celecionado][0][0][1:ids])
                
                self.rotacao = 0 
                self.novo_bloco()
        except IndexError:
            pass
            
    def update(self):
        
        canvas.delete('o')
        if not self.ja_colidiu:
            self.play_pos.clear()
        
        self.delei += 1
        
        # decer linha que esta fultuando
        if self.pontos_deletado != list():
            y = self.pontos_deletado[0]
            print(self.pontos_deletado[-1])
            self.pontos_deletado.pop(0)
            for menos in range(self.tamnho_y):
                for x in range(self.tamnho_x):
                
                    if self.matriz[x][y - menos] not in [0, 9]:
                        obig = self.matriz[x][y- menos]
                        self.matriz[x][y-menos] = 0
                        print(menos)
                        self.matriz[x][(y - menos) + 1] = obig
                        

        for pos_x, i in enumerate(self.matriz):
            
            for pos_y, e in enumerate(i):
              
                if e == 9:
                    self.play_pos.append([pos_x, pos_y])
                    self.play_pos.sort()
                elif e != 0:
                    
                    canvas.create_rectangle(pos_x * 10, pos_y * 10 , pos_x * 10 + 10, pos_y * 10 + 10, fill=self.cores.get(e, '#FF00A2'), tags='o')
                
                if all(self.matriz[x][pos_y] not in [0, 9] for x in range(self.tamnho_x)):
                    for x in range(self.tamnho_x):
                        self.matriz[x][pos_y] = 0
                    self.pontos_deletado.append(pos_y)
           
        self.lista.reverse()
        if len(self.lista) > 1:
            for e, x, y in self.lista:
                if y +1 <= self.tamnho_y -1:
                    
                    self.matriz[x][y] = 0
                    self.matriz[x][y + 1] = e
                    
               
        if self.poder_cair >= 15:
            self.poder_cair = 0
            self.cair_bloco()
        else:
            self.poder_cair += 1
            
        for x, y in self.play_pos:

            x *= 10
            y *= 10
            e = int(str(self.obigeto[self.celecionado][0][0]).split("p")[0][1:])
            
            
            canvas.create_rectangle(x, y, x + 10, y + 10, fill=self.cores.get(e, '#FF00A2'), tags='o')
        if not self.reboot_on:
            janela.after(1000//60, self.update)
        
    def limpar_tela(self):
         contagem = 0
         for pos_x, coluna in enumerate(self.matriz):
                for pos_y, bloco in enumerate(coluna):
                    if bloco == 9:
                        contagem += 1
                        self.matriz[pos_x][pos_y] = 0
                        
                    elif contagem >= 4:
                        return None
        
    def novo_bloco(self):
       
        self.ja_colidiu = False
        self.limpar_tela()
        self.celecionado = ''
        if self.matriz[10][0] not in [0,9]:
            self.reboot_on = True
            self.reboot()
            return
        for letra in self.obigeto.keys():
            self.celecionado += letra

        self.celecionado = choice(self.celecionado)
        for o in self.obigeto[self.celecionado][self.rotacao]:
            self.matriz[10 + int(o[-2])][int(o[-1])] = 9
            
    def reboot(self):
        self.reboot_on = False
        self.__init__()

if __name__ == "__main__":
    Game()
    
    janela.mainloop()
    
