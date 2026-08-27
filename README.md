# Sistema Web de GestÃ£o de Tarefa

Projeto inicial do laboratÃ³rio de programaÃ§Ã£o back end. Nesta etapa, foi criada uma base reproduzÃ­vel do projeto e um protÃ³tipo de cadastro de tarefa executado no terminal.

## Objetivo

Preparar uma estrutura simples de projeto Python que possa ser aberta, compreendida e executada no VS Code. O projeto contÃ©m um script inicial com o nome do sistema e um protÃ³tipo que recebe os dados de uma tarefa, realiza cÃ¡lculos simples e exibe um resumo formatado.

## PrÃ©-requisitos

Ã‰ necessÃ¡rio ter o **Python 3** e o **Git** instalados no computador. O projeto nÃ£o precisa de banco de dados, serviÃ§o externo ou conta em nuvem.

## Como abrir no VS Code

Abra o VS Code, selecione **File > Open Folder** e escolha a pasta `sistema-tarefas`. TambÃ©m Ã© possÃ­vel abrir a pasta pelo terminal com o comando abaixo:

```bash
code .
```

## CriaÃ§Ã£o e ativaÃ§Ã£o do ambiente virtual

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

Depois que o ambiente estiver ativo, instale as dependÃªncias registradas:

```bash
pip install -r requirements.txt
```

Para sair do ambiente virtual, utilize:

```bash
deactivate
```

## ExecuÃ§Ã£o

Para executar o script inicial da atividade de base reproduzÃ­vel:

```bash
python main.py
```

A saÃ­da esperada Ã©:

```text
Sistema Web de GestÃ£o de Tarefas
```

Para executar o protÃ³tipo de cadastro de tarefa:

```bash
python cadastro_tarefa.py
```

O programa solicita o tÃ­tulo, a prioridade, o prazo estimado e a indicaÃ§Ã£o de urgÃªncia. Em seguida, calcula o esforÃ§o estimado, verifica se a prioridade Ã© alta e informa se a tarefa deve ser tratada como prioritÃ¡ria.

## CenÃ¡rios de teste

O primeiro cenÃ¡rio deve ser preenchido com os valores abaixo. Como a prioridade Ã© 2 e a tarefa nÃ£o Ã© urgente, o resultado de `Deve ser tratada como prioritÃ¡ria` deve ser `False`.

| Campo | Valor |
|---|---|
| TÃ­tulo | Tarefa planejada |
| Prioridade | 2 |
| Prazo | 6.5 |
| Urgente | nao |

No segundo cenÃ¡rio, utilize uma prioridade 3 e responda `sim` para urgÃªncia. Mesmo sem prioridade alta, a urgÃªncia torna o resultado `True`.

| Campo | Valor |
|---|---|
| TÃ­tulo | CorreÃ§Ã£o crÃ­tica |
| Prioridade | 3 |
| Prazo | 1.5 |
| Urgente | sim |

## Estrutura do projeto

| Arquivo ou pasta | Finalidade |
|---|---|
| `main.py` | Exibe a mensagem inicial do Sistema Web de GestÃ£o de Tarefas. |
| `cadastro_tarefa.py` | Executa o protÃ³tipo de cadastro e apresenta o resumo da tarefa. |
| `requirements.txt` | Registra a dependÃªncia instalada no ambiente virtual. |
| `.gitignore` | Impede que `.venv/` e arquivos temporÃ¡rios do Python sejam versionados. |
| `.venv/` | Ambiente virtual local do projeto; nÃ£o deve ser enviado ao repositÃ³rio. |

## Controle de versÃ£o

Para inicializar o Git e registrar a implementaÃ§Ã£o, execute:

```bash
git init
git add .
git commit -m "Cria estrutura inicial e prototipo de cadastro"
```

Para conferir a situaÃ§Ã£o do repositÃ³rio:

```bash
git status
```

A pasta `.venv/` nÃ£o deve aparecer entre os arquivos preparados para commit porque estÃ¡ indicada no `.gitignore`.

## Menu interativo de tarefas

A atividade da Semana 03/04 foi implementada no arquivo `menu_tarefas.py`. O programa mantÃ©m um menu ativo atÃ© que a opÃ§Ã£o de encerramento seja escolhida.

Para executar o menu no Windows, use o terminal dentro da pasta do projeto:

```powershell
python menu_tarefas.py
```

Se necessÃ¡rio, tambÃ©m Ã© possÃ­vel executar com:

```powershell
py menu_tarefas.py
```

O menu possui as seguintes opÃ§Ãµes:

| OpÃ§Ã£o | Funcionamento |
|---|---|
| `1` | Cadastra uma tarefa com tÃ­tulo, prioridade e situaÃ§Ã£o inicial pendente. |
| `2` | Lista as tarefas cadastradas usando uma repetiÃ§Ã£o `for`. |
| `3` | Atualiza uma tarefa existente para a situaÃ§Ã£o concluÃ­da. |
| `4` | Encerra o sistema. |

O cadastro rejeita tÃ­tulo vazio e prioridades diferentes de baixa, mÃ©dia ou alta. O programa tambÃ©m informa quando uma opÃ§Ã£o Ã© invÃ¡lida, quando nÃ£o hÃ¡ tarefas cadastradas ou quando o nÃºmero informado nÃ£o corresponde a uma tarefa existente.

### LimitaÃ§Ã£o conhecida

Os registros sÃ£o mantidos somente em memÃ³ria durante a execuÃ§Ã£o. Portanto, as tarefas sÃ£o perdidas quando o programa Ã© encerrado. Nesta etapa ainda nÃ£o foi utilizado banco de dados ou arquivo permanente.

### Participantes

- Gabriel Leal da Silva
- Brenno César G. dos Santos
