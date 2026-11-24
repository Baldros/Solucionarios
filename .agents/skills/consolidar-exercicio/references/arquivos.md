# Arquivos e registro do processo

A solução e os extras já existentes do Exercício 1.1 orientam a continuidade da exposição. Seu arquivo `- Erros.md` pertence ao fluxo anterior: não é o modelo do novo documento de processo. Não migre arquivos históricos sem solicitação nem invente ciclos de revisão ausentes da conversa.

## Organização

```text
<Livro> vol. N (<Autor>)/
├── Capítulo N/
│   ├── Exercício N.M.md                         ← resolução final adequada
│   └── Exercício N.M - Processo de resolução.md ← percurso de aprimoramento
├── Extras no acervo.md
└── Extras fora do acervo.md
```

A numeração é a do livro: Exercício 1.1 é o primeiro exercício do capítulo 1. As pastas de imagens mantêm os nomes dados pelo usuário. Os novos exercícios produzem o registro de processo em lugar de `- Erros.md`; o verificador ainda aceita os pares históricos de solução e erros.

## A solução

O nome do arquivo é o título. A abertura contém o enunciado formalizado e pode ser `## Enunciado` ou `## Concepção`, conforme a organização aprovada e o modelo atual do exercício.

1. **Enunciado e concepção.** Objetos, hipóteses e tese com quantificadores explícitos e convenções do vault. Preserve a numeração das hipóteses do livro, quando houver. Reflexões validadas sobre a leitura ficam perto do enunciado.
2. **Elaboração.** Estratégia e reflexões que organizam a rota, quando necessárias. Use `[!note]` para os azuis, título específico, conceitos em negrito e nenhum wikilink.
3. **Demonstração ou resolução.** A resposta adequada construída pelo usuário ao longo das revisões, organizada sem perda de passos, fundamentos ou reflexões aproveitáveis. Nomeie cada definição ou resultado que fundamenta um passo. Demonstrações terminam com $\blacksquare$.

Não entram histórico das tentativas, intervenções do agente, referências às páginas, relato dos erros, desvios abandonados ou rotas alternativas. Não complete aqui um gap matemático que o ciclo ainda não resolveu; volte ao debate antes de consolidar. Ajustes de apresentação não devem mudar o significado validado.

## O processo de resolução

O arquivo conta como a resposta foi aprimorada, **com base na conversa e nas revisões observadas**. Registra a ajuda recebida e o que o usuário fez com ela. Não apresenta os problemas iniciais como erros ainda existentes na resposta final.

Abra com um parágrafo que explique a finalidade e use estas seções, nesta ordem:

- `## Ponto de partida` — o que a tentativa inicial já conseguia, seus acertos, a rota escolhida e os gaps que impediam uma resposta adequada.
- `## Ciclos de revisão` — uma entrada `### <título do gap>` por assunto. Dentro de cada entrada, acompanhe a sequência de orientação, revisão do usuário e releitura, inclusive quando foram necessárias várias rodadas.
- `## Síntese do aprendizado` — o que a versão final passou a justificar e quais fundamentos sustentam esse avanço. Distingua o que foi demonstrado nas revisões do que apenas foi discutido ou indicado para estudo posterior. Se não houve gaps nem intervenções, diga isso; não invente um percurso.

Cada entrada deve deixar recuperáveis o gap, a teoria, a ajuda efetivamente dada, a ação do usuário e a evidência de fechamento. Parágrafos corridos ou rodadas numeradas dentro da entrada são adequados; não é preciso transcrever a conversa. Nomeie as notas teóricas em texto simples. Se o acervo não cobre o fundamento, registre isso e o encaminhamento combinado.

Modelo de uma entrada, a preencher somente com fatos observados:

