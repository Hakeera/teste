

try:
    file = open('abrir-arquivo.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
