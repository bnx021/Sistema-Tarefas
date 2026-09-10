from django.test import TestCase
from django.urls import reverse

from tarefa import Tarefa
from servicos import cadastrar_tarefa, filtrar_por_situacao


class TarefaTestCase(TestCase):
    def test_tarefa_inicia_pendente_e_pode_ser_concluida(self):
        tarefa = Tarefa("Estudar", "Revisar conteúdo", "Alta")
        self.assertEqual(tarefa.situacao, "Pendente")
        tarefa.concluir()
        self.assertEqual(tarefa.situacao, "Concluída")

    def test_servicos_cadastram_e_filtram(self):
        tarefas = []
        criada = cadastrar_tarefa(tarefas, "Uma", "Descrição", "Baixa", Tarefa)
        cadastrar_tarefa(tarefas, "Duas", "Descrição", "Alta", Tarefa).concluir()
        self.assertIs(tarefas[0], criada)
        self.assertEqual(filtrar_por_situacao(tarefas, "Concluída"), [tarefas[1]])


class RotasTarefasTestCase(TestCase):
    def test_inicio_renderiza_link_da_lista(self):
        response = self.client.get(reverse("inicio"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sistema Web de Gestão de Tarefas")
        self.assertContains(response, "/tarefas/")

    def test_lista_exibe_dados_temporarios(self):
        response = self.client.get(reverse("lista_tarefas"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Estudar URLs no Django")
        self.assertContains(response, "Alta")
        self.assertContains(response, "Concluída")
