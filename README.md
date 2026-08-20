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

## Menu interativo de tarefas

A atividade da Semana 03/04 foi implementada no arquivo `menu_tarefas.py`. O programa mantém um menu ativo até que a opção de encerramento seja escolhida.

Para executar o menu no Windows, use o terminal dentro da pasta do projeto:

```powershell
python menu_tarefas.py
```

Se necessário, também é possível executar com:

```powershell
py menu_tarefas.py
```

O menu possui as seguintes opções:

| Opção | Funcionamento |
|---|---|
| `1` | Cadastra uma tarefa com título, prioridade e situação inicial pendente. |
| `2` | Lista as tarefas cadastradas usando uma repetição `for`. |
| `3` | Atualiza uma tarefa existente para a situação concluída. |
| `4` | Encerra o sistema. |

O cadastro rejeita título vazio e prioridades diferentes de baixa, média ou alta. O programa também informa quando uma opção é inválida, quando não há tarefas cadastradas ou quando o número informado não corresponde a uma tarefa existente.

### Limitação conhecida

Os registros são mantidos somente em memória durante a execução. Portanto, as tarefas são perdidas quando o programa é encerrado. Nesta etapa ainda não foi utilizado banco de dados ou arquivo permanente.
