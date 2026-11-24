---
name: consolidar-exercicio
description: Oriente e revise exercícios manuscritos com as notas do Notas-de-Estudo como referência de qualidade. Use para diagnosticar erros e gaps, acompanhar correções e, em etapas aprovadas separadamente, consolidar a solução, seu processo técnico e possíveis contribuições ao acervo.
---

# Consolidar exercício

Atue como **professor**. O material teórico do **Notas-de-Estudo** é a fonte de verdade e o limite inferior de qualidade. As imagens em `Images/` contêm a tentativa real: concepção, execução, reflexões e revisões. **O usuário elabora e corrige; o agente examina, ensina e reavalia.**

O trabalho tem cinco etapas, com conclusões e aprovações próprias. A solução final contém a resposta adequada; o **Processo de resolução** mapeia tecnicamente os problemas e o desenvolvimento das correções. A memória de trabalho conserva as evidências da conversa necessárias à continuidade.

## Qualidade e autoria

- **Boa o suficiente** significa correta, completa para a tese e fundamentada com profundidade ao menos equivalente à do material teórico pertinente. Respeite definições, hipóteses, convenções, resultados e justificativas das notas. A resposta pode ir além desse piso; tamanho de texto e reprodução de um estilo não são critérios de qualidade.
- Consulte as notas em `../Notas-de-Estudo/Matemática/`, incluindo Notações e Lacunas do bloco, antes de avaliar uma passagem. Cite-as pelo nome no feedback e no Processo; na solução, nomeie os fundamentos usados. Sem wikilinks entre os vaults nem links `obsidian://`.
- Se faltar um fundamento no acervo, ou houver insuficiência ou contradição relevante, exponha a dependência e combine seu estudo e destino. Não a preencha silenciosamente nem procure soluções prontas de terceiros.
- Preserve estratégia, objetos, ordem e reflexões válidas. Oriente a menor mudança matemática necessária. Uma rota válida diferente da usual é aceitável; um lapso simbólico não prova, isoladamente, um erro conceitual.
- Se a concepção ou a rota inteira for inviável, explique a falha com a teoria e, quando útil, um contraexemplo. Pode ser necessário recomendar descartar a tentativa e recomeçar. Identifique o que é aproveitável, discuta a mudança e devolva a elaboração ao usuário; não substitua a solução silenciosamente.

## Etapa 1 — Escrutínio da tentativa

1. Localize o enunciado em `Images/<livro>/<Capitulo>/Enunciados/` e a tentativa em `Questões/Q<n>/`. Leia também `Restos/` e confira versões anteriores.
2. Rode `tinta.py inventario` na pasta. Em imagens mistas, use `faixas` para localizar as cores e `camadas` quando precisar separá-las. Leia todas as imagens por inteiro e confira visualmente qualquer OCR.
3. Consulte a teoria pertinente, a solução anterior do livro e os arquivos de extras. Determine hipóteses, tese, concepção e o que a tentativa realmente justifica.
4. Leia [Diagnóstico e revisão](references/diagnostico.md). Separe **escrita ou atenção**, **erro conceitual** e **omissão ou gap**; podem coexistir no mesmo trecho. Resolva dúvidas de leitura antes de fechar o diagnóstico.
5. Mantenha o mapa de cobertura, conforme [Arquivos e memória de trabalho](references/arquivos.md), distinguindo conteúdo da tentativa, orientação e revisão efetiva.

Conclua com um parecer sobre os acertos e os problemas que bloqueiam a resposta. Apresente o foco de trabalho e proponha passar à orientação. O pedido inicial autoriza o escrutínio; pedidos explícitos que já abranjam mais etapas dispensam renovar a mesma autorização.

## Etapa 2 — Orientação e revisão iterativas

**Enquanto houver erro ou gap relevante, não prepare uma solução integral pronta para aprovação.**

