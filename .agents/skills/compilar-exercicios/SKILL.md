---
name: compilar-exercicios
description: Compile tentativas manuscritas de exercícios em soluções Markdown para o Obsidian, preservando a rota do usuário e corrigindo-a com base no acervo teórico do Notas-de-Estudo. Use para ler, diagnosticar, discutir e compilar exercícios deste repositório — a solução, o arquivo de erros, os extras do livro e os insights que voltam ao acervo —, preservando o papel das cores e registrando a qualidade da tentativa real.
---

# Compilar exercícios

As imagens em `Images/` são a tentativa manuscrita do usuário de resolver um exercício: uma bagunça de ideias, rascunhos, versões, desvios e reflexões. A tarefa é dissecá-la e estruturá-la numa solução correta e bem organizada, com um storytelling que concatena as etapas, o raciocínio e as reflexões do usuário. Cada exercício gera dois arquivos: a **solução**, que é o que a tentativa vira quando corrigida e completada, e o **arquivo de erros**, que registra a qualidade da tentativa real.

O trabalho combina leitura, diagnóstico, debate e escrita matemática. O agente atua como professor: aponta os erros, corrige, fundamenta e discute. A solução, porém, continua sendo do usuário.

## A solução é do usuário

Esta é a espinha dorsal da skill.

- **Preserve a rota.** A solução compilada segue o caminho que o usuário tomou: a estratégia, a ordem dos passos, a divisão em casos, os objetos escolhidos e o modo de pensar, ainda que não seja o caminho usual dos livros. O objetivo não é a solução canônica do exercício, e sim a do usuário, correta.
- **Repare o mínimo.** Corrija com a menor mudança que mantém a rota e complete com o passo que a própria rota pede. No Exercício 1.1, a tentativa já fazia a dupla inclusão e já tinha os dois ingredientes; faltava aplicar a hipótese universal com $Y=A\cup B$. A solução acrescentou esse passo e manteve todo o resto.
- **Fundamente no acervo.** Toda correção e todo complemento vêm do material teórico do Notas-de-Estudo (veja a seção seguinte). Não se copia solução de terceiros, publicada ou não, nem se procura a resposta pronta. Quando o acervo não basta, isso vira ponto de debate, não atalho.
- **Se a rota não funciona,** mostre por quê no debate, com a teoria e, se couber, um contraexemplo, e construa a solução a partir da parte válida mais próxima do que o usuário fez. Nunca troque de rota em silêncio: a troca só acontece com o acordo dele.
- **Desvios abandonados** não entram na solução. A lição que deixaram entra como reflexão azul corrigida, quando ilumina a rota; os erros que contêm vão para o arquivo de erros.
- **Rotas alternativas,** inclusive a usual ou a mais elegante, vão para os extras como outra forma de resolver. Nunca substituem a do usuário.
- **Storytelling.** A solução intercala a execução (preto) com as reflexões que a organizaram (azul), para que se veja como ela foi concebida, e não só o resultado.

## A ponte com a teoria

É o segundo pilar: teoria e prática se alimentam nos dois sentidos.

- **Da teoria para a prática.** Antes de corrigir, localize no acervo (`../Notas-de-Estudo/Matemática/`, a partir da raiz do repositório) a definição ou o resultado que decide a questão, junto com os arquivos de Notações e de Lacunas do bloco. A correção se apoia nele e, no debate e no arquivo de erros, cita a nota pelo nome. O contraexemplo, quando houver, vem da mesma base.
- **Na solução,** todo passo que usa um resultado o nomeia, como "pela antissimetria da inclusão" ou "pela definição de união", para que se veja qual teoria opera em cada passo. A citação é em texto simples: sem wikilinks, porque são vaults separados, e sem links `obsidian://`.
- **No arquivo de erros,** toda entrada de erro de raciocínio e de incompletude diz em que nota está a teoria que sustenta a correção, ou diz que o acervo não cobre o assunto.
- **Quando falta teoria.** Se a solução precisa de um resultado que o acervo não tem, ou que ele enuncia sem demonstrar, aponte isso no debate, sem preencher em silêncio com teoria de fora. O destino, Extras fora do acervo ou o arquivo de Lacunas do bloco no acervo, é decidido com o usuário.
- **Da prática para a teoria.** O que o exercício ensina sobre a teoria — uma propriedade usada sem estar enunciada, um teste de leitura, uma identidade que esclarece um erro, uma malandragem algébrica — volta ao acervo como `[!insight]`. Conexões com o que já está compilado vão para Extras no acervo.

