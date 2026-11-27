# Arquivos e memória de trabalho

A solução, o Processo e as contribuições ao acervo são entregas separadas, produzidas nessa ordem e com aprovações próprias. A solução anterior do livro orienta notação e nível de exposição. Registros antigos de erros e Processos narrativos permanecem históricos, salvo revisão expressamente solicitada.

## Organização e estados

```text
<Livro> vol. N (<Autor>)/
├── Capítulo N/
│   ├── Exercício N.M.md
│   └── Exercício N.M - Processo de resolução.md
├── Extras no acervo.md
└── Extras fora do acervo.md
```

A numeração é a do livro. As pastas de imagens mantêm seus nomes originais. Não crie um novo arquivo de erros: o Processo técnico o substitui para novas consolidações. O verificador continua aceitando os pares e estruturas históricos.

A memória de trabalho deve identificar separadamente os estados da solução, do Processo e das contribuições ao acervo: em elaboração, apresentado, aprovado, gravado e verificado, além de pendências ou adiamentos explícitos. Uma etapa não é concluída apenas porque a anterior foi aprovada.

## A solução

O nome do arquivo é o título. Abra com `## Enunciado` ou `## Concepção`, seguindo a organização aprovada e a continuidade do livro. Formalize objetos, hipóteses, tese e quantificadores; preserve a numeração das propriedades quando houver.

Conserve a estratégia, os passos e as reflexões validadas, com detalhe suficiente para recuperar o raciocínio. Use `[!note]` com título específico para as reflexões azuis, junto ao passo que organizam, e destaque os conceitos em **negrito**. Nomeie os fundamentos matemáticos usados. Demonstrações terminam com $\blacksquare$.

A solução contém apenas a resposta final adequada. Não recebe relato de erros, versões, debate, participantes ou localização dos manuscritos. Um desenvolvimento iniciado em vermelho contribui com sua execução corrigida; sua frase de abertura não vira uma reflexão da solução. Desvios abandonados pertencem ao Processo, quando ajudam a entender a correção; rotas alternativas podem ser propostas posteriormente como extras.

Após aprovar e gravar a solução, rode `verificar.py --etapa solucao <arquivo>`. A opção permite apenas a ausência temporária do Processo; mantém as demais regras. Não crie um Processo vazio para satisfazer o verificador. Depois da aprovação própria do Processo, faça a verificação completa do par, sem essa dispensa.

## O Processo de resolução

O documento mapeia os problemas efetivamente identificados e o desenvolvimento matemático das correções. A conversa e as tentativas são fontes de evidência; o texto final é orientado ao conteúdo estudado.

Use estas seções, nesta ordem:

- `## Abordagem inicial`: concepção, estratégia, argumentos válidos e dependências ainda abertas na tentativa de partida.
- `## Problemas e correções`: uma entrada `###` por assunto, com o problema, seu tipo, o fundamento teórico, o desenvolvimento corretivo e a justificativa final. Se houver várias revisões relevantes, preserve a evolução das ideias sem narrar as interações.
- `## Síntese técnica`: o que a resposta passou a justificar, os fundamentos que a sustentam e as pendências externas ao escopo concluído.

Registre também os lapsos de atenção trabalhados. Diferencie uma correção de escrita de uma mudança conceitual ou do preenchimento de uma omissão. A entrada pode reunir camadas dependentes, desde que explique separadamente seus efeitos. Nomeie as notas teóricas em texto simples; se o acervo não cobrir um fundamento, explicite a ausência e o encaminhamento pertinente.

Exemplo de exposição técnica:

```markdown
### Separar a inclusão repetida da justificativa ausente

Havia duas escritas de uma única inclusão: $X\subseteq Z$ e $Z\supseteq X$. O lapso de escrita era a direção da segunda expressão, cujo alvo era $Z\subseteq X$. Mesmo corrigido o símbolo, faltava justificar essa inclusão.

Pela nota Subconjunto, $Z\subseteq X$ exige começar com um elemento arbitrário de $Z$ e demonstrar sua pertinência a $X$. No caso $Z=A\cap B$, definir $Y$ por todos os elementos comuns torna $Y=Z$. Verificadas as condições da hipótese universal, obtém-se $Y\subseteq X$, logo $Z\subseteq X$. A antissimetria então fornece $X=Z$.
```

