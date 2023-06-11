from random import choice
import customtkinter as ctk


class janela(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global canvas
        self.title('tetris')
        self.rotacao = 0
        self.play_pos = list()
        self.poder_cair = 6
        # o = obijeto numero igual a cor, p = pos x 0 y 0
        self.obigeto = {'i': [['o2p00', 'o2p01', 'o2p02', 'o2p03']],
                        'j': [['o4p10', 'o4p11', 'o4p12', 'o4p02']],
                        'l': [['o6p00', 'o6p01', 'o6p02', 'o6p12']],
                        'o': [['o8p00', 'o8p01', 'o8p10', 'o08p11']],
                        's': [['o10p10', 'o10p20', 'o10p01', 'o10p11']],
                        't': [['o12p00', 'o12p10', 'o12p11', 'o12p20']],
                        'z': [['o14p00', 'o14p10', 'o14p11', 'o14p21']]
                        }

        canvas = ctk.CTkCanvas(self, width=200, height=400, bg='black')
        canvas.grid()

        self.grade = [list(0 for i in range(0, 40)) for i in range(0, 20)]
        self.novo_bloco(False)
        self.bind("<Key>", self.inputs)
        self.after(2000 // 5, self.update)

    def inputs(self, key):
        
        if key.keycode == 114 and all(x < len(self.grade) - 1 for x, y in self.play_pos):
            self.limpar_tela()
            for o in self.obigeto[self.celecionado][self.rotacao]:
                            self.grade[int(o[-2]) + self.play_pos[0][0] + 1
                                       ][self.play_pos[0][1] + int(o[-1])] = 9
        elif key.keycode == 113 and all(x > 0  for x, y in self.play_pos):
            self.limpar_tela()
            for o in self.obigeto[self.celecionado][self.rotacao]:
                self.grade[int(o[-2]) + self.play_pos[0][0] - 1
                           ][self.play_pos[0][1] + int(o[-1])] = 9

    def cair_bloco(self):
        
        if all(y < len(self.grade[0]) - 1 for x, y in self.play_pos):
            self.limpar_tela()
            
            for o in self.obigeto[self.celecionado][self.rotacao]:
                self.grade[int(o[-2]) + self.play_pos[0][0]
                           ][self.play_pos[0][1] + int(o[-1]) + 1] = 9
        else:
            pass

    def update(self):

        canvas.delete('o')
        self.play_pos.clear()

        for pos_x, i in enumerate(self.grade):

            for pos_y, e in enumerate(i):
                if e == 9:
                    self.play_pos.append([pos_x, pos_y])
                    self.play_pos.sort()
        if self.poder_cair >= 15:
            self.cair_bloco()
            self.poder_cair = 0
        else:
            self.poder_cair += 1
        for x, y in self.play_pos:

            x *= 10
            y *= 10

            canvas.create_rectangle(x, y, x + 10, y + 10, fill='red', tags='o')

        self.after(1000//60, self.update)
        
    def limpar_tela(self):
         contagem = 0
         for pos_x, coluna in enumerate(self.grade):
                for pos_y, bloco in enumerate(coluna):
                    if bloco == 9:
                        contagem += 1
                        self.grade[pos_x][pos_y] = 0

                    elif contagem >= 4:
                        return None
        
    def novo_bloco(self, ja_iniciado=True):
       
        if ja_iniciado:
           self.limpar_tela()
           
        self.celecionado = ''
        for letra in self.obigeto.keys():
            self.celecionado += letra

        self.celecionado = choice(self.celecionado)
        for o in self.obigeto[self.celecionado][self.rotacao]:
            self.grade[10 + int(o[-2])][int(o[-1])] = 9


if __name__ == "__main__":
    janela().mainloop()