## Preparar a leitura

- Localize o enunciado em `Images/<livro>/<Capitulo>/Enunciados/` e a tentativa em `Images/<livro>/<Capitulo>/Questões/Q<n>/`. **A pasta `Restos/` faz parte da tentativa** e é lida como as outras.
- Rode `tinta.py inventario` na pasta da questão (veja "Ferramentas"). Ele dá as famílias de cor de cada imagem e aponta possíveis versões, como uma página fotografada antes de ser continuada. Em páginas com cores misturadas, `tinta.py faixas` diz onde está cada cor, e `tinta.py camadas` separa as cores em imagens próprias.
- Leia **todas** as imagens por inteiro. A ferramenta orienta, mas quem decide é a imagem: posição, agrupamento, setas, rasuras e cor também carregam sentido. Não confie em OCR sem conferir na imagem.
- Leia as notas pertinentes do acervo, as soluções já compiladas do livro, para manter a continuidade de notação e de estilo, e os dois arquivos de extras do livro.
- Distinga dúvida de leitura, falta de contexto e erro conceitual. Exponha a incerteza específica antes de decidir algo que dependa dela.

## Preservar o papel das cores

As cores seguem a linha da skill consolidar-manuscritos: são **famílias de tom**, não valores hexadecimais. O traço com menos pressão parece cinza, mas é preto; um azul pode puxar para o anil. Na dúvida, meça com `tinta.py`. Se a ambiguidade mudar o tratamento do conteúdo, pergunte ao usuário. Uma cor fora das três famílias também pede pergunta.

- **Preto — operacionalização.** É a solução de fato: as contas, as passagens, a demonstração. Entra no corpo da solução já corrigido e completado, sem narrar o erro anterior, e o erro vai para o arquivo de erros.
- **Azul — reflexão.** São os pensamentos do usuário, as estruturações, a organização da ideia: a elaboração do caminho. **Todo texto azul passa por escrutínio**, como na consolidar-manuscritos: revise o conteúdo, debata-o e proponha as correções necessárias. Ele entra na solução já corrigido, com a intenção preservada e sem narrar o erro, num bloco `> [!note] <Título>` perto do passo que organiza. O título é curto e exprime a ideia, como `> [!note] O "ou" já cobre a interseção`, nunca genérico. Dentro do bloco, use **negrito** para conceitos e não use wikilinks. Reflexões com ideias distintas vão em blocos distintos. Um azul todo errado não entra, mas o erro dele vai para o arquivo de erros. Uma conjectura, analogia ou pergunta não vira resultado estabelecido.
- **Verde — metaconversa.** São comentários e orientações que o usuário deixa para o agente: pedidos de ajuda, dúvidas sobre o livro, instruções de apresentação. Responda a eles no debate e aplique as orientações. O verde não é transcrito; o que ele originar, como um extra ou um insight, só entra com o acordo do usuário.

A correção de um texto azul não muda sua autoria: ele continua sendo a reflexão do usuário.

## Dissecar a tentativa

Leia a tentativa como um professor que corrige uma prova, contribuição por contribuição. Os critérios e exemplos estão em [Diagnóstico](references/diagnostico.md).

