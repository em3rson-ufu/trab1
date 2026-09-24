"""
CRUD de ativos de TI (requisitos 3, 4, 5, 6).
"""
from utils import ler_inteiro, ler_texto, escolher_opcao, pausar
from enums import TIPOS_ATIVO
from persistencia import salvar_ativos


def _proximo_id(ativos: dict) -> int:
    """Gera um ID inteiro único (req. 3)."""
    return max(ativos.keys(), default=0) + 1


def cadastrar_ativo(ativos: dict, vulns: dict):
    print("\n--- CADASTRAR ATIVO ---")
    id_ativo = _proximo_id(ativos)
    nome = ler_texto("  Nome / hostname: ")
    responsavel = ler_texto("  Responsável: ")
    setor = ler_texto("  Setor: ")
    localizacao = ler_texto("  Localização: ")
    tipo = escolher_opcao("  Tipo de ativo:", TIPOS_ATIVO)

    ativos[id_ativo] = {
        "id": id_ativo,
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "localizacao": localizacao,
        "tipo": tipo,
    }
    salvar_ativos(ativos)
    print(f"\n  [OK] Ativo #{id_ativo} cadastrado com sucesso!")

    # Requisito 3: lista inicial de vulnerabilidades associadas
    if input("  Deseja cadastrar vulnerabilidades agora? (s/n): ").lower() == "s":
        from vulnerabilidades import cadastrar_vuln
        while True:
            cadastrar_vuln(vulns, id_ativo)
            if input("  Cadastrar outra vulnerabilidade? (s/n): ").lower() != "s":
                break
    pausar()


def _exibir_ativo(ativo: dict, vulns: dict):
    print(f"\n  ID........: {ativo['id']}")
    print(f"  Nome......: {ativo['nome']}")
    print(f"  Responsável: {ativo['responsavel']}")
    print(f"  Setor.....: {ativo['setor']}")
    print(f"  Localização: {ativo['localizacao']}")
    print(f"  Tipo......: {TIPOS_ATIVO.get(ativo['tipo'], '?')}")
    qtd = sum(1 for v in vulns.values() if v["id_ativo"] == ativo["id"])
    print(f"  Vulnerabilidades associadas: {qtd}")


def consultar_ativo(ativos: dict, vulns: dict):
    print("\n--- CONSULTAR ATIVO ---")
    print("  [1] Buscar por ID")
    print("  [2] Buscar por nome/hostname")
    opcao = ler_inteiro("  Escolha: ", minimo=1, maximo=2)

    if opcao == 1:
        id_busca = ler_inteiro("  ID do ativo: ", minimo=1)
        ativo = ativos.get(id_busca)
        if ativo:
            _exibir_ativo(ativo, vulns)
        else:
            print("  [!] Ativo não encontrado.")
    else:
        termo = ler_texto("  Nome/hostname (parcial): ").lower()
        encontrados = [a for a in ativos.values() if termo in a["nome"].lower()]
        if not encontrados:
            print("  [!] Nenhum ativo encontrado.")
        for a in encontrados:
            _exibir_ativo(a, vulns)
    pausar()


def atualizar_ativo(ativos: dict, vulns: dict):
    print("\n--- ATUALIZAR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", minimo=1)
    ativo = ativos.get(id_ativo)
    if not ativo:
        print("  [!] Ativo não encontrado.")
        pausar()
        return

    _exibir_ativo(ativo, vulns)
    print("\n  Deixe em branco para manter o valor atual.")
    novo_nome = ler_texto(f"  Nome [{ativo['nome']}]: ", obrigatorio=False)
    novo_resp = ler_texto(f"  Responsável [{ativo['responsavel']}]: ", obrigatorio=False)
    novo_setor = ler_texto(f"  Setor [{ativo['setor']}]: ", obrigatorio=False)
    nova_loc = ler_texto(f"  Localização [{ativo['localizacao']}]: ", obrigatorio=False)

    if novo_nome:
        ativo["nome"] = novo_nome
    if novo_resp:
        ativo["responsavel"] = novo_resp
    if novo_setor:
        ativo["setor"] = novo_setor
    if nova_loc:
        ativo["localizacao"] = nova_loc

    if input("  Alterar tipo? (s/n): ").lower() == "s":
        ativo["tipo"] = escolher_opcao("  Novo tipo:", TIPOS_ATIVO)

    salvar_ativos(ativos)
    print("  [OK] Ativo atualizado.")
    pausar()


def deletar_ativo(ativos: dict, vulns: dict):
    print("\n--- DELETAR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", minimo=1)
    if id_ativo not in ativos:
        print("  [!] Ativo não encontrado.")
        pausar()
        return

    _exibir_ativo(ativos[id_ativo], vulns)
    if input("  Confirma exclusão? (s/n): ").lower() != "s":
        print("  Operação cancelada.")
        pausar()
        return

    # Requisito 6: remover vulnerabilidades associadas
    ids_vulns_remover = [vid for vid, v in vulns.items() if v["id_ativo"] == id_ativo]
    for vid in ids_vulns_remover:
        del vulns[vid]

    del ativos[id_ativo]
    salvar_ativos(ativos)
    from persistencia import salvar_vulns
    salvar_vulns(vulns)

    print(f"  [OK] Ativo removido. {len(ids_vulns_remover)} vulnerabilidade(s) também removida(s).")
    pausar()