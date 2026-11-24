## Concepção

Dados os conjuntos $A$ e $B$, seja $X$ um conjunto com as seguintes propriedades:

$$
\begin{aligned}
&(1)\quad X\subseteq A\ \land\ X\subseteq B,\\
&(2)\quad \forall Y:\ \bigl(Y\subseteq A\ \land\ Y\subseteq B\bigr)\implies Y\subseteq X.
\end{aligned}
$$

Vamos demonstrar que $X=A\cap B$.

> [!note] Adaptar a caracterização da união à interseção
> A caracterização da **união** descreve o menor conjunto que contém $A$ e $B$. Para a **interseção**, as inclusões mudam de sentido: procuramos um conjunto contido em ambos e que contenha qualquer outro conjunto com essa propriedade. Assim, $X$ deve ser o **maior conjunto contido em $A$ e em $B$**. A formulação das propriedades se adapta, e o método de provar a igualdade por **dupla inclusão** continua como estratégia válida.

Pelo **axioma da extensão**, provar $X=A\cap B$ é provar que os conjuntos possuem exatamente os mesmos elementos:

$$
\forall x:\quad\bigl(x\in X\iff x\in A\cap B\bigr).
$$

A equivalência exige os dois sentidos. Pela definição de inclusão, eles se escrevem como

$$
\begin{aligned}
X\subseteq A\cap B
&\iff\forall x:\ \bigl(x\in X\implies x\in A\cap B\bigr),\\[4pt]
A\cap B\subseteq X
&\iff\forall x:\ \bigl(x\in A\cap B\implies x\in X\bigr).
\end{aligned}
$$

Precisamos, portanto, demonstrar as duas inclusões conjuntamente. A **antissimetria da inclusão** permitirá concluir a igualdade.

> [!note] A dupla inclusão acompanha o mesmo elemento
> Mostrar que todo elemento de $X$ também pertence a $A\cap B$ pode ser escrito como
> $$
> \forall x\in X,\ \exists u\in A\cap B:\ x=u.
> $$
> O elemento $u$ cuja existência se afirma é o **próprio $x$**, agora reconhecido como elemento da interseção. No sentido contrário, queremos
> $$
> \forall u\in A\cap B,\ \exists x\in X:\ u=x.
> $$
> Podemos acompanhar uma única letra em cada parte da prova: começar com um elemento de um conjunto e verificar que **esse mesmo elemento** pertence ao outro. Provar que os conjuntos têm os mesmos elementos e usar a **antissimetria** são duas apresentações do mesmo critério de igualdade.

## Demonstração

### Primeira inclusão: de X para A∩B

Pela propriedade (1), temos $X\subseteq A$ e $X\subseteq B$. Pela definição de inclusão,

$$
\begin{aligned}
&\forall x:\quad x\in X\implies x\in A,\\
&\forall x:\quad x\in X\implies x\in B.
\end{aligned}
$$

Seja $x\in X$ um elemento arbitrário. As duas afirmações se aplicam a esse mesmo elemento, de modo que $x\in A$ e $x\in B$. Pela definição de interseção,

$$
x\in A\cap B\iff\bigl(x\in A\ \land\ x\in B\bigr).
$$

Logo, $x\in A\cap B$. Como $x$ foi tomado arbitrariamente em $X$, demonstramos que

$$
\forall x:\quad x\in X\implies x\in A\cap B,
$$

isto é,

$$
X\subseteq A\cap B.
$$

### Segunda inclusão: de A∩B para X

Agora precisamos começar com os elementos de $A\cap B$ e verificar que pertencem a $X$. Para isso, vamos usar a propriedade (2).

Se $Y$ é um conjunto tal que $Y\subseteq A$ e $Y\subseteq B$, então cada $y\in Y$ pertence a $A$ e a $B$. Pela definição de interseção, $y\in A\cap B$; portanto, $Y\subseteq A\cap B$. Pela propriedade (2), esse mesmo $Y$ satisfaz $Y\subseteq X$. Juntando esta última inclusão à primeira parte da demonstração, temos

$$
A\cap B\supseteq X\supseteq Y.
$$

Para obter a inclusão $A\cap B\subseteq X$, vamos escolher um $Y$ que reúna todos os elementos comuns a $A$ e a $B$. A propriedade (2) vale para **todo** conjunto que satisfaça suas duas condições, permitindo aplicá-la a essa escolha particular.

Escolha

$$
Y=\{y:\ y\in A\ \land\ y\in B\}.
$$

Por essa definição e pela definição de interseção,

$$
\forall y:\quad\bigl(y\in Y\iff y\in A\cap B\bigr).
$$

Assim, $Y=A\cap B$: a condição seleciona exatamente os elementos da interseção.

