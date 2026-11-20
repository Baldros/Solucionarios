Conteúdos que se relacionam com as soluções deste livro e ainda não estão compilados no Notas-de-Estudo: outra forma de resolver, outra forma de ver ou uma ponte com um assunto ainda não estudado. As pistas de estudo vieram do debate com o agente e ainda precisam ser conferidas.

## Capítulo 1

### A união como supremo

No Exercício 1.1, a propriedade (1) diz que $X$ é uma cota superior de $A$ e $B$ na relação de inclusão, e a (2), que $X$ está abaixo de todas as cotas superiores. A inclusão é reflexiva, antissimétrica e transitiva, como registra a nota Subconjunto, isto é, uma ordem parcial em $\mathcal P(E)$; o exercício mostra que $A\cup B$ é o supremo de $\{A,B\}$ nessa ordem. O Exercício 1.2 faz o mesmo com a interseção, que é o ínfimo. Um conjunto parcialmente ordenado em que todo par tem supremo e ínfimo é um reticulado, e $\mathcal P(E)$ é um. O supremo de um conjunto de números reais, no estudo dos números reais, tem a mesma forma: uma cota superior que está abaixo de qualquer outra. Falta estudar ordens parciais e reticulados. Uma pista a conferir é Halmos, *Naive Set Theory*, §14; outra, Davey & Priestley, *Introduction to Lattices and Order*, cap. 2.

### Unicidade pelo argumento cruzado

Uma segunda solução do Exercício 1.1 separa existência e unicidade. Existência: $A\cup B$ satisfaz (1), pela definição de união, e (2), porque $A\subseteq Y$ e $B\subseteq Y$ dão $A\cup B\subseteq Y$, como na primeira inclusão da solução. Unicidade: se $X$ e $X'$ satisfazem (1) e (2), a propriedade (2) de $X$ aplicada a $Y=X'$ dá $X\subseteq X'$, a de $X'$ aplicada a $Y=X$ dá $X'\subseteq X$, e a antissimetria dá $X=X'$. Logo todo $X$ com (1) e (2) é igual a $A\cup B$. O argumento não usa elementos, só as propriedades da inclusão, e é o molde da unicidade do supremo e, em geral, de objetos caracterizados por serem os menores, ou os maiores, com uma propriedade. Na teoria das categorias, essa forma de caracterizar um objeto é a de uma propriedade universal.

### Prova por casos

A parte $A\cup B\subseteq X$ do Exercício 1.1 é uma prova por casos: para concluir $x\in X$ de "$x\in A$ ou $x\in B$", basta concluí-lo de cada alternativa. Na lógica proposicional, é a equivalência

$$
\bigl((P\implies R)\land(Q\implies R)\bigr)\iff\bigl((P\lor Q)\implies R\bigr).
$$

Com $P$, $Q$ e $R$ as afirmações $x\in A$, $x\in B$ e $x\in Y$, quantificadas em $x$, ela se torna $A\subseteq Y\land B\subseteq Y\iff A\cup B\subseteq Y$, pela correspondência entre implicação e inclusão da nota Subconjunto e pela distribuição do quantificador universal sobre a conjunção. O acervo não tem notas de lógica. Falta estudar o cálculo proposicional e as regras de inferência, como a prova por casos. Uma pista a conferir é Tarski, *Introduction to Logic*, que o próprio *Curso de Análise* recomenda.
