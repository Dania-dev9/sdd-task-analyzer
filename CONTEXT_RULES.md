# CONTEXT_RULES.md

## 1. Objetivo

Este documento define as regras de governança que devem ser seguidas por assistentes de Inteligência Artificial durante o desenvolvimento do TaskAnalyzer.

A implementação deverá respeitar a especificação de negócio localizada em `specs/task_analyzer_spec.md`. O código gerado pela IA deverá ser revisado e validado por uma pessoa antes de ser considerado aprovado.

## 2. Regras de desenvolvimento

- Utilizar Python 3.11 ou superior.
- Utilizar type hints em todas as funções e parâmetros.
- Manter o código organizado, simples e de fácil compreensão.
- Definir funções com responsabilidades bem delimitadas.
- Implementar tratamento de erros com exceções específicas.
- Documentar funções e classes.
- Utilizar o módulo `logging` para registrar eventos relevantes.
- Prevenir erros de divisão por zero.
- Seguir as regras de negócio e os cenários de aceite definidos na especificação SDD.

## 3. Restrições para a IA

A Inteligência Artificial não deverá:

- Alterar os requisitos definidos no projeto.
- Modificar os testes apenas para fazer um código incorreto passar.
- Alterar a estrutura do projeto sem necessidade ou autorização.
- Criar funcionalidades que não foram solicitadas.
- Utilizar bibliotecas externas sem autorização.
- Remover ou ignorar regras definidas na especificação.
- Alterar as assinaturas das funções sem autorização.
- Considerar o código gerado automaticamente como correto sem validação.

Quando houver informações ausentes ou ambiguidades na especificação, a decisão deverá ser identificada e analisada antes da implementação. A IA não deverá inventar requisitos para preencher essas lacunas.

## 4. Regras de implementação do TaskAnalyzer

- Implementar a função `analyze_tasks` conforme o contrato definido em `specs/task_analyzer_spec.md`.
- Implementar a exceção personalizada `TaskValidationError`.
- Considerar as regras de cálculo e validação definidas na especificação.
- Identificar datas inconsistentes e tratar os erros de validação adequadamente.
- Não considerar tarefas pendentes nos cálculos que, segundo a especificação, dependam de tarefas concluídas.
- Garantir que situações sem tarefas concluídas não provoquem divisão por zero.
- Não introduzir comportamentos que contrariem os requisitos documentados.

## 5. Regras para os testes

- Utilizar `pytest` para executar os testes automatizados.
- Cobrir os cenários de aceite e os casos de borda descritos na especificação.
- Verificar os resultados calculados e as exceções esperadas.
- Não alterar os testes apenas para ocultar falhas da implementação.
- Investigar e corrigir a causa de cada falha antes de considerar o sistema aprovado.

## 6. Homologação humana

Antes de aprovar a implementação, a pessoa responsável deverá:

- Revisar o código gerado pela IA.
- Comparar o comportamento implementado com a especificação SDD.
- Executar os testes automatizados.
- Verificar o tratamento de erros e os casos de borda.
- Registrar e corrigir divergências encontradas.

O sistema somente deverá ser considerado homologado quando cumprir os requisitos e passar pelas verificações previstas.

## 7. Controle de alterações

Alterações nos requisitos, na estrutura do projeto ou nas assinaturas das funções deverão ser avaliadas antes de serem implementadas.

As alterações de código e testes deverão ser versionadas com Git, utilizando commits descritivos e o fluxo de revisão previsto no projeto.