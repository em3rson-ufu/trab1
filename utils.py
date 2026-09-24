"""
Funções auxiliares: validação de entrada, leitura segura, etc.
Requisito 1: tratamento de erros.
"""


def ler_inteiro(mensagem: str, minimo: int = None, maximo: int = None) -> int:
    """Lê um inteiro do usuário, tratando erros e limites."""
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"  [!] Valor deve ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  [!] Valor deve ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("  [!] Entrada inválida. Digite um número inteiro.")


def ler_texto(mensagem: str, obrigatorio: bool = True) -> str:
    """Lê uma string não vazia (se obrigatório)."""
    while True:
        valor = input(mensagem).strip()
        if not valor and obrigatorio:
            print("  [!] Este campo não pode ficar vazio.")
            continue
        return valor


def escolher_opcao(mensagem: str, opcoes: dict) -> int:
    """Mostra um dicionário de opções e retorna a chave escolhida."""
    print(mensagem)
    for chave, valor in opcoes.items():
        print(f"  [{chave}] {valor}")
    return ler_inteiro("  Escolha: ", minimo=min(opcoes), maximo=max(opcoes))


def pausar():
    input("\n  Pressione ENTER para continuar...")