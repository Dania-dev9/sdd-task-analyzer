
"""Análise de produtividade de tarefas."""

import logging
from datetime import datetime
from typing import Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FORMATO_DATA = "%Y-%m-%d %H:%M:%S"
PRIORIDADES = ("baixa", "média", "alta")


class TaskValidationError(ValueError):
    """Indica que uma tarefa possui dados inválidos."""


def _parse_date(value: str | datetime | None, field: str) -> datetime | None:
    """Converte uma data textual em datetime, mantendo valores ausentes."""
    if value is None or value == "":
        return None

    if isinstance(value, datetime):
        return value

    if not isinstance(value, str):
        raise TaskValidationError(f"{field} deve ser uma data válida.")

    try:
        return datetime.strptime(value, FORMATO_DATA)
    except ValueError as exc:
        raise TaskValidationError(
            f"{field} deve seguir o formato AAAA-MM-DD HH:MM:SS."
        ) from exc


def analyze_tasks(tasks: list[dict[str, Any]]) -> dict[str, Any]:
    """Calcula indicadores gerais e por prioridade das tarefas."""
    if not isinstance(tasks, list):
        raise TaskValidationError("A entrada deve ser uma lista de tarefas.")

    total = len(tasks)
    concluidas = 0
    pendentes = 0
    tempos: list[float] = []
    atrasadas = 0

    quantidade_por_prioridade = {p: 0 for p in PRIORIDADES}
    tempos_por_prioridade: dict[str, list[float]] = {
        p: [] for p in PRIORIDADES
    }
    atrasadas_por_prioridade = {p: 0 for p in PRIORIDADES}
    concluidas_por_prioridade = {p: 0 for p in PRIORIDADES}

    for task in tasks:
        if not isinstance(task, dict):
            raise TaskValidationError("Cada tarefa deve ser um dicionário.")

        prioridade = task.get("prioridade")
        if prioridade not in PRIORIDADES:
            raise TaskValidationError(
                "A prioridade deve ser baixa, média ou alta."
            )

        quantidade_por_prioridade[prioridade] += 1

        status = task.get("status")
        if status not in ("concluída", "concluida", "concluído",
                          "concluido", "pendente", "em andamento"):
            raise TaskValidationError("Status de tarefa inválido.")

        _parse_date(task.get("data_criacao"), "data_criacao")
        inicio = _parse_date(task.get("data_inicio"), "data_inicio")
        conclusao = _parse_date(
            task.get("data_conclusao"), "data_conclusao"
        )
        prazo = _parse_date(task.get("prazo"), "prazo")

        if inicio and conclusao and conclusao < inicio:
            raise TaskValidationError(
                "A data de conclusão não pode ser anterior ao início."
            )

        if status in ("concluída", "concluida", "concluído", "concluido"):
            concluidas += 1
            concluidas_por_prioridade[prioridade] += 1

            if inicio is not None and conclusao is not None:
                minutos = (conclusao - inicio).total_seconds() / 60
                tempos.append(minutos)
                tempos_por_prioridade[prioridade].append(minutos)

            if conclusao is not None and prazo is not None:
                if conclusao > prazo:
                    atrasadas += 1
                    atrasadas_por_prioridade[prioridade] += 1
        else:
            pendentes += 1

    media = sum(tempos) / len(tempos) if tempos else 0.0

    # A taxa considera somente tarefas concluídas, conforme o contrato.
    taxa_atraso = (
        atrasadas / concluidas * 100 if concluidas else 0.0
    )

    media_por_prioridade = {
        p: (
            sum(valores) / len(valores) if valores else 0.0
        )
        for p, valores in tempos_por_prioridade.items()
    }

    taxa_atraso_por_prioridade = {
        p: (
            atrasadas_por_prioridade[p] / concluidas_por_prioridade[p] * 100
            if concluidas_por_prioridade[p] else 0.0
        )
        for p in PRIORIDADES
    }

    logger.info("Análise concluída: %d tarefas processadas.", total)

    return {
        "total_tarefas": total,
        "total_concluidas": concluidas,
        "total_pendentes": pendentes,
        "tempo_medio_conclusao_minutos": media,
        "taxa_atraso_percentual": taxa_atraso,
        "quantidade_por_prioridade": quantidade_por_prioridade,
        "tempo_medio_por_prioridade": media_por_prioridade,
        "taxa_atraso_por_prioridade": taxa_atraso_por_prioridade,
    }