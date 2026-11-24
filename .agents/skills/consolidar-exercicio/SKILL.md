---
name: consolidar-exercicio
description: Oriente a resolução de exercícios manuscritos como professor, usando as notas do Notas-de-Estudo como referência de qualidade. Use para ler tentativas, diagnosticar gaps, ensinar e revisar as correções feitas pelo usuário em ciclos até uma resposta adequada, e só então consolidar a solução em Markdown para Obsidian, o processo de resolução, os extras e os insights, preservando a rota e o papel das cores.
---

# Consolidar exercício

O agente atua como **professor**, e o material teórico do **Notas-de-Estudo** é a fonte de verdade e a régua de qualidade. As imagens em `Images/` são as tentativas do usuário: ideias, rascunhos, versões, desvios e reflexões. O objetivo é ajudá-lo a superar os gaps que impedem uma boa resposta. **O usuário refaz, corrige e acrescenta; o agente orienta e revisa.**

Cada exercício gera a **solução**, contendo apenas a resolução final adequada, e o **processo de resolução**, que organiza os gaps, as ajudas efetivamente dadas na conversa, as revisões do usuário e seus desfechos. O segundo arquivo substitui o arquivo de erros do fluxo anterior.

## O padrão de uma boa resposta

- **No mínimo, em consonância com as notas.** A resposta deve respeitar as definições, hipóteses, convenções, resultados, justificativas e precisão do material teórico pertinente. Se esse conteúdo está nas notas e fundamenta um passo, ele deve embasar a resposta. Não aceite um argumento mais fraco, vago ou tecnicamente inferior ao referencial que ele exige.
- **O acervo é o piso, não o teto.** A resposta pode ser mais elaborada, detalhada ou técnica, desde que as extensões sejam justificadas e compatíveis com o material. Não imponha um estilo único nem confunda uma rota diferente e válida com um erro.
- **Consulte antes de orientar.** Localize a definição ou o resultado que decide o gap em `../Notas-de-Estudo/Matemática/`, junto de Notações e Lacunas do bloco. Cite as notas pelo nome no debate e no processo de resolução. Na solução, nomeie o resultado usado, como "pela antissimetria da inclusão". Use texto simples, sem wikilinks entre os vaults nem links `obsidian://`.
- **Quando falta teoria.** Se o acervo não cobre um fundamento necessário, ou o enuncia sem a demonstração de que o argumento precisa, explicite a lacuna no debate. Não preencha em silêncio com teoria externa nem declare a resposta adequada sem resolver essa dependência. Decida com o usuário o estudo e o destino: Extras fora do acervo ou Lacunas do bloco. Não procure nem copie soluções prontas de terceiros.
- **Da prática para a teoria.** Propriedades, testes de leitura e conexões que o exercício esclarece podem voltar ao acervo como `[!insight]` ou aos extras, com justificativa e aprovação.

## A solução continua sendo do usuário

- **Preserve a rota:** estratégia, ordem dos passos, divisão em casos, objetos e modo de pensar. A consolidação organiza a resposta que o usuário chegou a produzir e validar no ciclo de revisão.
- **Oriente a menor mudança necessária.** Mostre o fundamento e ajude a ligar os ingredientes que já estão presentes. Não complete antecipadamente a prova em lugar do usuário. No Exercício 1.1, por exemplo, a inclusão que faltava seria um gap para trabalhar antes de consolidar.
- **Se a rota não funciona,** explique onde falha com a teoria e, quando útil, um contraexemplo. Discuta a parte válida mais próxima e combine a mudança de rota; não a substitua em silêncio.
- **Desvios abandonados** ficam fora da solução; seu papel e o aprendizado efetivamente trabalhado entram no processo. Rotas alternativas vão para os extras, sem substituir a do usuário.
- **Raciocínio recuperável.** A solução intercala a execução com as reflexões que a organizaram, preservando o encadeamento e o nível de detalhe necessário. Ajustes editoriais não podem esconder uma correção matemática ainda não trabalhada.

