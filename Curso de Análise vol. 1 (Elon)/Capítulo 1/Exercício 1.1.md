## Concepção

Dados os conjuntos $A$ e $B$, seja $X$ um conjunto com as seguintes propriedades:

$$
\begin{aligned}
&(1)\quad A\subseteq X\ \land\ B\subseteq X,\\
&(2)\quad \forall Y:\ \bigl(A\subseteq Y\ \land\ B\subseteq Y\bigr)\implies X\subseteq Y.
\end{aligned}
$$

> [!note] O ⊂ do livro é a inclusão ampla
> O livro escreve as propriedades com $\subset$, que nele é sempre a **inclusão ampla**. A leitura não muda o rigor da resposta, muda o sentido do enunciado: com a **inclusão estrita**, as hipóteses seriam contraditórias. Por (1), o próprio $X$ contém $A$ e $B$; tomando $Y=X$ em (2), viria $X\subset X$, que a estrita nunca admite. Nenhum conjunto satisfaria o enunciado.

Provar que $X=A\cup B$ é provar que os dois conjuntos possuem exatamente os mesmos elementos. Pelo critério de **igualdade de conjuntos**, dado pelo **axioma da extensão**, queremos estabelecer
$$
\forall x:\quad x\in A\cup B\iff x\in X.
$$

Essa equivalência tem dois sentidos. Precisamos mostrar que todo elemento de $A\cup B$ pertence a $X$ e, depois, que todo elemento de $X$ pertence a $A\cup B$. Pela definição de inclusão, podemos escrever essas duas afirmações como:

$$
\begin{aligned}
A\cup B\subseteq X
&\iff\forall x:\ \bigl(x\in A\cup B\implies x\in X\bigr),\\[4pt]
X\subseteq A\cup B
&\iff\forall x:\ \bigl(x\in X\implies x\in A\cup B\bigr).
\end{aligned}
$$

A **antissimetria da inclusão** garante que, demonstradas as duas inclusões, podemos concluir a igualdade.

A ideia da dupla inclusão é começar com um elemento de um dos conjuntos e mostrar que esse mesmo elemento também pertence ao outro. Se quisermos escrever isso com duas letras, podemos usar

$$
\begin{aligned}
&\forall x\in A\cup B,\ \exists y\in X:\ x=y,\\
&\forall y\in X,\ \exists x\in A\cup B:\ y=x.
\end{aligned}
$$

Na primeira linha, dizer que existe $y\in X$ com $x=y$ é dizer que o próprio $x$ pertence a $X$. Na segunda, dizer que existe $x\in A\cup B$ com $y=x$ é dizer que o próprio $y$ pertence à união. Podemos, portanto, acompanhar uma única letra em cada parte da prova. O ponto é verificar a pertinência do mesmo elemento aos dois conjuntos.

## Demonstração

### Primeira inclusão: de A∪B para X

Analisando a propriedade (1), temos $A\subseteq X$ e $B\subseteq X$. Pela definição de inclusão, isso significa

$$
\begin{aligned}
&\forall a:\quad a\in A\implies a\in X,\\
&\forall b:\quad b\in B\implies b\in X.
\end{aligned}
$$

Ou seja, todo elemento de $A$ está em $X$, e todo elemento de $B$ também está em $X$. As duas informações valem ao mesmo tempo. Queremos reuni-las numa afirmação sobre os elementos de $A\cup B$.

Seja, então, $x\in A\cup B$ um elemento arbitrário. Pela definição de união,

$$
(3)\quad x\in A\cup B\iff x\in A\ \lor\ x\in B.
$$

Temos, portanto, duas possibilidades:

1. Se $x\in A$, então $x\in X$, pois $A\subseteq X$ pela propriedade (1).
2. Se $x\in B$, então $x\in X$, pois $B\subseteq X$ pela mesma propriedade.

Em qualquer dos casos, chegamos a $x\in X$. Como $x$ foi tomado arbitrariamente na união, o argumento vale para todo elemento dela. Assim,

$$
\forall x:\quad\bigl(x\in A\ \lor\ x\in B\bigr)\implies x\in X.
$$

Pelas definições de união, expressa em (3), e de inclusão, acabamos de demonstrar que

$$
A\cup B\subseteq X.
$$

> [!note] O "ou" inclui os elementos comuns
> Ao reunir os elementos de $A$ e de $B$, precisamos também contemplar os que pertencem aos dois conjuntos. Isso já acontece porque o "ou" da união é **inclusivo**: ele admite que as duas alternativas sejam verdadeiras ao mesmo tempo.
>
> Se $x\in A\cap B$, então $x\in A$ e $x\in B$. Pela primeira pertinência e por $A\subseteq X$, já temos $x\in X$; pela segunda e por $B\subseteq X$, chegamos à mesma conclusão. Portanto, nenhum elemento comum fica de fora do argumento, e temos também $A\cap B\subseteq X$.
>
> Essa afirmação é **condicional**: se um elemento pertence à interseção, ele pertence a $X$. Ela não afirma que a interseção tenha algum elemento. Por exemplo, $A=\{1\}$, $B=\{2\}$ e $X=\{1,2\}$ satisfazem as duas propriedades do enunciado: $X$ contém $A$ e $B$, e qualquer conjunto $Y$ que contenha ambos precisa conter $1$ e $2$, logo contém $X$. Mesmo assim, $A\cap B=\varnothing$. A prova da primeira inclusão funciona tanto quando há elementos comuns quanto quando não há.

### Segunda inclusão: de X para A∪B

Até aqui, sabemos que todo elemento da união pertence a $X$. Ainda precisamos verificar o sentido contrário: começando com um elemento de $X$, queremos chegar à união. O alvo agora é

$$
\forall x\in X,\quad x\in A\cup B,
$$