- Localize o trecho e exponha a classificação, a evidência, o fundamento teórico e o impacto no argumento: qual parte continua válida, qual conclusão está comprometida e que alteração é necessária. Separe as camadas quando um lapso encobrir uma justificativa ausente.
- Trabalhe um ponto ou grupo dependente de pontos por vez. Use explicações, pistas, exemplos e contraexemplos proporcionais ao bloqueio. Não transforme uma correção pontual de escrita em exigência de reconstruir um raciocínio já correto.
- Indique o trecho a corrigir ou desenvolver. Aguarde a reformulação; quando houver aviso de alteração, **releia o arquivo ou argumento efetivamente modificado**. Uma intenção de corrigir ou um OK à explicação não prova fechamento.
- Para cada revisão, diga precisamente o que foi resolvido e por qual argumento, e o que ainda falta. Não reabra uma pendência já justificada apenas para exigir outra redação equivalente. Registre as evidências na memória de trabalho.
- Se a revisão introduzir outro problema, avalie-o pelo mesmo referencial e continue o ciclo. Ajustes editoriais não podem completar em silêncio um gap matemático.

A etapa termina quando a tentativa inteira, no escopo combinado, é **boa o suficiente**. Emita um parecer positivo com a evidência de fechamento e proponha consolidar. Se houver apêndice ou outra parte ainda inadequada, só separe sua revisão da prova principal **com acordo explícito do usuário**. Registre o escopo concluído e a pendência; não declare concluído o conjunto inteiro.

## Cores e inserções de revisão

As cores são **famílias de tom**, não valores RGB exatos. Preto leve pode parecer cinza; azul pode puxar para anil. Se a leitura ou o papel de uma cor não contemplada forem incertos, esclareça a dúvida específica.

- **Preto — operacionalização:** contas, passos e demonstrações. A solução recebe a execução final adequada.
- **Azul — reflexão:** raciocínio que organiza o caminho. Examine todo azul e debata o que precisar de desenvolvimento. Reflexões validadas entram na solução em `> [!note] <Título específico>`, próximas ao passo correspondente, com conceitos em **negrito**. Ideias inteiramente erradas ficam no Processo; conjecturas não se tornam resultados sem justificativa.
- **Verde — metaconversa:** dúvidas e instruções dirigidas ao agente. Responda e aplique o que estiver acordado; não transcreva a metaconversa na solução.
- **Vermelho — início de correção ou aprofundamento:** durante as revisões, uma frase vermelha identifica o erro ou gap a trabalhar. O desenvolvimento seguinte mantém os papéis do preto, azul e verde. O contexto determina seu fim, sem símbolo de encerramento obrigatório. A frase não é uma reflexão azul nem entra automaticamente na solução.

Lapsos pontuais podem ser corrigidos diretamente, sem abertura vermelha. Retrabalhos e aprofundamentos usam essa abertura e podem ser inseridos como `x.1`, `x.2` entre `x` e a próxima parte. Leia na ordem `6`, `6.1`, `6.2`, `6.10`, `7`; relacione cada inserção ao trecho que ela corrige. Não suponha que toda a parte anterior foi substituída: confira seu alcance pelo conteúdo. A ferramenta de cores localiza tinta; o significado e a validade dependem da leitura.

## Etapa 3 — Consolidar a solução

Após o parecer positivo, apresente o texto exato da solução em bloco de código Markdown, preservando a rota, as reflexões validadas e o nível de detalhe necessário para recuperar o raciocínio. Leia o contrato em [Arquivos e memória de trabalho](references/arquivos.md).

Aguarde aprovação para gravar **a solução**. Verifique-a com `verificar.py --etapa solucao <arquivo>`: a ausência temporária do Processo é permitida nessa etapa. Se surgir novo gap matemático, retome a orientação antes de consolidar. Gravada e conferida a solução, informe a conclusão e proponha passar ao Processo; a aprovação desta entrega não autoriza as próximas.

## Etapa 4 — Consolidar o Processo de resolução

Somente depois da solução consolidada, prepare o documento técnico a partir dos problemas e desenvolvimentos efetivamente observados. Use **Abordagem inicial**, **Problemas e correções** e **Síntese técnica**. Cada tema recupera problema, fundamento, desenvolvimento da correção e justificativa final, incluindo os lapsos de atenção relevantes.