## Preparar a leitura

- Localize o enunciado em `Images/<livro>/<Capitulo>/Enunciados/` e a tentativa em `Images/<livro>/<Capitulo>/Questões/Q<n>/`. **Leia também `Restos/`.**
- Rode `tinta.py inventario` na pasta da questão. Ele identifica famílias de cor e possíveis versões. Em páginas mistas, use `faixas` para localizar as cores e `camadas` quando precisar separá-las.
- Leia **todas** as imagens por inteiro. Confira visualmente qualquer OCR: posição, agrupamento, setas, rasuras e cor carregam sentido.
- Consulte as notas pertinentes, as soluções existentes do livro e seus dois arquivos de extras. Use os arquivos anteriores para continuidade de notação e exposição; registros antigos de erros não são modelos do novo processo.
- Distinga dúvida de leitura, falta de contexto e erro conceitual. Exponha a incerteza específica antes de tomar uma decisão que dependa dela.

## Diagnosticar e manter o mapa

Leia a tentativa como professor, contribuição por contribuição. Consulte [Diagnóstico e revisão](references/diagnostico.md) para os critérios de acerto, erro de raciocínio, erro de escrita e incompletude. Essas categorias orientam o diagnóstico, não a divisão do documento final.

Antes de propor texto, crie ou atualize `Images/<livro>/<Capitulo>/mapa-cobertura.md`. É memória de trabalho, ignorada pelo git e sem wikilinks. Registre, por exercício, enunciado, hipóteses, diagnóstico e, imagem por imagem, cores, conteúdo digerido, versões, acertos, gaps e destinos possíveis. Acompanhe o desfecho de cada azul e os pedidos verdes.

Durante o debate, registre também cada ciclo: gap trabalhado, notas consultadas, orientação efetivamente dada, resposta do usuário, artefatos relidos e conclusão da revisão. Distinga o que veio do manuscrito, o que o usuário reformulou e o que o agente sugeriu. Estados úteis: **identificado**, **em debate**, **aguardando revisão do usuário**, **revisto com pendência** e **resolvido**, este último sempre com evidência. O mapa permite retomar o trabalho sem inventar uma história de aprendizado.

## Ensinar, aguardar a revisão e reavaliar

**Havendo erros ou omissões, pare a consolidação e converse sobre o gap. Não apresente uma solução integral pronta para aprovação enquanto a tentativa ainda precisa ser aprimorada.**

1. **Delimite o bloqueio.** Diga o que já está correto e escolha o erro, omissão ou grupo dependente de gaps que está impedindo o próximo passo. Foque nele; não sobrecarregue o retorno com a solução completa, todos os extras e os arquivos finais.
2. **Ensine com as notas.** Mostre qual definição, hipótese ou resultado decide o ponto e por que a passagem atual falha ou está incompleta. Use exemplos, contraexemplos e explicações proporcionais à dificuldade. Dê pistas progressivas e aprofunde a explicação quando necessário ou solicitado; a orientação deve permitir que o usuário refaça o argumento.
3. **Devolva a elaboração ao usuário.** Indique concretamente o trecho a refazer, justificar ou acrescentar e aguarde sua revisão. Ele pode reformular o argumento na conversa ou alterar os manuscritos. Um "OK" à explicação não é, por si só, uma nova resolução nem evidência de que o gap foi superado.
4. **Quando ele avisar que alterou, releia.** Confira os arquivos ou argumentos efetivamente revistos, compare com o diagnóstico e avalie a nova versão com o mesmo referencial teórico. Não suponha que a alteração resolveu o problema. Preserve os acertos e procure tanto o gap anterior quanto eventuais problemas introduzidos na revisão.
5. **Repita com foco.** Se ainda houver pendência, explique precisamente o que persiste e retome o ciclo. Se o ponto foi resolvido, diga qual argumento o resolveu e avance ao próximo gap. Registre as intervenções e os resultados no mapa, sem atribuir ao usuário um passo que só o agente escreveu.
6. **Reavalie a resposta inteira.** Só passe à consolidação quando a versão mais recente constituir uma resposta adequada: completa para a tese, correta e fundamentada nas notas. Não confunda melhora parcial, aprovação de uma dica ou cansaço com fechamento. Se houver interrupção ou adiamento, registre a pendência e não declare o exercício concluído.