- Classifique cada contribuição como **acerto**, **erro de raciocínio**, **erro de escrita** ou **incompletude**, que é o que ficou faltando ou vago e a solução precisa complementar.
- Reconheça versões (uma página que reescreve outra), desvios (caminhos abandonados) e o fio principal da tentativa, que é a rota que a solução vai preservar.
- Teste a leitura do enunciado: convenções de notação do livro, quantificadores implícitos, consistência das hipóteses sob cada leitura possível.
- Para cada correção, encontre a teoria do acervo que a sustenta e, quando uma afirmação é falsa, um contraexemplo concreto.
- Registre também os acertos: eles fazem parte do retrato da qualidade da tentativa.

## Mapear a cobertura

Antes de propor qualquer texto, crie ou atualize o **mapa de cobertura** em `Images/<livro>/<Capitulo>/mapa-cobertura.md`, com uma seção por exercício. A pasta é ignorada pelo git; o mapa é memória de trabalho, não nota, e não leva wikilinks.

Na seção do exercício, registre o enunciado e as hipóteses, o diagnóstico geral e, imagem por imagem, a cor, o conteúdo digerido (não transcrito), o diagnóstico e o destino proposto: solução, arquivo de erros, extra, insight ou só debate. Agrupe imagens contíguas do mesmo assunto, deixando claro quais foram consideradas. Ao longo do trabalho, acompanhe o estado de cada contribuição e o desfecho de cada azul (entrou correto, entrou corrigido ou ficou de fora por estar todo errado) e registre à parte o que surgiu na conversa. Use o mapa para retomar o trabalho depois de pausas; volte à imagem quando ele não bastar.

## Apresentar e aguardar aprovação

Nada é compilado antes do OK do usuário. A apresentação, na conversa, traz:

1. **Veredito:** o que a tentativa demonstra, o que falta e o que travou o caminho.
2. **Correções por tema,** cada uma com a teoria do acervo que a sustenta. Na conversa, pode-se citar as páginas.
3. **Resposta aos verdes.**
4. **Rascunho exato da solução,** num bloco de código Markdown, como vai para o arquivo.
5. **Resumo do arquivo de erros:** a avaliação e as entradas de cada categoria.
6. **Insights e extras propostos,** com destino e texto.
7. **Decisões pendentes,** cada uma com uma recomendação.

Debata e refine. Quando o usuário aprovar o rascunho, compile todos os arquivos do exercício. As decisões que o usuário reservou para si esperam a escolha dele; as demais seguem a recomendação apresentada, e o relatório final diz isso. Se a leitura aprofundada revelar algo não mapeado, atualize o mapa e apresente o ponto antes de compilá-lo.

## Arquivos produzidos

A anatomia, os modelos e os exemplos estão em [Arquivos](references/arquivos.md). Os arquivos do Exercício 1.1 são o modelo vivo.

- `<Livro> vol. N (<Autor>)/Capítulo N/Exercício N.M.md` — **só a solução:** o enunciado formalizado, as reflexões azuis corrigidas e a solução. Nada sobre o manuscrito, as páginas, o debate ou o agente.
- `<Livro> vol. N (<Autor>)/Capítulo N/Exercício N.M - Erros.md` — **a qualidade da tentativa real:** Avaliação (com os acertos), Erros de raciocínio, Erros de escrita e Incompletudes. Escrito por conteúdo, nunca por página.
- `<Livro> vol. N (<Autor>)/Extras no acervo.md` e `Extras fora do acervo.md` — conexões com o que já está e com o que não está compilado no Notas-de-Estudo, por capítulo. A separação serve à meta-análise do estudo.
- **No acervo,** callouts `> [!insight] <Título>`, âmbar e com ícone de lâmpada, pelo snippet `.obsidian/snippets/insight.css` que já existe no Notas-de-Estudo. Ficam perto do conteúdo a que se referem e seguem as regras de callout da consolidar-manuscritos: título que exprime a ideia, conceitos em negrito, sem wikilinks. Usam as letras da nota que os recebe e entram só por inserção, sem alterar o conteúdo existente. Nunca use `[!note]` para um insight: `[!note]` é a reflexão azul.

