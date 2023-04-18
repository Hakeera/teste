with open('meu-arquivo.txt', 'w+', encoding='utf-8') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0, 0)
    print(file.read())