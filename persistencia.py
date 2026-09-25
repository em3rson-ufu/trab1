# persistencia.py
# Leitura e gravacao dos dados em arquivos de texto.

import os

DIR_DADOS = "dados"
ARQ_ATIVOS = os.path.join(DIR_DADOS, "ativos.txt")
ARQ_VULNS = os.path.join(DIR_DADOS, "vulnerabilidades.txt")

SEP = ";"


def garantir_diretorio():
    # Cria a pasta e os arquivos caso nao existam ainda.
    os.makedirs(DIR_DADOS, exist_ok=True)
    for arq in (ARQ_ATIVOS, ARQ_VULNS):
        if not os.path.exists(arq):
            open(arq, "w", encoding="utf-8").close()


def salvar_ativos(ativos):
    # Reescreve o arquivo inteiro com o conteudo atual do dicionario.
    garantir_diretorio()
    with open(ARQ_ATIVOS, "w", encoding="utf-8") as f:
        for a in ativos.values():
            linha = SEP.join([
                str(a["id"]),
                a["nome"],
                a["responsavel"],
                a["setor"],
                str(a["tipo"]),
            ])
            f.write(linha + "\n")


def carregar_ativos():
    # Le o arquivo e monta o dicionario indexado por id.
    garantir_diretorio()
    ativos = {}
    with open(ARQ_ATIVOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            p = linha.split(SEP)
            # Formato: id;nome;responsavel;setor;tipo
            if len(p) != 5:
                continue
            ativos[int(p[0])] = {
                "id": int(p[0]),
                "nome": p[1],
                "responsavel": p[2],
                "setor": p[3],
                "tipo": int(p[4]),
            }
    return ativos


def salvar_vulns(vulns):
    # Grava as vulnerabilidades no arquivo.
    garantir_diretorio()
    with open(ARQ_VULNS, "w", encoding="utf-8") as f:
        for v in vulns.values():
            linha = SEP.join([
                str(v["id"]),
                str(v["id_ativo"]),
                v["descricao"],
                str(v["categoria"]),
                str(v["severidade"]),
                str(v["status"]),
            ])
            f.write(linha + "\n")


def carregar_vulns():
    # Le o arquivo e devolve o dicionario indexado por id.
    garantir_diretorio()
    vulns = {}
    with open(ARQ_VULNS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            p = linha.split(SEP)
            # Formato: id;id_ativo;descricao;categoria;severidade;status
            if len(p) != 6:
                continue
            vulns[int(p[0])] = {
                "id": int(p[0]),
                "id_ativo": int(p[1]),
                "descricao": p[2],
                "categoria": int(p[3]),
                "severidade": int(p[4]),
                "status": int(p[5]),
            }
    return vulns