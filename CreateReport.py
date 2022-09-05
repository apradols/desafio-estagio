from datetime import datetime
import babel.numbers
from utils.enum import tableG029
from utils.mask_cnpj import mask_cnpj

class CreateReport:
    def __init__(self, list_registro_detalhe, header_lote, header_arquivo, file_export):
        self.list_details_registry = list_registro_detalhe
        self.header_lote = header_lote
        self.header_arquivo = header_arquivo
        self.file_export = file_export

    def generateByExtension(self):
        if self.file_export[-4::] == 'txt' :
            print(f'Gerando relatório: {self.file_export}')
            self.generate_txt_report()


    def generate_txt_report(self):
        f   = open(self.file_export,"w+")

        f.write('------------------------------------------------------------------------------------------------------------------------------------------------------------ \n')
        f.write('Nome da Empresa | Numero de Inscricao da Empresa | Nome do Banco | Nome da Rua        | Numero do Local | Nome da Cidade       | CEP       | Sigla do Estado \n')
        f.write('------------------------------------------------------------------------------------------------------------------------------------------------------------ \n')
        f.write(f'{self.header_arquivo[72:102].rstrip()}   | {mask_cnpj(self.header_arquivo[18:32]).rstrip()}             | {self.header_arquivo[102:132].rstrip()}          | {self.header_lote[142:172].rstrip()} | {self.header_lote[172:177].rstrip()}             | {self.header_lote[192:212].rstrip()} | {self.header_lote[212:217].rstrip()}-{self.header_lote[217:220].rstrip()} | {self.header_lote[220:222].rstrip()} \n')
        f.write('------------------------------------------------------------------------------------------------------------------------------------------------------------ \n')
        f.write('-------------------------------------------------------------------------------------------------------------------------------------- \n')
        f.write('Nome do Favorecido   | Data de Pagamento | Valor do Pagamento | Numero do Documento Atribuido pela Empresa | Forma de Lancamento \n')
        f.write('-------------------------------------------------------------------------------------------------------------------------------------- \n')

        for registry in self.list_details_registry:
            price = registry[119:134]
            price_spaces = babel.numbers.format_currency(price[:13] + '.' + price[13:], 'BRL', locale='pt_BR') + (' ' * (19-len(babel.numbers.format_currency(price[:13] + '.' + price[13:], 'BRL', locale='pt_BR'))))
            csv_registry = f'''{registry[43:73].rstrip()} | {datetime(int(registry[97:101]), int(registry[95:97]), int(registry[93:95])).strftime('%d/%m/%Y').rstrip()}        | {price_spaces}| {registry[73:93].rstrip()}                                 | {tableG029[self.header_lote[11:13]]} \n'''
            f.write(csv_registry)

        f.write('-------------------------------------------------------------------------------------------------------------------------------------- \n')
        f.close()