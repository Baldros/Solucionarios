# Arquivos produzidos

Os arquivos do Exercício 1.1 do *Curso de Análise* são o modelo vivo: `Curso de Análise vol. 1 (Elon)/Capítulo 1/Exercício 1.1.md` e `Exercício 1.1 - Erros.md`, e os dois arquivos de extras do livro. Consulte-os antes de escrever; este guia diz o que cada parte faz e por quê.

## Organização

```
<Livro> vol. N (<Autor>)/           ← título do livro, volume e autor
├── Capítulo N/
│   ├── Exercício N.M.md            ← a solução
│   └── Exercício N.M - Erros.md    ← a qualidade da tentativa
├── Extras no acervo.md
└── Extras fora do acervo.md
```

A numeração é a do livro: Exercício 1.1 é o primeiro exercício do capítulo 1. A pasta de imagens correspondente, em `Images/`, mantém o nome que o usuário deu, como `Analise Vol. 1/Capitulo 1/Questões/Q1`.

## A solução

O nome do arquivo já é o título. O corpo começa por `## Enunciado`, sem repetir o título.

1. **Enunciado.** Formalizado: os objetos, as hipóteses numeradas como no livro, com os quantificadores explícitos, e a tese, na convenção do vault ($\subseteq$, e não o $\subset$ do livro). Logo após vêm as reflexões azuis sobre a leitura do enunciado, se houver.
2. **Seções de elaboração**, como "Leitura das hipóteses" ou "Estratégia". São opcionais e formadas pelas reflexões azuis que organizam o caminho antes da execução. As reflexões são do usuário, corrigidas; uma reflexão surgida no debate só entra se o usuário a aprovar no rascunho.
3. **Demonstração** (ou **Resolução**). É o preto corrigido e completado, na ordem da rota do usuário, e cada passo nomeia o resultado que usa. A reflexão azul que organiza um passo fica junto dele. Fecha com $\blacksquare$ quando é demonstração.

Não entram: menção ao manuscrito, a páginas, ao debate ou ao agente; o desvio abandonado; a narração do erro; rotas alternativas, que vão para os extras; wikilinks.

## O arquivo de erros

Abre com um parágrafo dizendo o que o arquivo é. Depois vêm quatro seções, nessa ordem e com esses nomes, que o `verificar.py` confere:

- `## Avaliação` — um ou dois parágrafos: se a tentativa demonstra o resultado, o que falta, o que travou o caminho e os acertos. É o retrato da qualidade da tentativa.
- `## Erros de raciocínio` — afirmações falsas, passagens inválidas, leituras erradas, circularidades, quantificadores trocados, hipóteses mal usadas.
- `## Erros de escrita` — notação mal formada, símbolo trocado, variável sem introdução, parênteses omitidos, proposição escrita como conjunto.
- `## Incompletudes` — o que ficou faltando ou vago e a solução teve de complementar: passos sem demonstração, justificativas ausentes, quantificadores implícitos, hipóteses não interpretadas. A incompletude decisiva, a que impede a demonstração, vem primeiro.

Cada entrada é um `### <título curto>` seguido de um parágrafo corrido, sem rótulos. O parágrafo diz o que a tentativa fez, citando a escrita dela em notação quando isso ajuda; por que está errado ou incompleto; qual é a forma certa; e qual nota do acervo sustenta a correção, em texto simples, como "(nota Subconjunto)".
- Em erros de raciocínio e incompletudes, a citação da teoria é obrigatória; se o acervo não cobre o assunto, a entrada diz isso.
- Use contraexemplos concretos e ordene as entradas por peso dentro de cada seção.
- Escreva por conteúdo: "numa versão" ou "um dos rascunhos" servem, "página 5" não.
- Uma seção sem entradas continua no arquivo, com uma frase dizendo que não houve erro daquele tipo.

## Os extras

São dois arquivos por livro, com o mesmo formato.

- `Extras no acervo.md` reúne conexões com conteúdo já compilado no Notas-de-Estudo: um resultado do acervo que usa a mesma ideia, uma outra forma de resolver com o que o acervo já tem, uma dualidade com outro exercício.
- `Extras fora do acervo.md` reúne pontes com assuntos que o acervo ainda não tem: outra área, outra perspectiva, uma generalização, uma rota alternativa que depende de teoria não estudada. Traz as pistas de estudo, marcadas como "a conferir".

Os dois abrem com um parágrafo dizendo o que reúnem e se dividem em seções `## Capítulo N`. Cada entrada é um `### <título>` com um parágrafo corrido que diz de que exercício ela vem ("No Exercício 1.1, …") e cita as notas do acervo pelo nome, em texto simples. Uma entrada nova num capítulo que já existe entra na seção dele.

## Os insights no acervo

Um insight é algo que o exercício ensinou sobre a teoria e que merece morar na nota teórica: uma propriedade usada sem estar enunciada no acervo, um teste de leitura, uma identidade que esclarece um erro comum, uma malandragem algébrica. Ele precisa estar justificado, pelo próprio exercício ou por uma linha de argumento no texto.

```markdown
> [!insight] A união é o menor conjunto que contém os dois
> Um conjunto $Y$ contém $B$ e $C$ exatamente quando contém a **união**: …
```

- Vai na nota do acervo cujo conteúdo enriquece, logo depois do trecho a que se refere, separado de outros callouts por uma linha em branco.
- Usa as letras e os nomes da nota que o recebe (em *Operações de Conjuntos*, $B$ e $C$), e não os do exercício.
- O título exprime a ideia, os conceitos ficam em **negrito**, e não há wikilinks nem menção ao exercício, ao livro ou ao Solucionários.
- Entra só por inserção: o diff no acervo não altera nenhuma linha existente.
- Modelos: os três `[!insight]` de *Operações de Conjuntos* e *Subconjunto*, em `../Notas-de-Estudo/Matemática/Teoria dos Conjuntos/`, a partir da raiz.

## O mapa de cobertura

O mapa fica em `Images/<livro>/<Capitulo>/mapa-cobertura.md`, que o git ignora, com uma seção por exercício. O topo do arquivo diz que ele é memória de trabalho, lembra a convenção de cores e lista as notas do acervo usadas como fundamentação.

```markdown
## Exercício N.M (pasta Q<n>)

Enunciado: … Hipóteses: … Tese: …
Estado: <diagnóstico apresentado | aprovado | compilado | concluído> (data).

### Diagnóstico geral
O que a tentativa demonstra, o que falta e as causas.

### Imagens
- **Q<n>/1.png** (preto). Conteúdo digerido. Diagnóstico. Destino: …
- **Q<n>/5.png** (preto + azul na margem). …

### Destinos e estado
- **Compilado — <arquivo>:** o que entrou, e o desfecho de cada azul.
- **Pendente — <item>:** o que falta e por quê.
```

A tabela do `tinta.py inventario` pode ser colada na seção do exercício.
