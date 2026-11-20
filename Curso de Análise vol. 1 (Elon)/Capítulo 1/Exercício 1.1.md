## Enunciado

Dados os conjuntos $A$ e $B$, seja $X$ um conjunto com as propriedades

$$
\begin{aligned}
&(1)\quad A\subseteq X\ \land\ B\subseteq X,\\
&(2)\quad \forall Y:\ \bigl(A\subseteq Y\ \land\ B\subseteq Y\bigr)\implies X\subseteq Y.
\end{aligned}
$$

Prove que $X=A\cup B$.

> [!note] O ⊂ do livro é a inclusão ampla
> O livro escreve as propriedades com $\subset$, que nele é sempre a **inclusão ampla**. A leitura não muda o rigor da resposta, muda o sentido do enunciado: com a **inclusão estrita**, as hipóteses seriam contraditórias. Por (1), o próprio $X$ contém $A$ e $B$; tomando $Y=X$ em (2), viria $X\subset X$, que a estrita nunca admite. Nenhum conjunto satisfaria o enunciado.

## Leitura das hipóteses

> [!note] O menor conjunto que contém A e B
> A propriedade (1) diz que $X$ contém $A$ e $B$; a (2), que $X$ está contido em **todo** conjunto que contém $A$ e $B$. Juntas, dizem que $X$ é o **menor** conjunto que contém $A$ e $B$. As duas são independentes: $A\cup B\cup\{z\}$, com $z\notin A\cup B$, satisfaz (1) mas não (2), que falha para $Y=A\cup B$.

> [!note] Uma inclusão para cada propriedade
> A igualdade se prova por **dupla inclusão**, e cada propriedade fornece uma delas. De (1) sai $A\cup B\subseteq X$. A outra é $X\subseteq A\cup B$, isto é, $\forall x\in X,\ x\in A\cup B$, e sai de (2). A propriedade (2) não é algo a demonstrar: é uma **hipótese universal**, válida para todo $Y$, e se usa **escolhendo** um $Y$ que cumpra sua condição. O candidato é o próprio conjunto a que se quer chegar, $A\cup B$.

## Demonstração

Pela antissimetria da inclusão, basta provar $A\cup B\subseteq X$ e $X\subseteq A\cup B$.

**$A\cup B\subseteq X$.** Seja $x\in A\cup B$. Pela definição de união, $x\in A$ ou $x\in B$. Se $x\in A$, então $x\in X$, pois $A\subseteq X$ por (1); se $x\in B$, então $x\in X$, pois $B\subseteq X$ por (1). Em qualquer caso, $x\in X$.

> [!note] O "ou" já cobre a interseção
> Um elemento de $A\cap B$ não pede tratamento à parte: o "ou" da união é **inclusivo**, e esse elemento cai em qualquer dos dois casos. Também não se pode supor que ele exista. A inclusão é uma afirmação **universal**, sobre cada elemento que se tome, e não garante a existência de nenhum: $A=\{1\}$, $B=\{2\}$ e $X=\{1,2\}$ satisfazem (1) e (2) com $A\cap B=\varnothing$.

**$X\subseteq A\cup B$.** Pela definição de união, $A\subseteq A\cup B$ e $B\subseteq A\cup B$. Assim, $Y=A\cup B$ satisfaz a hipótese de (2), e (2) dá $X\subseteq A\cup B$.

As duas inclusões dão $X=A\cup B$. $\blacksquare$
