Visão geral e contrato de negócio

1.1 Identificação

- Discente: Dania Sadallah Kader
- Curso: Análise e desenvolvimento de sistemas
- Polo: Asa Norte
- Turma: A
- E-mail institucional: daniasadallah@sempreceub.com

1.2 Propósito do módulo TaskAnalyzer

O sistema do TaskAnalyzer tem como objetivo analisar um conjunto de tarefas, efetuando o processamento das informações fornecidas, mostrando métricas que estão relacionadas à produtividade. Dentro do que será analisado de informação, está: o total de tarefas a serem realizadas, suas prioridades de acordo com a necessidade, o quanto essas tarefas tiveram de atraso e o tempo para executá-las. Esse sistema deve executar os dados de acordo com as normas estabelecidas no contrato do negócio, gerando resultados que sejam posteriormente validados através de testes automatizados.
1.3 Contrato de interface
1.3.1 Entradas
O TaskAnalyzer receberá uma lista de tarefas. Cada tarefa deverá possuir informações necessárias para que os cálculos sejam realizados.
Os principais dados serão:
id_tarefa: identificador da tarefa;
data_criacao: data em que a tarefa foi criada;
data_inicio: data em que a tarefa começou a ser realizada;
data_conclusao: data em que a tarefa foi finalizada;
prazo: data limite para conclusão da tarefa;
prioridade: prioridade da tarefa;
status: situação atual da tarefa.
A prioridade deverá possuir apenas três possibilidades:
baixa;
média;
alta.
O status será utilizado para identificar se a tarefa já foi concluída ou ainda está em andamento.

1.3.2 Saídas
Depois de analisar as tarefas recebidas, o módulo deverá retornar as informações calculadas.
Entre os principais resultados estão:
tempo médio de conclusão em minutos;
taxa de tarefas atrasadas em porcentagem;
quantidade de tarefas por prioridade;
indicadores de desempenho separados por prioridade.
Dessa forma, o resultado deverá permitir uma visão geral das tarefas e também uma comparação entre tarefas de diferentes prioridades.
1.3.3 Regras de negócio
Para que os resultados sejam calculados corretamente, serão utilizadas as seguintes regras:
Apenas tarefas com status concluída serão utilizadas no cálculo do tempo de conclusão.
O tempo de conclusão será calculado utilizando a diferença entre a data de início e a data de conclusão.
Uma tarefa será considerada atrasada quando a data de conclusão for maior que o prazo definido.
Tarefas que ainda não foram concluídas não deverão ser consideradas no cálculo da taxa de atraso.
Caso uma tarefa não possua data de início ou data de conclusão, não será possível calcular seu tempo de conclusão.
A data de conclusão não poderá ser anterior à data de início.
A prioridade deverá ser informada como baixa, média ou alta.
A taxa de atraso deverá ser apresentada em porcentagem.
O sistema deverá evitar erros de divisão por zero quando não existirem tarefas concluídas.
Os resultados deverão ser calculados de acordo com os dados recebidos pelo módulo.



2. Cenários de aceite e Test Harness
2.1 Cenários de aceite:
Cenário 1 – Análise realizada com sucesso: Dado que o sistema recebeu uma lista de tarefas com informações válidas; Quando o TaskAnalyzer realizar a análise das tarefas; Então o sistema deverá apresentar corretamente o tempo médio de conclusão, a taxa de atraso e a quantidade de tarefas por prioridade.
Cenário 2 – Dados inválidos: Dado que o sistema recebeu uma tarefa com informações inválidas, como uma data de conclusão anterior à data de início; Quando o TaskAnalyzer tentar realizar a análise; Então o sistema deverá identificar o problema e apresentar uma mensagem de erro informando que os dados são inválidos.
Cenário 3 – Nenhuma tarefa concluída: Dado que a lista recebida não possui tarefas concluídas;Quando o TaskAnalyzer realizar a análise;Então o sistema não deverá apresentar erro de divisão por zero e deverá retornar os indicadores com valores adequados para essa situação.
2.2 Test Harness
O Test Harness será utilizado para verificar se o TaskAnalyzer está funcionando de acordo com o que foi definido na especificação. Os testes deverão verificar principalmente:
se o tempo médio está sendo calculado corretamente;
se tarefas atrasadas estão sendo identificadas;
se a porcentagem de atraso está correta;
se as tarefas estão sendo separadas corretamente por prioridade;
se entradas inválidas geram erros;
se o sistema consegue lidar com uma lista sem tarefas concluídas.
Os testes automatizados serão desenvolvidos utilizando pytest. Cada teste deverá possuir dados de entrada e um resultado esperado. Dessa forma, será possível comparar o resultado obtido pelo sistema com o resultado esperado.



3. Regras para utilização de IA
Durante o desenvolvimento do TaskAnalyzer, a Inteligência Artificial poderá ser utilizada como ferramenta de apoio para auxiliar na criação e melhoria do código. Entretanto, o código gerado pela IA deverá ser analisado e testado antes de ser considerado correto. A IA deverá seguir as regras definidas no projeto e não poderá alterar o comportamento definido na especificação sem autorização.
3.1 Regras de desenvolvimento
O projeto deverá utilizar:
Python 3.11 ou superior;
type hints nas funções;
código organizado e de fácil entendimento;
funções com responsabilidades bem definidas;
tratamento de erros;
documentação das funções e classes;
utilização do módulo logging para registros importantes.
O código deverá priorizar simplicidade e organização, evitando funções muito grandes ou desnecessariamente complexas.
3.2 Restrições para a IA
A IA não deverá:
alterar os requisitos definidos no projeto;
modificar os testes para fazer um código incorreto passar;
alterar a estrutura do projeto sem necessidade;
criar funcionalidades que não foram solicitadas;
utilizar bibliotecas externas sem autorização;
remover regras definidas na especificação;
alterar as assinaturas das funções sem autorização.
Quando existir alguma informação que não esteja definida na especificação, a decisão deverá ser analisada antes de ser implementada.



4. Estrutura do projeto
A estrutura inicial do projeto será organizada da seguinte forma:
sdd-task-analyzer/
│
├── README.md
├── CONTEXT_RULES.md
│
├── specs/
│   └── task_analyzer_spec.md
│
├── tests/
│   └── test_harness.py
│
└── src/
    └── task_analyzer.py

O arquivo README.md terá informações gerais sobre o projeto. O arquivo CONTEXT_RULES.md terá as regras que deverão ser seguidas durante o desenvolvimento com auxílio de Inteligência Artificial. O arquivo task_analyzer_spec.md terá a especificação do TaskAnalyzer. O arquivo test_harness.py será responsável pelos testes automatizados. O arquivo task_analyzer.py terá a implementação do módulo.
4.1 Homologação
Depois que o código for desenvolvido, será realizada uma revisão para verificar se ele está de acordo com a especificação. A homologação deverá verificar:
funcionamento dos testes;
atendimento aos requisitos;
funcionamento dos cálculos;
tratamento de entradas inválidas;
organização do código;
cumprimento das regras definidas para utilização da IA.
Além dos testes automatizados, poderão ser realizados testes manuais para verificar situações que não foram contempladas nos testes principais.
O código somente será considerado aprovado depois de passar pelos testes e pela revisão.
