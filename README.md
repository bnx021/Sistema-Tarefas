# Sistema de Gestão de Tarefas

Projeto didático que evolui um protótipo de tarefas em Python para uma primeira interface web com Django. Nesta etapa, as tarefas da aplicação web são temporárias e ficam definidas em memória; não há banco de dados funcional.

## Requisitos

Python 3.10 ou superior, pip e Django entre as versões 5 e 6.

## Instalação e execução

Na raiz do projeto, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
```

Execute as verificações e o servidor Django:

```bash
python manage.py check
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` para a página inicial e `http://127.0.0.1:8000/tarefas/` para a listagem.

## Organização

| Arquivo ou pasta | Responsabilidade |
| --- | --- |
| `tarefa.py` | Classe `Tarefa`, com estado inicial, conclusão e resumo. |
| `servicos.py` | Cadastro, listagem e filtro por situação. |
| `main.py` | Demonstração da refatoração com três tarefas e uma conclusão. |
| `gestao_tarefas/settings.py` | Configurações do projeto e registro da aplicação. |
| `gestao_tarefas/urls.py` | Rotas gerais e inclusão das rotas de `tarefas`. |
| `tarefas/views.py` | Views `inicio` e `lista_tarefas`, com dados temporários. |
| `tarefas/urls.py` | Rotas `/` e `/tarefas/`. |
| `tarefas/templates/tarefas/` | Templates HTML das duas páginas. |
| `manage.py` | Comandos administrativos do Django. |

## Demonstração Python

A refatoração solicitada na primeira atividade pode ser executada sem servidor:

```bash
python main.py
```

Ela cadastra três objetos `Tarefa`, conclui o primeiro, lista todos e filtra os concluídos.

## Funcionalidades web entregues

A página inicial apresenta o sistema e um link para a lista. A página `/tarefas/` apresenta duas tarefas temporárias com título, prioridade e situação, usando um template Django com `for` e `if`; também oferece um link de retorno para a página inicial.

## Observação sobre persistência

Os dados da view são recriados quando o processo Django é reiniciado, conforme o escopo da atividade. A configuração SQLite padrão do Django permanece apenas como configuração inicial do projeto e nenhum modelo ou migração de negócio foi criado.
