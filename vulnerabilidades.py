# vulnerabilidades.py
# CRUD de vulnerabilidades associadas aos ativos.

from utils import ler_inteiro, ler_texto, escolher_opcao, pausar
from enums import SEVERIDADES, STATUS_VULN, CATEGORIAS_VULN
from persistencia import salvar_vulns


def _proximo_id(vulns):
    # Retorna o maior id existente + 1.
    return max(vulns.keys(), default=0) + 1


def cadastrar_vuln(vulns, id_ativo):
    # Cadastra UMA vulnerabilidade vinculada ao ativo informado.
    # Usada internamente por cadastrar_vuln_existente.
    print("\n--- CADASTRAR VULNERABILIDADE (Ativo #%d) ---" % id_ativo)
    id_v = _proximo_id(vulns)

    descricao = ler_texto("  Descricao: ")
    categoria = escolher_opcao("  Categoria:", CATEGORIAS_VULN)
    severidade = escolher_opcao("  Severidade:", SEVERIDADES)
    status = escolher_opcao("  Status:", STATUS_VULN)

    vulns[id_v] = {
        "id": id_v,
        "id_ativo": id_ativo,
        "descricao": descricao,
        "categoria": categoria,
        "severidade": severidade,
        "status": status,
    }
    salvar_vulns(vulns)
    print("  Vulnerabilidade #%d cadastrada." % id_v)


def cadastrar_vuln_existente(ativos, vulns):
    # Pede o ID de um ativo ja cadastrado e permite cadastrar
    # uma ou mais vulnerabilidades associadas a ele.
    print("\n--- CADASTRAR VULNERABILIDADE EM ATIVO ---")

    # Se nao ha ativos, avisa e volta ao menu.
    if not ativos:
        print("  Nenhum ativo cadastrado ainda.")
        print("  Cadastre um ativo primeiro (opcao 1 do menu).")
        pausar()
        return

    # Pede o id do ativo.
    id_ativo = ler_inteiro("  ID do ativo: ", 1)

    # Confere se o ativo existe.
    if id_ativo not in ativos:
        print("  Ativo nao encontrado.")
        pausar()
        return

    # Mostra o ativo escolhido para confirmacao.
    print("\n  Ativo: %s" % ativos[id_ativo]["nome"])
    print("  Setor: %s" % ativos[id_ativo]["setor"])

    # Loop para cadastrar varias vulns em sequencia.
    while True:
        cadastrar_vuln(vulns, id_ativo)
        if input("  Cadastrar outra? (s/n): ").lower() != "s":
            break

    pausar()


def listar_vulns_por_ativo(ativos, vulns):
    # Mostra todas as vulnerabilidades de um ativo.
    print("\n--- VULNERABILIDADES POR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", 1)

    if id_ativo not in ativos:
        print("  Ativo nao encontrado.")
        pausar()
        return

    print("\n  Ativo: %s" % ativos[id_ativo]["nome"])

    achou = False
    for v in vulns.values():
        if v["id_ativo"] == id_ativo:
            print()
            print("  #%d" % v["id"])
            print("    Descricao..: %s" % v["descricao"])
            print("    Categoria..: %s" % CATEGORIAS_VULN.get(v["categoria"], "?"))
            print("    Severidade.: %s" % SEVERIDADES.get(v["severidade"], "?"))
            print("    Status.....: %s" % STATUS_VULN.get(v["status"], "?"))
            achou = True

    if not achou:
        print("  Nenhuma vulnerabilidade registrada para este ativo.")
    pausar()