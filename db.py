def ler():
    leitura = open("pasta.txt", "r", encoding='utf-8')
    leitura = leitura.read()
    leitura = leitura.split('\n')
    albuns = []
    for i in leitura:
        albuns.append(i.split('|'))
    albuns.pop()
    return albuns

def escrever(y):
    db = open('pasta.txt', 'a', encoding = "utf-8")
    db.write(y)
    db.close()