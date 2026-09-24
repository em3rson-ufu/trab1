"""
CRUD de vulnerabilidades (requisitos 7 e 8).
"""
from utils import ler_inteiro, ler_texto, escolher_opcao, pausar
from enums import SEVERIDADES, STATUS_VULN, CATEGORIAS_VULN
from persistencia import salvar_vulns


def _proximo_id_vuln(vulns: dict) -> int:
    return max(vulns.keys(), default=0) + 1


def cadastrar_vuln(vulns: dict, id_ativo: int):
    print(f"\n--- CADASTRAR VULNERABILIDADE (Ativo #{id_ativo}) ---")
    id_v = _proximo_id_vuln(vulns)
    descricao = ler_texto("  Descrição: ")
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
    print(f"  [OK] Vulnerabilidade #{id_v} cadastrada.")


def listar_vulns_por_ativo(ativos: dict, vulns: dict):
    print("\n--- VULNERABILIDADES POR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", minimo=1)
    if id_ativo not in ativos:
        print("  [!] Ativo não encontrado.")
        pausar()
        return

    print(f"\n  Ativo: {ativos[id_ativo]['nome']}")
    associadas = [v for v in vulns.values() if v["id_ativo"] == id_ativo]
    if not associadas:
        print("  Nenhuma vulnerabilidade registrada para este ativo.")
    else:
        for v in associadas:
            print(f"\n  #{v['id']}")
            print(f"    Descrição..: {v['descricao']}")
            print(f"    Categoria..: {CATEGORIAS_VULN.get(v['categoria'], '?')}")
            print(f"    Severidade.: {SEVERIDADES.get(v['severidade'], '?')}")
            print(f"    Status.....: {STATUS_VULN.get(v['status'], '?')}")
    pausar()