Vamos verificar as condições para aplicar (2). Se $y\in Y$, então $y\in A$ e $y\in B$. Como isso vale para todo $y\in Y$, temos simultaneamente

$$
Y\subseteq A\qquad\text{e}\qquad Y\subseteq B.
$$

A propriedade (2) fornece, portanto,

$$
Y\subseteq X.
$$

Além disso, se $u\in A\cap B$, então $u\in A$ e $u\in B$. Pela definição do $Y$ escolhido, segue que $u\in Y$. Como $u$ é arbitrário na interseção, isso explicita a inclusão

$$
A\cap B\subseteq Y.
$$

Reunindo as duas últimas inclusões,

$$
A\cap B\subseteq Y\subseteq X.
$$

Pela **transitividade da inclusão**, concluímos que

$$
A\cap B\subseteq X.
$$

> [!note] Cada sentido da equivalência sobre Y usa uma propriedade
> Sob as hipóteses (1) e (2), para qualquer conjunto $Y$ temos
> $$
> Y\subseteq X\iff Y\subseteq A\cap B.
> $$
> Se $Y\subseteq X$, a propriedade **(1)** e a transitividade dão $Y\subseteq A$ e $Y\subseteq B$. Pelas definições de inclusão e de interseção, $Y\subseteq A\cap B$.
>
> Reciprocamente, se $Y\subseteq A\cap B$, todo elemento de $Y$ pertence a $A$ e a $B$. Temos, então, $Y\subseteq A$ e $Y\subseteq B$, e a propriedade **(2)** fornece $Y\subseteq X$.
>
> Cada sentido tem sua justificativa. Na demonstração da segunda inclusão, a escolha particular $Y=A\cap B$ permite aplicar (2) ao conjunto cujos elementos queremos colocar em $X$.

## Conclusão

Demonstramos

$$
X\subseteq A\cap B
\qquad\text{e}\qquad
A\cap B\subseteq X.
$$

A primeira inclusão mostra que todo elemento de $X$ pertence à interseção; a segunda mostra que todo elemento da interseção pertence a $X$. Pela **antissimetria da inclusão**,

$$
\boxed{X=A\cap B}.
$$

Portanto, as propriedades (1) e (2) caracterizam a interseção: $X$ está contido em $A$ e em $B$ e contém qualquer conjunto contido em ambos. $\blacksquare$

> [!note] O Y escolhido coincide com X
> Para o **$Y$ particular escolhido** na segunda inclusão, temos
> $$
> A\cap B=X=Y.
> $$
> A igualdade com $Y$ decorre de sua definição por todos os elementos comuns. Um conjunto arbitrário que esteja contido em $A$ e em $B$ precisa apenas estar contido em $X$, conforme (2).

# Apendice

## Uma reflexão sobre a verdade

Eu acho que é interessante aproveitar essa dupla de exercícios para fazer uma reflexão sobre a “verdade” aqui.

Note que, em ambas as questões, trabalhamos com os conjuntos $A$ e $B$, **para $A\neq B$**, e um conjunto $X$ que é formado mediante algumas propriedades. Temos um $Y$ também, mas o principal são esses.

Note que, pelas propriedades do exercício 1,

$$
(1)\quad X\supseteq A\qquad\text{e}\qquad X\supseteq B.
$$

Ou seja, dado o enunciado e como visto no resultado anterior,

$$
X=(A\setminus B)\cup(A\cap B)\cup(B\setminus A).
$$

Ou seja, só pela (1) dessa forma, já temos que a proposição do exercício 2,

$$
X=A\cap B,
$$

é **falsa**. Não precisa nem checar a propriedade (2) para chegar nessa conclusão. Por isso que o enunciado da questão 2 pede explicitamente para enunciar, ou seja, reescrever as propriedades sob outra caracterização. Por isso, usamos

$$
(1)\quad X\subseteq A\qquad\text{e}\qquad X\subseteq B.
$$

que, levando o restante da resolução com a propriedade (2), como visto na parte de **demonstração** desta questão, podemos ai sim considerar

$$
X=\{x:\ x\in A\ \land\ x\in B\}=A\cap B,
$$

como **verdadeira**.

Ou seja, é interessante pensar que a matemática nos demonstra que a verdade, de certa maneira, pelo menos sob certo contexto, é **relativa**.

$$
X\stackrel{?}{=}A\cap B
$$

Depende! A depender das propriedades de $X$, é verdadeira ou não.

Note até que, em sendo,

$$
\begin{aligned}
X_{A\cup B}&=A\cup B=(A\setminus B)\cup(A\cap B)\cup(B\setminus A),\\
X_{A\cap B}&=A\cap B,
\end{aligned}
$$

para $A \neq B$,

$$
X_{A\cap B}\subseteq X_{A\cup B},
$$
Mas eles não são iguais.