Preserve explicações, distinções, exemplos e contraexemplos que contribuam para o estudo. Retire fórmulas como “o usuário pediu”, “o agente explicou”, relatos de ferramentas, divergências de leitura, sequência de mensagens, autorizações e avaliações de autonomia ou domínio pessoal. Trocar esses sujeitos por voz passiva não torna um relato do chat técnico: o objeto de cada parágrafo deve ser o argumento matemático ou sua correção.

Não invente uma evolução ausente. Pontos apenas discutidos não viram correções concluídas; registre o alcance matemático efetivamente estabelecido. Quando não houver problemas, diga que a abordagem já atendia ao referencial, sem criar entradas artificiais. Apêndices adiados por acordo podem ser identificados brevemente como pendentes, sem desenvolver ou declarar encerrados seus gaps.

Na consolidação, apresente o texto para revisão e aguarde aprovação própria antes de gravar. O formato histórico `Ponto de partida / Ciclos de revisão / Síntese do aprendizado` continua legível pelo verificador; novas produções usam o formato técnico acima.

## Extras e insights: etapa posterior

Depois de consolidar solução e Processo, avalie o retorno ao material teórico. Confira o conteúdo existente antes de propor entradas e apresente cada texto com destino, fundamento e recomendação para aprovação específica.

- `Extras no acervo.md`: conexões e perspectivas que usam conteúdo já compilado.
- `Extras fora do acervo.md`: fundamentos ainda não compilados, generalizações e pistas de estudo, marcados como “a conferir” quando não verificados.
- Notas teóricas: insights justificados que acrescentem uma propriedade, conexão ou recurso útil ao estudo.

Os extras abrem com sua finalidade, usam `## Capítulo N` e entradas `###` por tema. Identifique o exercício de origem e cite as notas por nome. Acrescente à seção existente do capítulo e evite duplicações.

Nas notas teóricas, insira `> [!insight] <Título específico>` perto do conteúdo pertinente, usando as letras da nota de destino, conceitos em **negrito**, sem wikilinks no callout nem referência ao exercício ou aos participantes. Preserve o conteúdo existente por inserção e use o snippet `insight.css` disponível. `[!note]` continua reservado à reflexão azul no fluxo dos exercícios.

Exemplos de conteúdo a conferir antes de propor:

- A união é o **menor conjunto que contém ambos**: $B\subseteq Y\land C\subseteq Y\iff B\cup C\subseteq Y$.
- A interseção é o **maior conjunto contido em ambos**: $Y\subseteq B\land Y\subseteq C\iff Y\subseteq B\cap C$.

O resultado, seus sentidos e o alcance das hipóteses precisam estar justificados. Se a nota já desenvolve o mesmo ponto, não crie outro callout equivalente. Nenhuma proposta é inserida automaticamente por ter surgido na resolução.

## Memória de trabalho durante as revisões

O mapa `Images/<livro>/<Capitulo>/mapa-cobertura.md` é memória recuperável, ignorada pelo git e sem wikilinks. Nele, a localização dos manuscritos e o histórico das intervenções são úteis para retomar o trabalho. Eles não pertencem ao Processo técnico.

As páginas corrigidas e seus roteiros, em `.correcoes/` ao lado de cada imagem, também são material de trabalho: mostram o que foi marcado na última rodada daquela página. Não substituem o registro do diagnóstico no mapa nem entram na solução ou no Processo.

Registre por exercício:

- Enunciado, hipóteses, tese e concepção.
- Conteúdo de cada imagem, cores, versões e relação das inserções `x.1`, `x.2` com os trechos corrigidos. Diferencie acréscimo, substituição parcial e versão anterior, sem inferir isso apenas do nome.
- Diagnóstico por problema: tipo, evidência, teoria, impacto, orientação efetivamente dada, reformulações e resultado da releitura.
- Argumento que fecha cada ponto, ou pendência específica; não atribua uma elaboração autônoma se o passo só foi fornecido como orientação.
- Destino de cada reflexão azul, resposta aos verdes e escopo dos desenvolvimentos iniciados em vermelho.
- Aprovações, escopo consolidado, apêndices adiados por acordo e estado de cada entrega.

Um mapa detalhado não substitui reler uma imagem alterada nem permite inventar intervenções. Antes de fechar uma etapa, confira os artefatos correspondentes, suas aprovações e a cobertura do escopo. Antes de gravar o Processo, selecione dessa memória apenas o conteúdo técnico que explica os problemas e suas correções.
