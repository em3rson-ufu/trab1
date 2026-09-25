# Sistema de Ativos de TI

Trabalho de Ciberseguranca (UFU) - Sprints 1 e 2 - 2026/2.

Programa em Python para cadastrar ativos de TI e as vulnerabilidades
associadas a eles. Permite cadastrar, consultar, atualizar e remover
os registros (CRUD).

## Como executar

Precisa do Python 3.8 ou superior. Nenhuma dependencia externa.

    python main.py

## Estrutura

- main.py              menu principal
- ativos.py            CRUD de ativos
- vulnerabilidades.py  CRUD de vulnerabilidades
- persistencia.py      gravacao em arquivos de texto
- utils.py             validacao de entrada
- enums.py             constantes
- relatorio.py         relatorio na tela
- testes.py            testes basicos

## Arquivos de dados

Os arquivos ficam na pasta `dados/`, criada automaticamente na
primeira execucao:

- `dados/ativos.txt`
- `dados/vulnerabilidades.txt`

Cada arquivo usa `;` como separador de campos.

## Requisitos atendidos

1. Menu textual com tratamento de erros
2. Pelo menos 4 categorias de ativos (tem 8)
3. Cadastro de ativo com id unico
4. Busca por id ou nome
5. Atualizacao de ativo
6. Remocao de ativo junto com suas vulnerabilidades
7. Cadastro de vulnerabilidades
8. Visualizacao de vulnerabilidades por ativo
9. Uso de dicionario indexado por id
10. Versionamento no GitHub com branches

## Testes

    python testes.py

## Autor

    Émerson André Unfried
