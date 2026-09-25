# relatorio.py
# Mostra na tela um relatorio dos ativos e suas vulnerabilidades.

from enums import TIPOS_ATIVO, SEVERIDADES, STATUS_VULN, CATEGORIAS_VULN
from utils import pausar


def _resumo(ativos, vulns):
    # Mostra os totais gerais.
    print()
    print("=" * 60)
    print("  RELATORIO DO INVENTARIO")
    print("=" * 60)
    print("  Total de ativos.........: %d" % len(ativos))
    print("  Total de vulnerabilidades: %d" % len(vulns))


def _lista_ativos(ativos, vulns):
    # Lista todos os ativos com contagem de vulnerabilidades.
    print()
    print("  ATIVOS CADASTRADOS")
    print("  " + "-" * 58)

    if not ativos:
        print("  Nenhum ativo cadastrado.")
        return

    print("  %-4s %-22s %-18s %-5s" % ("ID", "Nome", "Tipo", "Vulns"))
    print("  " + "-" * 58)

    for ativo in sorted(ativos.values(), key=lambda a: a["id"]):
        # Conta as vulns deste ativo.
        qtd = 0
        for v in vulns.values():
            if v["id_ativo"] == ativo["id"]:
                qtd += 1

        nome = ativo["nome"]
        if len(nome) > 22:
            nome = nome[:21] + "."

        tipo = TIPOS_ATIVO.get(ativo["tipo"], "?")
        print("  %-4d %-22s %-18s %-5d" % (ativo["id"], nome, tipo, qtd))


def _detalhes(ativos, vulns):
    # Mostra cada ativo e suas vulnerabilidades em detalhe.
    print()
    print("  DETALHAMENTO POR ATIVO")
    print("  " + "-" * 58)

    if not ativos:
        return

    for ativo in sorted(ativos.values(), key=lambda a: a["id"]):
        print()
        print("  #%d - %s" % (ativo["id"], ativo["nome"]))
        print("    Responsavel: %s" % ativo["responsavel"])
        print("    Setor......: %s" % ativo["setor"])
        print("    Tipo.......: %s" % TIPOS_ATIVO.get(ativo["tipo"], "?"))

        # Procura vulns deste ativo.
        achou = False
        for v in vulns.values():
            if v["id_ativo"] != ativo["id"]:
                continue

            if not achou:
                print("    Vulnerabilidades:")
                achou = True

            sev = SEVERIDADES.get(v["severidade"], "?")
            sta = STATUS_VULN.get(v["status"], "?")
            cat = CATEGORIAS_VULN.get(v["categoria"], "?")

            print("      #%d - %s" % (v["id"], v["descricao"]))
            print("        categoria: %s | severidade: %s | status: %s"
                  % (cat, sev, sta))

        if not achou:
            print("    Sem vulnerabilidades registradas.")


def exibir_relatorio(ativos, vulns):
    # Funcao principal chamada pelo menu.
    _resumo(ativos, vulns)
    _lista_ativos(ativos, vulns)
    _detalhes(ativos, vulns)

    print()
    print("=" * 60)
    pausar()