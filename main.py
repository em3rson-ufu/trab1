# main.py
# Programa principal: menu e loop de execucao.

from persistencia import carregar_ativos, carregar_vulns, garantir_diretorio
from ativos import cadastrar_ativo, consultar_ativo, atualizar_ativo, deletar_ativo
from vulnerabilidades import cadastrar_vuln_existente, listar_vulns_por_ativo
from relatorio import exibir_relatorio


def exibir_menu():
    # Imprime o menu principal na tela.
    print()
    print("=" * 50)
    print("  SISTEMA DE ATIVOS E VULNERABILIDADES")
    print("=" * 50)
    print("  [1] Cadastrar ativo")
    print("  [2] Consultar ativo")
    print("  [3] Atualizar ativo")
    print("  [4] Deletar ativo")
    print("  [5] Cadastrar vulnerabilidade em ativo")
    print("  [6] Ver vulnerabilidades de um ativo")
    print("  [7] Exibir relatorio")
    print("  [0] Sair")
    print("=" * 50)


def main():
    # Carrega os dados e roda o menu ate o usuario sair.
    garantir_diretorio()
    ativos = carregar_ativos()
    vulns = carregar_vulns()

    while True:
        exibir_menu()
        try:
            opcao = int(input("  Escolha uma opcao: ").strip())
        except ValueError:
            print("  Digite um numero valido.")
            continue

        if opcao == 1:
            cadastrar_ativo(ativos, vulns)
        elif opcao == 2:
            consultar_ativo(ativos, vulns)
        elif opcao == 3:
            atualizar_ativo(ativos, vulns)
        elif opcao == 4:
            deletar_ativo(ativos, vulns)
        elif opcao == 5:
            cadastrar_vuln_existente(ativos, vulns)
        elif opcao == 6:
            listar_vulns_por_ativo(ativos, vulns)
        elif opcao == 7:
            exibir_relatorio(ativos, vulns)
        elif opcao == 0:
            print("\n  Encerrando.")
            break
        else:
            print("  Opcao invalida.")


main()