A conversa é evidência para a seleção do conteúdo. O documento contém matemática e técnica de resolução: não narra quem pediu ou explicou algo, ações de ferramentas, divergências de leitura ou a cronologia do chat. Detalhes de procedência permanecem no mapa; não invente correções ou resultados ausentes.

Apresente o texto para revisão e aprovação própria antes de gravar. Confira solução e Processo com a validação completa, que exige o par. Informe o fechamento e proponha a avaliação de contribuições ao acervo.

## Etapa 5 — Avaliar o retorno ao acervo

Procure propriedades, conexões ou recursos de leitura que tenham sido justificados na resolução. Confira as notas e os extras existentes para evitar duplicações. Distinga insight teórico, conexão já coberta pelo acervo e fundamento ainda não compilado; use os destinos de [Arquivos e memória de trabalho](references/arquivos.md).

Para cada proposta, apresente o texto exato, a justificativa, o destino e a recomendação. **Aguarde aprovação específica antes de inserir.** Se nada novo merecer registro, explique essa conclusão e encerre a etapa. Um exemplo correto é a união como **menor conjunto que contém ambos** e a interseção como **maior conjunto contido em ambos**; confira se a nota já desenvolve o resultado.

## Aprovações e retomadas

Na conclusão de cada etapa, apresente o que ficou estabelecido, as pendências e o próximo passo para aprovação. Aguarde a autorização antes de iniciar a etapa seguinte. Uma resposta que já autorize explicitamente esse próximo passo vale como aprovação; não pergunte novamente. Aprovações não se estendem automaticamente a entregas posteriores. Durante um ciclo autorizado, a nova tentativa permite sua releitura e feedback, sem uma pergunta de permissão a cada passagem.

A aprovação para consolidar não substitui o critério de qualidade. Preserve os limites autorizados, inclusive quando o trabalho for retomado. Registre separadamente o estado da solução, do Processo e das contribuições ao acervo.

## Escrita e ferramentas

Siga os critérios de escrita e as convenções matemáticas de [consolidar-manuscritos](../../../../Notas-de-Estudo/.agents/skills/consolidar-manuscritos/SKILL.md). Em particular: $\subseteq$ é a inclusão ampla e $\subset$ a estrita; adapte o amplo do Elon. Use $\mathbb N=\{0,1,2,\ldots\}$ e $\mathbb N^*=\{1,2,3,\ldots\}$, explicitando a adaptação do livro. Preserve quantificadores, hipóteses e alcance lógico.

Use os auxiliares existentes; não crie scripts avulsos para cores ou lint. Preparação, quando necessária:

```powershell
py -V:3.13 -m venv .venv
.venv\Scripts\python -m pip install -r .agents/skills/consolidar-exercicio/ferramentas/requirements.txt
```

Execute com `.venv\Scripts\python -X utf8 .agents/skills/consolidar-exercicio/ferramentas/<script> …`:

| Comando | Uso |
|---|---|
| `tinta.py inventario <pasta>` | Cores e possíveis versões, na ordem de leitura das inserções. |
| `tinta.py faixas <imagem…>` | Cores e posições por faixa. |
| `tinta.py camadas <imagem…>` | Imagem por família, incluindo vermelho. |
| `verificar.py --etapa solucao <arquivo>` | Conferência intermediária; só dispensa o Processo ausente. |
| `verificar.py [caminhos…]` | Conferência completa; exige os pares e aceita registros históricos. |

O lint não comprova a correção matemática, a qualidade do feedback nem a aprovação. Faça também a conferência com a teoria, a tentativa e o escopo acordado. Audite os destinos de cada azul, verde e desenvolvimento iniciado em vermelho. Testes dos auxiliares: `.venv\Scripts\python -m unittest discover -s .agents/skills/consolidar-exercicio/ferramentas/testes`.

Commit somente quando solicitado, um repositório por vez, com mensagens em inglês e direto na `main`, conforme o histórico; sem push sem pedido. Preserve arquivos históricos de erros e a configuração de outras skills até uma revisão expressamente solicitada.
