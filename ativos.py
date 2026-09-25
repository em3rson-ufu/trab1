# ativos.py
# CRUD de ativos de TI.

from utils import ler_inteiro, ler_texto, escolher_opcao, pausar
from enums import TIPOS_ATIVO
from persistencia import salvar_ativos, salvar_vulns


def _proximo_id(ativos):
    # Retorna o maior id existente + 1, garantindo id unico.
    return max(ativos.keys(), default=0) + 1


def _exibir_ativo(ativo, vulns):
    # Mostra os dados de um ativo na tela.
    print()
    print("  ID........: %d" % ativo["id"])
    print("  Nome......: %s" % ativo["nome"])
    print("  Responsavel: %s" % ativo["responsavel"])
    print("  Setor.....: %s" % ativo["setor"])
    print("  Tipo......: %s" % TIPOS_ATIVO.get(ativo["tipo"], "?"))

    qtd = 0
    for v in vulns.values():
        if v["id_ativo"] == ativo["id"]:
            qtd += 1
    print("  Vulnerabilidades: %d" % qtd)


def cadastrar_ativo(ativos, vulns):
    # Cadastra um ativo novo com id gerado automaticamente.
    print("\n--- CADASTRAR ATIVO ---")
    id_ativo = _proximo_id(ativos)
    nome = ler_texto("  Nome / hostname: ")
    responsavel = ler_texto("  Responsavel: ")
    setor = ler_texto("  Setor: ")
    tipo = escolher_opcao("  Tipo de ativo:", TIPOS_ATIVO)

    ativos[id_ativo] = {
        "id": id_ativo,
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo,
    }
    salvar_ativos(ativos)
    print("\n  Ativo #%d cadastrado." % id_ativo)

    resp = input("  Deseja cadastrar vulnerabilidades agora? (s/n): ").lower()
    if resp == "s":
        from vulnerabilidades import cadastrar_vuln
        while True:
            cadastrar_vuln(vulns, id_ativo)
            if input("  Cadastrar outra? (s/n): ").lower() != "s":
                break
    pausar()


def consultar_ativo(ativos, vulns):
    # Busca um ativo por id ou por nome.
    print("\n--- CONSULTAR ATIVO ---")
    print("  [1] Buscar por ID")
    print("  [2] Buscar por nome/hostname")
    opcao = ler_inteiro("  Escolha: ", 1, 2)

    if opcao == 1:
        id_busca = ler_inteiro("  ID do ativo: ", 1)
        ativo = ativos.get(id_busca)
        if ativo:
            _exibir_ativo(ativo, vulns)
        else:
            print("  Ativo nao encontrado.")
    else:
        termo = ler_texto("  Nome/hostname (parcial): ").lower()
        achou = False
        for a in ativos.values():
            if termo in a["nome"].lower():
                _exibir_ativo(a, vulns)
                achou = True
        if not achou:
            print("  Nenhum ativo encontrado.")
    pausar()


def atualizar_ativo(ativos, vulns):
    # Altera dados de um ativo. ENTER vazio mantem o valor atual.
    print("\n--- ATUALIZAR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", 1)
    ativo = ativos.get(id_ativo)
    if not ativo:
        print("  Ativo nao encontrado.")
        pausar()
        return

    _exibir_ativo(ativo, vulns)
    print("\n  Deixe em branco para manter o valor atual.")

    novo_nome = ler_texto("  Nome [%s]: " % ativo["nome"], obrigatorio=False)
    novo_resp = ler_texto("  Responsavel [%s]: " % ativo["responsavel"], obrigatorio=False)
    novo_setor = ler_texto("  Setor [%s]: " % ativo["setor"], obrigatorio=False)

    if novo_nome:
        ativo["nome"] = novo_nome
    if novo_resp:
        ativo["responsavel"] = novo_resp
    if novo_setor:
        ativo["setor"] = novo_setor

    if input("  Alterar tipo? (s/n): ").lower() == "s":
        ativo["tipo"] = escolher_opcao("  Novo tipo:", TIPOS_ATIVO)

    salvar_ativos(ativos)
    print("  Ativo atualizado.")
    pausar()


def deletar_ativo(ativos, vulns):
    # Remove o ativo e tambem as vulnerabilidades ligadas a ele.
    print("\n--- DELETAR ATIVO ---")
    id_ativo = ler_inteiro("  ID do ativo: ", 1)
    if id_ativo not in ativos:
        print("  Ativo nao encontrado.")
        pausar()
        return

    _exibir_ativo(ativos[id_ativo], vulns)
    if input("  Confirma exclusao? (s/n): ").lower() != "s":
        print("  Operacao cancelada.")
        pausar()
        return

    # Remove primeiro as vulnerabilidades do ativo.
    remover = []
    for vid, v in vulns.items():
        if v["id_ativo"] == id_ativo:
            remover.append(vid)
    for vid in remover:
        del vulns[vid]

    del ativos[id_ativo]
    salvar_ativos(ativos)
    salvar_vulns(vulns)
    print("  Ativo e %d vulnerabilidade(s) removidos." % len(remover))
    pausar()