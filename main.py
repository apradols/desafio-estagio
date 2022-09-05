import sys
from GetDataFile import *
from CreateReport import *


def main():

    file_import = sys.argv[1]
    file_export = sys.argv[2]

    data_file = GetDataFile(file_import)

    data = data_file.getData()
    list_registro_detalhe = []
    header_lote = ''
    header_arquivo = ''
    print('Obtendo as linhas do arquivo lido')
    for line in data:
        if len(line) > 1:
            if line[7] == '0':
                header_arquivo = line
            elif line[7] == '1':
                header_lote = line
            elif line[7] == '3':
                list_registro_detalhe.append(line)
            elif line[7] == '5':
                trailer_lote = line
            elif line[7] == '9':
                trailer_arquivo = line
            else:
                print('Tipo de linha não mapeado')
        else:
            print('A linha não possui a quantidade de caracteres suficientes')

    create_report = CreateReport(list_registro_detalhe, header_lote, header_arquivo, file_export)
    create_report.generateByExtension()


if __name__ == "__main__":
    main()
