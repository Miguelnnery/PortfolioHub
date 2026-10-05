class Conta:
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo
    

    def get_nome(self):
        return self.nome

    def get_saldo(self):
        return self.saldo

    def set_nome(self,nv_nome):
        self.nome= nv_nome



class Fisica(Conta):
    def __init__(self, nome,saldo = 0.0, cpf=0 ,genero='',):
        super().__init__(nome, saldo)
    
        self.gene = genero
        self.cpf = cpf
    def get_gen(self):
        return self.gene
    
    def set_gen(self,nv_gene):
        self.gene = nv_gene

    def show_fis(self):
        return (f'''
    Nome:   {self.nome}
    Saldo:  {self.saldo}
    CPF:    {self.cpf}
    Gênero: {self.gene}

        ''')

class Jurdica(Conta):
    def __init__(self, nome ,saldo = 0.0, tipo = '',cnpj=0):
        super().__init__(nome, saldo)
    
        self.tipo = tipo
        self.cnpj = cnpj
    
    def get_tipo(self):
        return self.tipo
    
    def get_cnpj(self):
        return self.cnpj
    
    def set_tipo(self,nv_tipo):
        self.tipo = nv_tipo
    
    def show_jur(self):
        return (f''' 

    Nome:   {self.nome}
    Saldo:  {self.saldo}
    Tipo:   {self.tipo}
    CNPJ:   {self.cnpj}
        ''')