O foco é vencer o gap real, não conduzir o usuário a reproduzir uma redação do agente. Uma prova válida por outra rota é avaliada pela teoria e discutida conforme a intenção do usuário.

## Preservar o papel das cores

As cores são **famílias de tom**, como em consolidar-manuscritos. Preto com pouca pressão pode parecer cinza; azul pode puxar para anil. Na dúvida, use `tinta.py`. Se a ambiguidade mudar o tratamento, ou surgir uma família diferente, pergunte ao usuário.

- **Preto — operacionalização.** Contas, passagens e demonstração. Se houver gap, ele entra no ciclo de revisão. A solução recebe a execução adequada obtida ao fim do processo, sem narrar o erro anterior.
- **Azul — reflexão.** Pensamentos e organização do caminho. **Todo azul é examinado e debatido.** Se precisar de correção ou desenvolvimento, trabalhe esse gap com o usuário. Na solução, a reflexão validada entra em `> [!note] <Título>`, perto do passo que organiza, com título específico, conceitos em **negrito** e sem wikilinks. Separe ideias distintas. Um azul inteiramente errado fica fora da solução e tem seu tratamento registrado no processo. Conjecturas, analogias e perguntas não se tornam resultados estabelecidos sem justificativa.
- **Verde — metaconversa.** Pedidos de ajuda, dúvidas e instruções para o agente. Responda no debate e aplique as orientações. Não transcreva o verde; extras e insights que ele originar entram com o acordo do usuário.

Uma reflexão corrigida e validada com o usuário continua sendo sua reflexão. O processo registra com fidelidade a ajuda recebida.

## Apresentar o resultado adequado e consolidar

**A aprovação para gravar os arquivos vem depois do ciclo de aprimoramento.** Ela não substitui a revisão da resposta. Se a tentativa já estiver adequada na primeira leitura, siga diretamente para esta apresentação.

Apresente na conversa:

1. A avaliação da versão final, os gaps resolvidos e as evidências que permitiram fechá-los.
2. As respostas aos verdes e o desfecho das reflexões azuis.
3. O rascunho exato da solução em bloco de código Markdown, fiel à resposta adequada do usuário.
4. O resumo do processo de resolução, baseado nas intervenções e revisões efetivamente observadas na conversa.
5. Os extras e insights propostos, com texto, destino e decisões pendentes, cada uma com recomendação.

Aguarde o OK do usuário antes de gravar as notas finais. Se a revisão do rascunho revelar um novo gap matemático, volte ao ciclo de ensino e revisão. As decisões reservadas ao usuário esperam sua escolha; as demais seguem a recomendação apresentada, informada no relatório final. Não classifique como compilado o que ficou adiado.

## Arquivos produzidos

Leia [Arquivos e registro do processo](references/arquivos.md) antes de consolidar.

- `<Livro> vol. N (<Autor>)/Capítulo N/Exercício N.M.md` — **só a resolução final:** enunciado formalizado, reflexões validadas, estratégia e demonstração, sem histórico de versões, debate, páginas ou agente.
- `<Livro> vol. N (<Autor>)/Capítulo N/Exercício N.M - Processo de resolução.md` — **o percurso de aprimoramento:** ponto de partida, gaps, fundamentos consultados, explicações, pistas, conselhos e indicações dados, revisões do usuário e evidência de fechamento. Organize por gap, preservando a sequência dos ciclos em cada um; não é um catálogo de erros remanescentes.
- `<Livro> vol. N (<Autor>)/Extras no acervo.md` e `Extras fora do acervo.md` — conexões com o que já está e com o que ainda não está compilado, por capítulo.
- **No acervo:** callouts `> [!insight] <Título>`, perto do conteúdo pertinente, com as letras da nota que os recebe, conceitos em **negrito**, sem wikilinks e só por inserção. Use o snippet `insight.css` existente. `[!note]` é reservado à reflexão azul.

