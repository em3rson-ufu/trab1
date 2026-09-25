# enums.py
# Constantes do sistema: tipos de ativo, severidades, status e categorias.
# Cada dicionario mapeia um codigo inteiro para o texto exibido no menu.

# Tipos de ativos de TI que podem ser cadastrados.
TIPOS_ATIVO = {
    1: "Notebook",
    2: "Servidor",
    3: "Roteador",
    4: "Software Licenciado",
    5: "Aplicacao Web",
    6: "Banco de Dados",
    7: "Estacao de Trabalho",
    8: "Impressora de Rede",
}

# Niveis de severidade de uma vulnerabilidade.
SEVERIDADES = {
    1: "Baixa",
    2: "Media",
    3: "Alta",
    4: "Critica",
}

# Situacao atual da vulnerabilidade.
STATUS_VULN = {
    1: "Aberta",
    2: "Em tratamento",
    3: "Corrigida",
    4: "Aceita como risco",
}

# Categorias para classificar a vulnerabilidade.
CATEGORIAS_VULN = {
    1: "Falha de configuracao",
    2: "Ausencia de atualizacao",
    3: "Senha fraca",
    4: "Exposicao indevida de servico",
    5: "Software desatualizado",
    6: "Permissao de acesso inadequada",
}