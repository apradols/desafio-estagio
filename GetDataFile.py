class GetDataFile:
    def __init__(self, filepath):
        self.filepath = filepath

    def getData(self):
        print('Abrindo o arquivo')
        arquivo = open(self.filepath, 'r')

        arquivo_string = arquivo.read()
        arquivo.close()

        data = arquivo_string.split("\n")

        return data