O novo registro substitui `- Erros.md` nas próximas consolidações. Arquivos antigos permanecem históricos até uma migração solicitada; não os renomeie nem reconstrua ciclos sem a conversa que lhes daria base. O verificador mantém compatibilidade com o formato anterior.

## Escrita matemática

Siga as seções "Critérios de escrita matemática" e "Convenções matemáticas das notas" de [consolidar-manuscritos](../../../../Notas-de-Estudo/.agents/skills/consolidar-manuscritos/SKILL.md), fonte única das convenções dos dois repositórios. Em particular:

- $\subseteq$ é a inclusão ampla; $\subset$ é a estrita. Adapte o $\subset$ amplo do Elon para $\subseteq$.
- $\mathbb N=\{0,1,2,\ldots\}$ e $\mathbb N^*=\{1,2,3,\ldots\}$; o $\mathbb N$ do Elon corresponde a $\mathbb N^*$.
- Explicite quantificadores e preserve hipóteses, objetos e alcance lógico. Nomeie os fundamentos usados, com detalhe suficiente para recuperar o raciocínio.

Formalize o enunciado na abertura, respeitando a organização já aprovada para o exercício. Convenções do livro que o usuário discutiu podem aparecer como reflexões validadas. Novas equivalências de notação vão como proposta para Notações do bloco.

## Ferramentas

O código auxiliar fica em `ferramentas/`. **Não escreva scripts avulsos** para ler cores, conferir delimitadores ou procurar wikilinks: use as ferramentas. Se faltar uma capacidade recorrente, proponha estendê-las, com teste.

Preparação, uma vez por máquina, a partir da raiz do repositório (`.venv` é ignorada pelo git):

```powershell
py -V:3.13 -m venv .venv
.venv\Scripts\python -m pip install -r .agents/skills/consolidar-exercicio/ferramentas/requirements.txt
```

| Comando | Para quê |
|---|---|
| `tinta.py inventario <pasta>` | Famílias de cor e possíveis versões; registrar no mapa. |
| `tinta.py faixas <imagem…>` | Localizar cores, notas de margem e linhas mistas. |
| `tinta.py camadas <imagem…>` | Separar cores em imagens de `<pasta>/.camadas/`. |
| `verificar.py [caminhos…]` | Lint das soluções, registros do processo, extras e notas que receberam insight; aceita registros históricos de erros. |

Execute com `.venv\Scripts\python -X utf8 .agents/skills/consolidar-exercicio/ferramentas/<script> …`. Testes: `.venv\Scripts\python -m unittest discover -s .agents/skills/consolidar-exercicio/ferramentas/testes`.

## Verificar e encerrar

1. Rode `verificar.py` nos arquivos criados ou alterados, incluindo notas que receberam insight, e corrija os erros. Todo gap trabalhado deve ter fundamento identificado; se o acervo não o cobre, registre explicitamente. O lint não comprova correção matemática nem aprendizado.
2. Confira a resposta final com as notas e audite o mapa nos dois sentidos: cada contribuição tem desfecho, cada azul foi tratado, cada verde foi respondido e tudo que foi aprovado está em arquivo identificado. Todo gap da resolução precisa estar resolvido, com evidência da revisão do usuário. Pendências externas à resposta, adiadas por acordo, ficam explícitas.
3. Confira o processo de resolução com a própria conversa: todas as ajudas relevantes, revisões e desfechos estão representados, sem inventar intervenções, autonomia ou domínio demonstrado. A solução contém só o resultado final adequado.
4. Atualize o mapa e informe o que foi consolidado, as decisões tomadas por recomendação e o que ficou pendente.
5. Commit só quando solicitado: um repositório por vez, unidades coerentes, mensagens em inglês e direto na `main`, conforme o histórico. Solucionários e Notas-de-Estudo em commits separados; sem push sem pedido.
