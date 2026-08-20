# Sistema Web de Gestão de Tarefas

Projeto inicial do laboratório de programação back end. Nesta etapa, foi criada uma base reproduzível do projeto e um protótipo de cadastro de tarefa executado no terminal.

## Objetivo

Preparar uma estrutura simples de projeto Python que possa ser aberta, compreendida e executada no VS Code. O projeto contém um script inicial com o nome do sistema e um protótipo que recebe os dados de uma tarefa, realiza cálculos simples e exibe um resumo formatado.

## Pré-requisitos

É necessário ter o **Python 3** e o **Git** instalados no computador. O projeto não precisa de banco de dados, serviço externo ou conta em nuvem.

## Como abrir no VS Code

Abra o VS Code, selecione **File > Open Folder** e escolha a pasta `sistema-tarefas`. Também é possível abrir a pasta pelo terminal com o comando abaixo:

```bash
code .
```

## Criação e ativação do ambiente virtual

Dentro da pasta do projeto, crie o ambiente virtual com:

```bash
python -m venv .venv
```

No Linux ou macOS, ative o ambiente com:

```bash
source .venv/bin/activate
```

No Windows PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
```

No Windows pelo Prompt de Comando, use:

```bat
.venv\Scripts\activate
```

Depois que o ambiente estiver ativo, instale as dependências registradas:

```bash
pip install -r requirements.txt
```

Para sair do ambiente virtual, utilize:

```bash
deactivate
```

## Execução

Para executar o script inicial da atividade de base reproduzível:

```bash
python main.py
```

A saída esperada é:

```text
Sistema Web de Gestão de Tarefas
```

Para executar o protótipo de cadastro de tarefa:

```bash
python cadastro_tarefa.py
```

O programa solicita o título, a prioridade, o prazo estimado e a indicação de urgência. Em seguida, calcula o esforço estimado, verifica se a prioridade é alta e informa se a tarefa deve ser tratada como prioritária.

## Cenários de teste

O primeiro cenário deve ser preenchido com os valores abaixo. Como a prioridade é 2 e a tarefa não é urgente, o resultado de `Deve ser tratada como prioritária` deve ser `False`.

| Campo | Valor |
|---|---|
| Título | Tarefa planejada |
| Prioridade | 2 |
| Prazo | 6.5 |
| Urgente | nao |

No segundo cenário, utilize uma prioridade 3 e responda `sim` para urgência. Mesmo sem prioridade alta, a urgência torna o resultado `True`.

| Campo | Valor |
|---|---|
| Título | Correção crítica |
| Prioridade | 3 |
| Prazo | 1.5 |
| Urgente | sim |

## Estrutura do projeto

| Arquivo ou pasta | Finalidade |
|---|---|
| `main.py` | Exibe a mensagem inicial do Sistema Web de Gestão de Tarefas. |
| `cadastro_tarefa.py` | Executa o protótipo de cadastro e apresenta o resumo da tarefa. |
| `requirements.txt` | Registra a dependência instalada no ambiente virtual. |
| `.gitignore` | Impede que `.venv/` e arquivos temporários do Python sejam versionados. |
| `.venv/` | Ambiente virtual local do projeto; não deve ser enviado ao repositório. |

## Controle de versão

Para inicializar o Git e registrar a implementação, execute:

```bash
git init
git add .
git commit -m "Cria estrutura inicial e prototipo de cadastro"
```

Para conferir a situação do repositório:

```bash
git status
```

A pasta `.venv/` não deve aparecer entre os arquivos preparados para commit porque está indicada no `.gitignore`.
