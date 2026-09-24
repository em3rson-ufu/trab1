"""
Persistência simples em arquivos de texto.
Requisito 3: dados gravados em arquivo de texto.
"""

import os

DIR_DADOS = "dados"
ARQ_ATIVOS = os.path.join(DIR_DADOS, "ativos.txt")
ARQ_VULNS = os.path.join(DIR_DADOS, "vulnerabilidades.txt")

# Separador de campos: ';'  |  Separador interno: '|'
SEP_CAMPO = ";"
SEP_LISTA = "|"


def garantir_diretorio():
    os.makedirs(DIR_DADOS, exist_ok=True)
    for arq in (ARQ_ATIVOS, ARQ_VULNS):
        if not os.path.exists(arq):
            with open(arq, "w", encoding="utf-8") as f:
                pass


def salvar_ativos(ativos: dict):
    """Salva o dicionário de ativos no arquivo."""
    garantir_diretorio()
    with open(ARQ_ATIVOS, "w", encoding="utf-8") as f:
        for ativo in ativos.values():
            linha = SEP_CAMPO.join([
                str(ativo["id"]),
                ativo["nome"],
                ativo["responsavel"],
                ativo["setor"],
                ativo["localizacao"],
                str(ativo["tipo"]),
            ])
            f.write(linha + "\n")


def carregar_ativos() -> dict:
    """Carrega ativos do arquivo para um dicionário indexado por ID (req. 9)."""
    garantir_diretorio()
    ativos = {}
    with open(ARQ_ATIVOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(SEP_CAMPO)
            if len(partes) != 6:
                continue
            ativo = {
                "id": int(partes[0]),
                "nome": partes[1],
                "responsavel": partes[2],
                "setor": partes[3],
                "localizacao": partes[4],
                "tipo": int(partes[5]),
            }
            ativos[ativo["id"]] = ativo
    return ativos


def salvar_vulns(vulns: dict):
    garantir_diretorio()
    with open(ARQ_VULNS, "w", encoding="utf-8") as f:
        for v in vulns.values():
            linha = SEP_CAMPO.join([
                str(v["id"]),
                str(v["id_ativo"]),
                v["descricao"],
                str(v["categoria"]),
                str(v["severidade"]),
                str(v["status"]),
            ])
            f.write(linha + "\n")


def carregar_vulns() -> dict:
    garantir_diretorio()
    vulns = {}
    with open(ARQ_VULNS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(SEP_CAMPO)
            if len(partes) != 6:
                continue
            v = {
                "id": int(partes[0]),
                "id_ativo": int(partes[1]),
                "descricao": partes[2],
                "categoria": int(partes[3]),
                "severidade": int(partes[4]),
                "status": int(partes[5]),
            }
            vulns[v["id"]] = v
    return vulns