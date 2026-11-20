Conteúdos já compilados no Notas-de-Estudo que se relacionam com as soluções deste livro: outra forma de resolver, outra forma de ver ou um resultado do acervo que usa a mesma ideia. As notas do acervo são citadas pelo nome, em texto simples.

## Capítulo 1

### O mesmo passo no complementar da união

A parte $A\cup B\subseteq X$ do Exercício 1.1 tira, de $A\subseteq X$ e $B\subseteq X$, que $A\cup B\subseteq X$. A nota Complementar usa esse mesmo passo, sem enunciá-lo, ao demonstrar pelo caminho do livro que $\complement(A\cup B)=\complement A\cap\complement B$: de $A\subseteq\complement X$ e $B\subseteq\complement X$, conclui $A\cup B\subseteq\complement X$. O conjunto que a nota chama de $X$ é $\complement A\cap\complement B$, e não o do exercício.

### Dualidade com o Exercício 1.2 pelo complementar

O Exercício 1.1 pode ser lido através do complementar. Tome um conjunto fundamental $E$ que contenha $A$ e $B$; a propriedade (2) com $Y=E$ dá também $X\subseteq E$. A inversão da inclusão e o complementar do complementar, da nota Complementar, transformam (1) em $\complement X\subseteq\complement A$ e $\complement X\subseteq\complement B$, e (2) em: todo $Z\subseteq E$ com $Z\subseteq\complement A$ e $Z\subseteq\complement B$ satisfaz $Z\subseteq\complement X$. Isto é, $\complement X$ é o maior subconjunto de $E$ contido em $\complement A$ e em $\complement B$, a caracterização da interseção que o Exercício 1.2 pede. Com o resultado do 1.2, $\complement X=\complement A\cap\complement B$, e a lei de De Morgan com o complementar do complementar dá $X=\complement(\complement A\cap\complement B)=A\cup B$. Os dois exercícios são o mesmo, lidos através do complementar: resolvido um, o outro sai por dualidade. É a forma correta de usar complementares neste exercício.
