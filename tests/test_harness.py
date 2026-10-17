import pytest

from src.task_analyzer import analyze_tasks, TaskValidationError


def test_analise_com_sucesso() -> None:
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": "2026-10-01 09:00:00",
            "data_conclusao": "2026-10-01 11:00:00",
            "prazo": "2026-10-01 12:00:00",
            "prioridade": "alta",
            "status": "concluída",
        },
        {
            "id_tarefa": 2,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": "2026-10-01 10:00:00",
            "data_conclusao": "2026-10-01 14:00:00",
            "prazo": "2026-10-01 13:00:00",
            "prioridade": "baixa",
            "status": "concluída",
        },
        {
            "id_tarefa": 3,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": None,
            "data_conclusao": None,
            "prazo": "2026-10-02 12:00:00",
            "prioridade": "média",
            "status": "pendente",
        },
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_tarefas"] == 3
    assert resultado["total_concluidas"] == 2
    assert resultado["total_pendentes"] == 1
    assert resultado["tempo_medio_conclusao_minutos"] == 180.0
    assert resultado["taxa_atraso_percentual"] == 50.0
    assert resultado["quantidade_por_prioridade"] == {
        "baixa": 1,
        "média": 1,
        "alta": 1,
    }
    assert resultado["tempo_medio_por_prioridade"] == {
        "baixa": 240.0,
        "média": 0.0,
        "alta": 120.0,
    }
    assert resultado["taxa_atraso_por_prioridade"] == {
        "baixa": 100.0,
        "média": 0.0,
        "alta": 0.0,
    }


def test_data_de_conclusao_anterior_ao_inicio() -> None:
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": "2026-10-01 11:00:00",
            "data_conclusao": "2026-10-01 10:00:00",
            "prazo": "2026-10-01 12:00:00",
            "prioridade": "alta",
            "status": "concluída",
        }
    ]

    with pytest.raises(TaskValidationError):
        analyze_tasks(tarefas)


def test_lista_vazia() -> None:
    resultado = analyze_tasks([])

    assert resultado["total_tarefas"] == 0
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 0
    assert resultado["tempo_medio_conclusao_minutos"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0


def test_apenas_tarefas_pendentes() -> None:
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": None,
            "data_conclusao": None,
            "prazo": "2026-10-01 12:00:00",
            "prioridade": "média",
            "status": "pendente",
        }
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_tarefas"] == 1
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 1
    assert resultado["tempo_medio_conclusao_minutos"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0


def test_prioridade_invalida() -> None:
    tarefas = [{"prioridade": "urgente", "status": "pendente"}]

    with pytest.raises(TaskValidationError, match="prioridade"):
        analyze_tasks(tarefas)


def test_tarefa_concluida_sem_datas_de_execucao() -> None:
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": "2026-10-01 08:00:00",
            "data_inicio": None,
            "data_conclusao": "2026-10-01 11:00:00",
            "prazo": "2026-10-01 12:00:00",
            "prioridade": "alta",
            "status": "concluída",
        }
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_concluidas"] == 1
    assert resultado["tempo_medio_conclusao_minutos"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0


def test_data_de_inicio_anterior_a_criacao_nao_invalida_tarefa() -> None:
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": "2026-10-01 10:00:00",
            "data_inicio": "2026-10-01 09:00:00",
            "data_conclusao": "2026-10-01 11:00:00",
            "prazo": "2026-10-01 12:00:00",
            "prioridade": "alta",
            "status": "concluída",
        }
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_concluidas"] == 1
    assert resultado["tempo_medio_conclusao_minutos"] == 120.0