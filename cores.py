"""
============================================================
MÓDULO: cores.py
============================================================
Formatação do terminal com códigos ANSI.

Recursos:
    - Paleta de cores e estilos.
    - Funções semânticas (titulo, sucesso, erro, aviso).
    - Colorização condicional por severidade e status.
    - Modo seguro: respeita a variável de ambiente NO_COLOR.

Referência: https://no-color.org
============================================================
"""

import os

# Se NO_COLOR estiver definida no ambiente, desativa as cores.
USAR_CORES = os.environ.get("NO_COLOR") is None


def _aplicar(codigo: str, texto: str) -> str:
    """Aplica um código ANSI ao texto (ou devolve sem cor)."""
    if not USAR_CORES:
        return texto
    return f"{codigo}{texto}\033[0m"


# ------------------------------------------------------------
# Estilos
# ------------------------------------------------------------
def negrito(texto: str) -> str:
    return _aplicar("\033[1m", texto)


def sublinhado(texto: str) -> str:
    return _aplicar("\033[4m", texto)


# ------------------------------------------------------------
# Cores básicas
# ------------------------------------------------------------
def vermelho(texto: str) -> str:
    return _aplicar("\033[91m", texto)


def verde(texto: str) -> str:
    return _aplicar("\033[92m", texto)


def amarelo(texto: str) -> str:
    return _aplicar("\033[93m", texto)


def azul(texto: str) -> str:
    return _aplicar("\033[94m", texto)


def magenta(texto: str) -> str:
    return _aplicar("\033[95m", texto)


def ciano(texto: str) -> str:
    return _aplicar("\033[96m", texto)


def cinza(texto: str) -> str:
    return _aplicar("\033[90m", texto)


# ------------------------------------------------------------
# Helpers semânticos
# ------------------------------------------------------------
def titulo(texto: str) -> str:
    """Título de seção — azul negrito."""
    return _aplicar("\033[1;94m", texto)


def sucesso(texto: str) -> str:
    """Mensagem [OK] — verde."""
    return _aplicar("\033[92m", texto)


def erro(texto: str) -> str:
    """Mensagem [!] — vermelho."""
    return _aplicar("\033[91m", texto)


def aviso(texto: str) -> str:
    """Mensagem de aviso — amarelo."""
    return _aplicar("\033[93m", texto)


def rotulo(texto: str) -> str:
    """Rótulo de campo — ciano."""
    return _aplicar("\033[96m", texto)


def valor(texto: str) -> str:
    """Valor de campo — branco."""
    return _aplicar("\033[97m", texto)


def linha_divisoria(tamanho: int = 50) -> str:
    """Linha decorativa '═' — azul."""
    return _aplicar("\033[94m", "═" * tamanho)


def cor_por_severidade(severidade: int, texto: str) -> str:
    """
    Colore conforme severidade:
        1=Baixa (verde), 2=Média (amarelo),
        3=Alta (laranja), 4=Crítica (vermelho negrito).
    """
    if severidade == 1:
        return _aplicar("\033[92m", texto)
    if severidade == 2:
        return _aplicar("\033[93m", texto)
    if severidade == 3:
        return _aplicar("\033[38;5;208m", texto)   # laranja (256 cores)
    if severidade == 4:
        return _aplicar("\033[1;91m", texto)       # vermelho negrito
    return texto


def cor_por_status(status: int, texto: str) -> str:
    """
    Colore conforme status:
        1=Aberta (vermelho), 2=Em tratamento (amarelo),
        3=Corrigida (verde), 4=Aceita (cinza).
    """
    if status == 1:
        return _aplicar("\033[91m", texto)
    if status == 2:
        return _aplicar("\033[93m", texto)
    if status == 3:
        return _aplicar("\033[92m", texto)
    if status == 4:
        return _aplicar("\033[90m", texto)
    return texto