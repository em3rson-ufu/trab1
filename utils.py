# utils.py
# Funcoes auxiliares para leitura e validacao de entrada do usuario.

def ler_inteiro(mensagem, minimo=None, maximo=None):
    # Le um inteiro e repete ate o valor ser valido.
    # Se minimo/maximo forem informados, respeita esses limites.
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print("  Valor deve ser >= %d." % minimo)
                continue
            if maximo is not None and valor > maximo:
                print("  Valor deve ser <= %d." % maximo)
                continue
            return valor
        except ValueError:
            print("  Entrada invalida. Digite um numero inteiro.")


def ler_texto(mensagem, obrigatorio=True):
    # Le uma string. Se obrigatorio=True, rejeita campo vazio.
    while True:
        valor = input(mensagem).strip()
        if not valor and obrigatorio:
            print("  Este campo nao pode ficar vazio.")
            continue
        return valor


def escolher_opcao(mensagem, opcoes):
    # Mostra um menu numerado a partir do dicionario recebido
    # e devolve a chave escolhida.
    print(mensagem)
    for chave, valor in opcoes.items():
        print("  [%d] %s" % (chave, valor))
    return ler_inteiro("  Escolha: ", min(opcoes), max(opcoes))


def pausar():
    # Pausa para o usuario ler antes do menu voltar.
    input("\n  Pressione ENTER para continuar...")