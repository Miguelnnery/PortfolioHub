from poo_bank import Fisica
from poo_bank import Jurdica
if __name__=='__main__':
    p1 = Fisica('Judite',90000,983645745-00,'f')
    p2 = Fisica('João',80000)
    p3 = Fisica('Inde')
    p4 = Jurdica('Bauducco',5000000, 'LTDA', 93127312-22)
    p5 = Jurdica('Bradesco',600000,'LTDA')
    p6 = Jurdica('BomColchao')


    print(f'{p1.show_fis()}')

    print(f'Saldo: {p2.get_saldo()}')
    
    p3.set_nome('Inguana')
    

    print(f'Nome mudado com sucesso: {p3.get_nome()}')

    print(f'{p4.show_jur()}')

    p5.set_tipo('ME')

    p6.set_nome ('BomColchões')


    print(f'Modalidade mudada com sucesso: {p5.get_tipo()}')

    print(f'Nome mudado com sucesso: {p6.get_nome()}')

