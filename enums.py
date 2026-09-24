"""
Módulo com enumerações e constantes do sistema.
Usamos dicionários (dict) como estruturas base conforme requisito 9.
"""

# Requisito 2: pelo menos 4 categorias de ativos de TI
TIPOS_ATIVO = {
    1: "Notebook",
    2: "Servidor",
    3: "Roteador",
    4: "Software Licenciado",
    5: "Aplicação Web",
    6: "Banco de Dados",
    7: "Estação de Trabalho",
    8: "Impressora de Rede",
}

SEVERIDADES = {
    1: "Baixa",
    2: "Média",
    3: "Alta",
    4: "Crítica",
}

STATUS_VULN = {
    1: "Aberta",
    2: "Em tratamento",
    3: "Corrigida",
    4: "Aceita como risco",
}

CATEGORIAS_VULN = {
    1: "Falha de configuração",
    2: "Ausência de atualização",
    3: "Senha fraca",
    4: "Exposição indevida de serviço",
    5: "Software desatualizado",
    6: "Permissão de acesso inadequada",
}