ou, pela definição de união,

$$
\forall x\in X,\quad x\in A\ \lor\ x\in B.
$$

Essa é a afirmação de que $X\subseteq A\cup B$.

> [!note] Conter A e B ainda permite elementos a mais
> A propriedade (1), sozinha, garante que todos os elementos de $A$ e de $B$ estão em $X$, mas ainda permite que $X$ tenha elementos que não estejam em nenhum dos dois. Por exemplo, com $A=\{1\}$ e $B=\{2\}$, o conjunto $Z=\{1,2,3\}$ contém $A$ e $B$, embora $3\notin A\cup B$. Logo, satisfazer (1) ainda não basta para concluir a **igualdade**. Precisamos usar a propriedade (2) para obter a **inclusão contrária**.

### Como a propriedade (2) permite obter a outra inclusão

A propriedade (2) afirma que, para todo conjunto $Y$, se $A\subseteq Y$ e $B\subseteq Y$, então $X\subseteq Y$. Em termos dos elementos, uma vez que todo elemento de $A$ e todo elemento de $B$ estejam em $Y$, essa hipótese garante que todo elemento de $X$ também está em $Y$.

Para organizar essa informação, consideremos primeiro um conjunto $Y$ qualquer que contenha $A$ e $B$. Se $u\in A\cup B$, então $u\in A$ ou $u\in B$, pela definição de união. Como $A\subseteq Y$ e $B\subseteq Y$, em qualquer dos casos temos $u\in Y$. Portanto,

$$
\bigl(A\subseteq Y\ \land\ B\subseteq Y\bigr)
\implies\forall u\in A\cup B,\quad u\in Y.
$$

Isso mostra que $A\cup B\subseteq Y$. Já a propriedade (2) nos fornece a informação sobre $X$: para esse mesmo $Y$, ela garante $X\subseteq Y$. Juntando com a primeira inclusão que demonstramos, temos

$$
A\cup B\subseteq X\subseteq Y
\qquad\text{sempre que }A\subseteq Y\text{ e }B\subseteq Y.
$$

O que queremos obter é $X\subseteq A\cup B$. Assim, nessa aplicação de (2), interessa escolher $Y=A\cup B$. Antes de usar a conclusão da hipótese, precisamos verificar que essa escolha atende às suas duas condições.

> [!note] Escolher Y a partir do que queremos concluir
> A ideia agora é mostrar que **cada elemento de $X$** está em $A\cup B$. A propriedade (2) já nos diz que cada elemento de $X$ está em qualquer $Y$ que contenha $A$ e $B$. Por isso, a escolha que produz a conclusão desejada é $Y=A\cup B$.
>
> Podemos fazer essa escolha porque a hipótese vale **para todo $Y$**. Também não estamos supondo a igualdade que queremos provar: a união é definida a partir de $A$ e de $B$, e podemos verificar que contém ambos antes de saber se coincide com $X$.

Façamos essa verificação por elementos. Se $a\in A$, então $a\in A\cup B$, pela definição de união. Como isso vale para todo $a\in A$, segue que $A\subseteq A\cup B$. Do mesmo modo, se $b\in B$, então $b\in A\cup B$; logo, $B\subseteq A\cup B$. Temos, assim,

$$
A\subseteq A\cup B
\qquad\text{e}\qquad
B\subseteq A\cup B.
$$

Portanto, $Y=A\cup B$ satisfaz as duas condições de (2). Aplicando essa hipótese a esse conjunto, obtemos

$$
\underbrace{\bigl(A\subseteq A\cup B\ \land\ B\subseteq A\cup B\bigr)}_{\text{condições verificadas}}
\implies X\subseteq A\cup B.
$$

Para acompanhar a conclusão em termos dos elementos, seja agora $x\in X$ arbitrário. A propriedade (2), aplicada ao $Y$ escolhido, garante que $x\in Y$. Como $Y=A\cup B$, segue que $x\in A\cup B$ e, pela definição de união, que $x\in A$ ou $x\in B$. Assim,

$$
\forall x\in X,\quad x\in A\cup B.
$$

Pela definição de inclusão, isso demonstra a segunda parte que faltava:

$$
X\subseteq A\cup B.
$$

> [!note] A inclusão permite que os conjuntos coincidam
> Dizer $X\subseteq Y$ é dizer que **todo elemento de $X$ pertence a $Y$**. Isso admite $X=Y$. Não há exigência de encontrar um elemento de $Y$ fora de $X$, nem um elemento diferente daquele que estamos acompanhando. Com a escolha $Y=A\cup B$, o que precisamos é justamente mostrar que o mesmo $x\in X$ pertence à união.

## Conclusão
Deste modo,

$$
\begin{aligned}
&\forall x:\quad x\in A\cup B\implies x\in X,\\
&\forall x:\quad x\in X\implies x\in A\cup B.
\end{aligned}
$$

A primeira afirmação veio de (1); a segunda, de (2), com $Y=A\cup B$. Todo elemento da união está em $X$, e todo elemento de $X$ está na união. Portanto, os conjuntos têm exatamente os mesmos elementos. Pela **antissimetria da inclusão**,

$$
\boxed{X=A\cup B}.
$$

$\blacksquare$

> [!note] O menor conjunto que contém A e B
> As duas propriedades passam a ter papéis claros: (1) exige que $X$ **contenha** $A$ e $B$; (2) exige que $X$ esteja **contido em todo conjunto** que contenha ambos. Nesse sentido da inclusão, $X$ é o **menor conjunto que contém $A$ e $B$**. A demonstração explica isso elemento a elemento: (1) coloca em $X$ todos os elementos da união, e (2), aplicada à própria união, garante que os elementos de $X$ também pertençam a ela.
