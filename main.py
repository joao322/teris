
import customtkinter as ctk


class janela(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global canvas
        self.title('calculadora')
        self.rotacao = 0
        linha = list(0 for i in range(0, 40))
        self.grade = [linha.copy()  for i in range(0, 20)] 
        
        # o = obijeto codigo apenas numero par, p = pos x 0 y 0
        self.obigeto_i = [['o2p00', 'o2p01', 'o2p02', 'o2p03']]
        self.obigeto_j = [['o4p10', 'o4p11', '04p12', '04p02']]
        self.obigeto_l = [['o6p00', 'o6p01', '06p02', '06p12']]
        self.obigeto_o = [['o8p00', 'o8p01', 'o8p10', 'o8p11']]
        '''self.obigeto_s
        self.obigeto_t
        self.obigeto_z'''



        self.y = 0
        canvas = ctk.CTkCanvas(self, width=200, height=400, bg='black')
        canvas.grid()
        self.add_obigeto()

        self.after(1000//5, self.update)
        
    def update(self):
        n1 = 200 / len(self.grade)
        n2 = 400 / len(self.grade[-1])

        canvas.delete('o')
        self.inicio = 0
        self.inicio_x = 0
        if self.y + int(self.obigeto_i[0][-1][-1]) * 10 + 10 < 400:
            self.y += 1
        for pos_x, i in enumerate(self.grade):
            for pos, e in enumerate(i):
                if e == 'p':
                    self.inicio = pos
                    self.inicio_x = pos_x
                    break
            if self.inicio > 0:
                break
        
        for obijeto in self.obigeto_i[self.rotacao]:
            
            canvas.create_rectangle((self.inicio_x + int(obijeto[-2])) * n1, (self.inicio + int(obijeto[-1])) * n1  + self.y, (self.inicio_x + int(obijeto[-2])) * n1 + n1, (self.inicio + int(obijeto[-1])) * n1 + self.y + n1, fill='red', tags='o')

        self.after(1000//60, self.update)
    def add_obigeto(self):
        self.grade[10].pop(0)
        self.grade[10].insert(0, 'p') 
        

if __name__ == "__main__":
    janela().mainloop()
