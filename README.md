# TaskAnalyzer

## Objetivo

O TaskAnalyzer é um projeto em Python para analisar tarefas com base nas regras e nos critérios de aceitação definidos na especificação SDD.

## Requisitos

- Python 3.11 ou superior.
- pytest para execução dos testes.

## Estrutura do projeto

- `src/task_analyzer.py`: implementação do analisador de tarefas.
- `tests/test_harness.py`: testes automatizados.
- `specs/task_analyzer_spec.md`: especificação SDD.
- `CONTEXT_RULES.md`: regras de contexto e governança do uso de IA.
- `requirements.txt`: dependências do projeto.

## Instalação

No Windows, crie e ative um ambiente virtual e instale as dependências:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Se o inicializador `py` não estiver disponível, substitua `py -3` por
`python`, desde que esse comando aponte para Python 3.11 ou superior.

## Testes

Execute os testes com:

```powershell
python -m pytest -v
```

## Status

Em desenvolvimento.