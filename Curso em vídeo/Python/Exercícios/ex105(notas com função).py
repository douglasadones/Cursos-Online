# Programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
# seguintes informações: 1) Quantidade de notas, 2) A maior nota, 3) A menor nota, 4) A média da turma,
# 4) A situação - BOM, RAZOÁVEL ou RUIM (Opcional).
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


# Programa Principal
resp = notas(9.5, 8.5, 7.5, sit=True)
print(resp)
help(notas)
