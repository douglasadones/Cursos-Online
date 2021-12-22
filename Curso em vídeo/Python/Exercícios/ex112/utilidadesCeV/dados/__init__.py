def leiaDinheiro(txt):
    info = str(input(txt)).strip()
    while True:
        if info.isnumeric():
            break
        elif info.isspace() or info.isalpha() or info in '' or info.isalnum():
            print(f'\033[1;31mERRO! "{info}" é um preço inválido!\033[m')
            info = str(input(txt)).strip()
        else:
            break
    info = info.replace(',', '.')
    info = float(info)
    return info
