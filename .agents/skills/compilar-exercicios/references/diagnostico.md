# Diagnóstico da tentativa

Como dissecar a tentativa manuscrita. As categorias são as do arquivo de erros. Os exemplos vêm do Exercício 1.1 e mostram o tipo de coisa a procurar, sem esgotar o que pode aparecer.

## Ler o enunciado antes da tentativa

- **Convenção de notação do livro.** Confira o sentido dos símbolos no livro antes de julgar a tentativa. O $\subset$ do Elon é a inclusão ampla (nota Notações de Teoria dos Conjuntos, no acervo).
- **Teste de consistência.** Leia as hipóteses sob cada interpretação possível. Se uma leitura as torna contraditórias, ela não é a do autor. No 1.1, com $\subset$ estrito, tomar $Y=X$ exigiria $X\subset X$.
- **Quantificadores implícitos.** "Se $Y\supset A$ e $Y\supset B$, então $Y\supset X$" vale para todo $Y$. Explicite-os ao formalizar; muitas vezes é o quantificador que permite o passo decisivo.
- **O que as hipóteses dizem juntas.** Uma interpretação, como "$X$ é o menor conjunto que contém $A$ e $B$", costuma sugerir a estratégia.

## Mapear a tentativa

- **Versões.** Uma imagem pode ser a anterior de outra (o `tinta.py inventario` aponta) ou uma reescrita do mesmo trecho. O diagnóstico vale para a versão final. Um erro que a própria tentativa corrigiu numa versão posterior entra no arquivo de erros, dizendo que foi corrigido.
- **Fio principal e desvios.** Identifique a rota que leva, ou levaria, à tese: é ela que a solução preserva. Desvio é um caminho que se afasta da tese. Descubra o que o motivou; no 1.1, foi a busca de um elemento em $A\cap B$, que levou a uma longa conta com complementares.
- **Ingredientes já presentes.** Muitas vezes a tentativa já tem as peças e falta só ligá-las. Mostre isso no veredito: é a forma mais útil de correção, e a que mais preserva a rota.

## Categorias

### Acertos

Estratégias corretas, dúvidas que procediam, contradições detectadas, autoavaliações exatas e passos corretos, ainda que mal escritos. Entram na Avaliação. Uma dúvida do usuário que procedia é acerto, mesmo que a tentativa não a tenha resolvido.

### Erros de raciocínio

- Conclusão declarada sem demonstração completa.
- Hipótese tratada como algo a provar; hipótese universal não instanciada.
- Símbolo ou convenção lidos com o sentido errado.
- Existência afirmada sem base, como supor $A\cap B\neq\varnothing$. Refute com um contraexemplo que satisfaz as hipóteses.
- Quantificador ou conectivo trocado: $\exists$ por $\forall$, "ou" por "e".
- Circularidade: partir da tese.
- Hipótese apresentada como resultado.
- Dependência inventada entre hipóteses, como afirmar que (2) segue de (1). Um objeto que satisfaz uma e não a outra mostra a independência.
- Erro lógico: "não implica $P$" lido como "implica $\neg P$"; negação mal feita. A negação de $\forall y\in Y,\ y\in X$ é $\exists y\in Y,\ y\notin X$ (nota Subconjunto, "Negar a inclusão").
- Identidade falsa, como $\complement(A\cap B)=A\,\Delta\,B$, e manipulação algébrica sem regra que a sustente.
- Objetos confundidos, como o conjunto fundamental e o menor conjunto que contém $A$ e $B$.

### Erros de escrita

- Proposição escrita como conjunto, com chaves em volta de uma afirmação.
- Símbolo trocado: $\subseteq$ por $\supseteq$, $\in$ por $\subseteq$, $\iff$ por $\implies$, $\equiv$ entre coisas de tipos diferentes.
- Quantificador mal formado: limitado a um conjunto e regendo uma equivalência, ou com duas variáveis.
- Variável livre, sem introdução.
- Parênteses omitidos onde a precedência não é convencional, como entre $\cup$ e $\cap$.

### Incompletudes

- A parte da demonstração que falta: é a incompletude decisiva, e vem primeiro.
- Passo verdadeiro afirmado sem argumento.
- Método usado sem justificativa, como a dupla inclusão sem a antissimetria.
- Quantificador implícito deixado implícito, quando é ele que permite o passo.
- Hipóteses não interpretadas.

## Como corrigir

- Para cada item, diga o que a tentativa fez, por que está errado ou incompleto, qual é a forma certa e que nota do acervo a sustenta. Se a afirmação é falsa, dê um contraexemplo.
- Prefira a menor correção que mantém a rota.
- Separe erro de escolha legítima diferente da usual: uma escolha legítima não é erro e é preservada.
- Se a correção exigir teoria que o acervo não tem, aponte isso em vez de buscá-la fora em silêncio.

## Apresentar o diagnóstico

O veredito vem primeiro e é direto, como "a tentativa prova só metade". Depois vêm as correções agrupadas por tema, e não por página, porque um mesmo erro costuma reaparecer em várias páginas; cite as páginas entre parênteses para o usuário localizar. Diga também o que estava certo.