## Escrita matemática

Leia e siga as seções "Critérios de escrita matemática" e "Convenções matemáticas das notas" da skill [consolidar-manuscritos](../../../../Notas-de-Estudo/.agents/skills/consolidar-manuscritos/SKILL.md) (`../Notas-de-Estudo/.agents/skills/consolidar-manuscritos/SKILL.md`, a partir da raiz). Elas são a fonte única das convenções dos dois repositórios. Em particular:

- $\subseteq$ é a inclusão ampla e $\subset$ a estrita. Muitos livros, como o *Curso de Análise* do Elon, usam $\subset$ para a ampla: confira a convenção do livro e escreva $\subseteq$.
- $\mathbb N=\{0,1,2,\ldots\}$ e $\mathbb N^*=\{1,2,3,\ldots\}$; o $\mathbb N$ do Elon é o $\mathbb N^*$ do vault.
- Use notação lógica e quantificacional quando ela preservar o sentido, com os quantificadores explícitos, sobretudo os que o livro deixa implícitos.

O enunciado entra formalizado, com os quantificadores explícitos. Uma convenção do livro que muda a leitura do exercício aparece na solução quando o usuário refletiu sobre ela, como reflexão azul corrigida. Uma equivalência de notação nova vira proposta para o arquivo de Notações do bloco no acervo.

## Ferramentas

O código auxiliar fica em `ferramentas/`, nesta pasta. **Não escreva scripts avulsos** para ler cores, conferir delimitadores ou procurar wikilinks: use as ferramentas. Se surgir uma necessidade recorrente que elas não cobrem, proponha ao usuário estendê-las, com teste.

Preparação, uma vez por máquina, a partir da raiz do repositório (a `.venv` é ignorada pelo git):

```powershell
py -V:3.13 -m venv .venv
.venv\Scripts\python -m pip install -r .agents/skills/compilar-exercicios/ferramentas/requirements.txt
```

| Comando | Para quê |
|---|---|
| `tinta.py inventario <pasta>` | Famílias de cor por imagem e possíveis versões; a saída vai para o mapa. |
| `tinta.py faixas <imagem…>` | Onde está cada cor, faixa por faixa; aponta notas de margem e linhas mistas. |
| `tinta.py camadas <imagem…>` | Uma imagem por cor, em `<pasta>/.camadas/`, para ler cada camada separada. |
| `verificar.py [caminhos…]` | Lint dos arquivos compilados e das notas do acervo que receberam insight. |

Os comandos rodam como `.venv\Scripts\python .agents/skills/compilar-exercicios/ferramentas/<script> …`. Os testes, como `.venv\Scripts\python -m unittest discover -s .agents/skills/compilar-exercicios/ferramentas/testes`.

## Verificar e encerrar

1. Rode `verificar.py` nos arquivos criados ou alterados, inclusive nas notas do acervo que receberam insight, e corrija todo erro. Um aviso de "ponte" só pode sobrar se a entrada disser que o acervo não cobre o assunto.
2. **Condição de parada.** Releia a lista de imagens e confira, nos dois sentidos: cada contribuição do manuscrito tem desfecho no mapa; toda correção feita está no arquivo de erros; todo azul tem desfecho; tudo o que foi aprovado está num arquivo identificado; todos os verdes foram respondidos. O que foi adiado por acordo fica explícito, sem ser classificado como compilado.
3. Atualize o mapa com o estado final e informe o que foi feito, as decisões tomadas por recomendação e o que ficou pendente.
4. Commit só quando o usuário pedir: um repositório por vez, em unidades coerentes, com o Solucionários e o Notas-de-Estudo em commits separados, mensagem em inglês e direto na `main`, como no histórico. Sem push sem pedido.
