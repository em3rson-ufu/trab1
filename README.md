# Sistema de Ativos e Vulnerabilidades

Trabalho 01 de Ciberseguranca (UFU) - Sprints 1 e 2 - 2026/2.

Programa em Python para cadastrar ativos de TI e as vulnerabilidades
associadas a eles. Permite cadastrar, consultar, atualizar e remover
os registros (CRUD).

## Como executar

1. Abrir o VS Code
2. Abrir o Terminal Integrado do VS Code
```bash
Ctrl + '
```
3. Escolher onde Clonar (criar e navegar até a pasta desejada)
```bash
mkdir C:\Users\USUARIO\Pictures\trab1
```
```bash
cd C:\Users\USUARIO\Pictures\trab1
```
> Trocar `USUARIO` pelo usuário atual da máquina.
4. Clonar o Repositório
```bash
git clone https://github.com/em3rson-ufu/trab1.git
```
5. Abrir o Projeto no VS Code
```bash
code .
```
6. Rodar o Projeto
```bash
python main.py
```
7. Explorar as opções do Menu
8. Para ver o Versionamento, execute no terminal:
```bash
git log --oneline --graph --all
```
## Estrutura

```bash
trab1/
├── main.py                # menu principal
├── ativos.py              # CRUD de ativos
├── vulnerabilidades.py    # CRUD de vulnerabilidades
├── persistencia.py        # gravação em arquivos de texto
├── utils.py               # validação de entrada
├── enums.py               # constantes
├── relatorio.py           # relatório na tela
├── README.md
└── .gitignore
```

## Arquivos de dados

Os arquivos ficam na pasta `dados/`, criada automaticamente na
primeira execução:

- `dados/ativos.txt`
- `dados/vulnerabilidades.txt`

Cada arquivo usa `;` como separador de campos.

## Requisitos atendidos

1. Menu textual com tratamento de erros
2. Pelo menos 4 categorias de ativos (tem 8)
3. Cadastro de ativo com id único
4. Busca por id ou nome
5. Atualização de ativo
6. Remoção de ativo junto com suas vulnerabilidades
7. Cadastro de vulnerabilidades
8. Visualização de vulnerabilidades por ativo
9. Uso de dicionário indexado por id
10. Versionamento no GitHub com branches

## Autor

Émerson André Unfried

## Licença

Projeto desenvolvido para fins acadêmicos.