from django.shortcuts import render


DADOS_TEMPORARIOS = [
    {
        "titulo": "Estudar URLs no Django",
        "prioridade": "Alta",
        "situacao": "Pendente",
    },
    {
        "titulo": "Criar template de listagem",
        "prioridade": "Média",
        "situacao": "Concluída",
    },
]


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    return render(request, "tarefas/lista.html", {"tarefas": DADOS_TEMPORARIOS})