```markdown
### Distinguir uma inclusão de sua recíproca

A tentativa apresentava $X\subseteq Z$ e $Z\supseteq X$ como as duas partes da igualdade. A orientação mostrou, com a definição de inclusão da nota Subconjunto, que eram duas escritas da mesma afirmação, e retomou a antissimetria. Foi pedido ao usuário que reformulasse o sentido ainda ausente.

Na revisão seguinte, o usuário [descrever o argumento efetivamente enviado]. A releitura [registrar o resultado observado]. O gap foi encerrado quando [identificar a justificativa concreta na revisão adequada].
```

O modelo não afirma que esse ciclo aconteceu em um exercício real. Substitua os trechos entre colchetes por evidência da conversa; não os deixe no documento final.

Escreva por conteúdo, sem páginas ou nomes de imagens. Erros de raciocínio, escrita e omissões podem ser identificados no relato de cada gap, mas não constituem seções separadas obrigatórias. Registre as ajudas relevantes mesmo quando foram explicações amplas; não atribua independência ao usuário se o agente forneceu o passo. A ausência de erro na versão final não apaga o caminho percorrido.

## Os extras

- `Extras no acervo.md`: conexões, perspectivas e outras formas de resolver com conteúdo já compilado no Notas-de-Estudo.
- `Extras fora do acervo.md`: pontes com fundamentos ainda não compilados, generalizações e pistas para estudo, identificadas como "a conferir" quando não verificadas.

Os arquivos abrem com sua finalidade e usam `## Capítulo N`. Cada entrada `### <título>` explica a conexão, identifica o exercício de origem e cita as notas pelo nome. Acrescente à seção do capítulo existente. Não duplique conexões anteriores nem antecipe extras durante o trabalho de um gap quando isso desviar o foco.

## Os insights no acervo

Um insight registra o que o exercício esclareceu sobre a teoria: uma propriedade, teste de leitura, identidade ou recurso útil. Deve estar justificado pelo argumento validado ou no próprio texto.

```markdown
> [!insight] A união é o menor conjunto que contém os dois
> Um conjunto $Y$ contém $B$ e $C$ exatamente quando contém a **união**: …
```

Insira perto do conteúdo pertinente, usando as letras da nota que recebe o insight, sem alterar suas linhas existentes. Título específico, conceitos em negrito, nenhum wikilink nem referência ao exercício ou ao agente. Exemplos existentes ficam em Operações de Conjuntos e Subconjunto, no acervo. `[!note]` continua reservado às reflexões azuis.

## O mapa durante as revisões

O mapa `Images/<livro>/<Capitulo>/mapa-cobertura.md` é memória recuperável, ignorada pelo git e sem wikilinks. Mantenha a digestão de todas as imagens, cores, versões, acertos e destinos, além do histórico dos ciclos. Separe os acréscimos da conversa do conteúdo do manuscrito.

```markdown
## Exercício N.M (pasta Q<n>)

Enunciado: … Hipóteses: … Tese: …
Estado: em debate | aguardando revisão do usuário | resposta adequada | aprovado | consolidado.

### Imagens e contribuições
- Q<n>/1.png: conteúdo, cores, diagnóstico, versão e destino.

### Gaps e ciclos
- Gap: … Estado: identificado | em debate | aguardando revisão | revisto com pendência | resolvido.
- Fundamento nas notas: …
- Orientação efetivamente dada: …
- Revisão do usuário e artefatos relidos: …
- Resultado da releitura e evidência de fechamento, quando houver: …

### Destinos e pendências
- Reflexões azuis: desfecho de cada uma.
- Pedidos verdes: resposta e encaminhamento.
- Arquivos finais: propostos | aprovados | consolidados e verificados.
- Pontos adiados por acordo: …
```

Antes de apresentar a consolidação, confira se os gaps da resolução foram resolvidos na versão mais recente. Antes de encerrar, confira se o processo final representa as intervenções relevantes e se cada contribuição tem desfecho. Um mapa detalhado ajuda a retomada, mas não substitui reler uma imagem alterada nem recuperar a conversa quando o registro não for suficiente.
