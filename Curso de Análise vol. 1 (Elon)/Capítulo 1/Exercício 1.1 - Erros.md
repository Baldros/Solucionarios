Erros e incompletudes da tentativa manuscrita de resolver o Exercício 1.1, separados em erros de raciocínio, erros de escrita e incompletudes, isto é, o que ficou faltando ou vago e a solução compilada precisou complementar. A solução está no arquivo do exercício; aqui fica o registro da qualidade da tentativa. As notas do acervo são citadas pelo nome, em texto simples.

## Avaliação

A tentativa não demonstra o resultado. Ela prova uma das inclusões, $A\cup B\subseteq X$, a partir de (1), mas declara $X=A\cup B$ sem provar a outra, $X\subseteq A\cup B$. O passo que falta é aplicar (2) com $Y=A\cup B$, e a tentativa já tinha os dois ingredientes: identificou o alvo, $\forall x\in X,\ x\in A\cup B$, e escreveu que $A\subseteq Y$ e $B\subseteq Y$ dão $\forall x\in A\cup B,\ x\in Y$. Três erros de raciocínio impediram de ligar os dois: a leitura de $\subset$ como inclusão estrita, a propriedade (2) tratada como algo a provar em vez de hipótese a usar, e a busca de um elemento em $A\cap B$, que levou a um desvio longo por complementares, com erros próprios e sem relação com a tese.

Ficam como acertos a estratégia da dupla inclusão; a dúvida sobre a existência de um elemento em $A\cap B$, que procedia; a percepção de que uma conta contradizia a lei de De Morgan, que denunciou os erros do desvio; e a autoavaliação de que a solução estava fraca, que era exata.

## Erros de raciocínio

### A propriedade (2) tratada como algo a provar

A tentativa procurou estabelecer fatos sobre um $Y$ qualquer, como a existência de um $y\in Y$ diferente de $x$, como se fosse preciso demonstrar (2). Mas (2) é hipótese, válida para todo $Y$, e uma hipótese universal se usa escolhendo um $Y$ que cumpra a condição e colhendo a conclusão. Por isso a escolha $Y=A\cup B$, que dá a inclusão que faltou, não chegou a ser considerada.

### O ⊂ do livro lido como inclusão estrita

A tentativa leu $X\subset Y$, na propriedade (2), como $X\subseteq Y\land X\neq Y$, e tratou a diferença entre as leituras como questão de rigor, dizendo que o livro não distingue as duas inclusões e que $\subset$ seria a ampla "na maioria dos casos". O livro distingue as duas: chama de parte própria a inclusão entre conjuntos diferentes, só não lhe dá símbolo. E nele $\subset$ é sempre a inclusão ampla (nota Notações de Teoria dos Conjuntos). A diferença entre as leituras é de sentido: com a estrita, as hipóteses se contradizem. Por (1), o próprio $X$ contém $A$ e $B$; com $Y=X$, (2) exigiria $X\subset X$, que a estrita nunca admite (nota Subconjunto).

### Existência de um elemento em A∩B

A tentativa afirmou que existe $x\in A\cap B$ com $x\in X$ e chegou a concluir $A\cap B\neq\varnothing$. Nada no enunciado garante isso: $A=\{1\}$, $B=\{2\}$ e $X=\{1,2\}$ satisfazem (1) e (2) com $A\cap B=\varnothing$. A preocupação que motivou a afirmação, a de não "perder" os elementos de $A\cap B$, também não procede: o "ou" da união é inclusivo, e um elemento de $A\cap B$ já está coberto (nota Operações de Conjuntos).

### Quantificador existencial no lugar do universal

A tentativa traduziu $A\subseteq X$ e $B\subseteq X$ por "existe $a\in A$ ou $b\in B$ com $a\in X$ ou $b\in X$". A inclusão é uma afirmação universal, $A\subseteq X\iff\forall x\,(x\in A\implies x\in X)$ (nota Subconjunto), e as duas inclusões se juntam por "e", não por "ou". A tradução certa das duas juntas é $\forall x\,\bigl((x\in A\lor x\in B)\implies x\in X\bigr)$, isto é, $A\cup B\subseteq X$. O mesmo erro reaparece ao passar de $X=A\cup B$ para "existe $x\in X$ com $x\in A$ ou $x\in B$".

### A tese usada como ponto de partida

Um dos rascunhos parte de $X=A\cup B$ para extrair propriedades de $X$. Isso supõe o que se quer provar. O ponto de partida são as hipóteses (1) e (2); a igualdade é o ponto de chegada.

### Hipótese apresentada como resultado

Depois do desvio por complementares, a tentativa concluiu que "isso demonstra que $A,B\subseteq X$". Mas $A\subseteq X$ e $B\subseteq X$ são a própria hipótese (1), não algo a demonstrar.

### A propriedade (2) como consequência de (1)

A tentativa afirmou que (2) surge como consequência de (1). As duas são independentes: $A\cup B\cup\{z\}$, com $z\notin A\cup B$, satisfaz (1) e falha (2) para $Y=A\cup B$. Cada propriedade fornece uma das inclusões, e nenhuma basta sozinha.

### "Não implica" lido como "implica a negação"

De "$A\subseteq Y$ e $B\subseteq Y$ não implicam $\forall y\in Y,\ y\in X$", a tentativa passou a "existe $y\in Y$ tal que $y\neq x$". Há dois erros. Uma afirmação não implicar $P$ não significa que ela implique a negação de $P$; significa só que $P$ pode falhar. E a negação de $\forall y\in Y,\ y\in X$ é $\exists y\in Y,\ y\notin X$: a não pertinência a um conjunto, e não a desigualdade entre dois elementos.

### Complementar da interseção confundido com a diferença simétrica

A tentativa escreveu $(A\cap B)^c=(A\cup B)-(A\cap B)=A\,\Delta\,B$. A segunda igualdade está certa, mas a primeira não: o complementar da interseção contém também os elementos fora de $A\cup B$, e $(A\cap B)^c=(A\,\Delta\,B)\cup(A\cup B)^c$ (nota Operações de Conjuntos). Com $E=\{1,2,3\}$, $A=\{1\}$ e $B=\{2\}$, tem-se $(A\cap B)^c=E$, enquanto $A\,\Delta\,B=\{1,2\}$. Os dois só coincidem quando $A\cup B=E$.

### Manipulação sem regra que a sustente

A tentativa escreveu $(A\cap B^c)\cup(B\cap A^c)=A\cap\Omega\cap A^c$ e, mais adiante, $A\cap X\cap A^c=B^c\cap A^c$. Nenhuma propriedade da união e da interseção (nota Operações de Conjuntos) produz a primeira passagem: as leis distributivas não permitem pôr em evidência termos de interseções diferentes. Além disso, $A\cap\Omega\cap A^c$ e $A\cap X\cap A^c$ são vazios, porque $A\cap A^c=\varnothing$. Essas passagens levaram a $(A\cap B)^c=A^c\cap B^c$, em contradição com a lei de De Morgan, $(A\cap B)^c=A^c\cup B^c$ (notas Complementar e Lei de De Morgan), e a tentativa percebeu a contradição.

### Conjunto fundamental identificado com X

A tentativa cogitou $\Omega=X$ porque os dois contêm $A$ e $B$. Conter $A$ e $B$ não determina um conjunto: $\Omega$ é o maior deles, e $X$, por (2), o menor. Supor $\Omega=X$ seria supor $\Omega=A\cup B$, que embute a tese.

## Erros de escrita

### Proposição escrita como conjunto

A inclusão foi escrita como $A\cup B\subseteq X\equiv\{x,y;\ \forall x\in A\cup B,\ \exists y\in X;\ x=y\}$. A inclusão é uma proposição, verdadeira ou falsa; as chaves constroem um conjunto, e $\equiv$ entre os dois não tem sentido. A forma certa é $A\cup B\subseteq X\iff\forall x\,(x\in A\cup B\implies x\in X)$. A parte $\exists y\in X;\ x=y$ diz apenas $x\in X$.

### ⊆ no lugar de ⊇

Ao escrever as duas inclusões da igualdade, a segunda repetiu $A\cup B\subseteq X$ quando devia ser $A\cup B\supseteq X$, isto é, $X\subseteq A\cup B$.

### Pertinência no lugar de inclusão

A propriedade (2) foi escrita, numa versão, como $A,B\subset Y\iff X\in Y$. $X$ e $Y$ são conjuntos, e a relação entre eles é a inclusão, $X\subseteq Y$, não a pertinência (nota Subconjunto). A mesma expressão usava $\iff$ onde (2) só dá $\implies$. As duas coisas foram corrigidas numa versão posterior.

### Quantificador limitado ligado a uma equivalência

A igualdade foi escrita como $\forall x\in A\cup B\iff x\in X$. Um quantificador limitado a $A\cup B$ não pode reger uma equivalência cujo lado esquerdo é a própria pertinência a $A\cup B$. A forma certa quantifica sobre todo $x$: $X=A\cup B\iff\forall x\,(x\in A\cup B\iff x\in X)$ (nota Axioma da Extensão).

### Duas variáveis sob um quantificador

Para dizer que $A\cup B\subseteq X$, a tentativa escreveu $\forall a\in A\lor b\in B\land a,b\in X$. Um quantificador rege uma variável, e a expressão mistura $a$ e $b$ sob conectivos sem parênteses. Basta uma variável: $\forall x\,\bigl((x\in A\lor x\in B)\implies x\in X\bigr)$.

### Variável sem introdução

Em "existe $y\in Y$ tal que $y\neq x$", a variável $x$ não foi introduzida por nenhum quantificador nem fixada antes, e não se sabe de que $x$ a expressão fala. Toda variável de uma fórmula precisa estar quantificada ou ter sido tomada explicitamente, como em "seja $x\in X$".

### Parênteses omitidos

Expressões como $A\cup B\cap(A\cap B)^c$ e $A\cap B^c\cup B\cap A^c$ ficaram sem parênteses. União e interseção não têm precedência convencional entre si, e as leituras possíveis dão conjuntos diferentes em geral: com $A=\{1\}$ e $B=C=\varnothing$, $(A\cup B)\cap C=\varnothing$, mas $A\cup(B\cap C)=\{1\}$. A escrita certa é $(A\cup B)\cap(A\cap B)^c$ e $(A\cap B^c)\cup(B\cap A^c)$.

## Incompletudes

### A segunda inclusão ficou sem demonstração

É a incompletude decisiva, a que impede a tentativa de demonstrar o resultado. A conclusão $X=A\cup B$ foi declarada com base em $A\cup B\subseteq X$ e numa leitura da propriedade (2), sem que $X\subseteq A\cup B$ fosse provado, e a igualdade exige as duas inclusões. A solução compilada a completa aplicando (2) com $Y=A\cup B$, que contém $A$ e $B$ pela definição de união.

### O "para todo Y" da propriedade (2) ficou implícito

A tentativa escreveu (2) como o livro, "se $Y\supset A$ e $Y\supset B$, então $Y\supset X$", sem explicitar que $Y$ é qualquer. No enunciado, o quantificador fica implícito, como nas implicações entre propriedades que a nota Notações de Teoria dos Conjuntos registra. É esse quantificador que permite escolher $Y$: deixado de lado, (2) passou a parecer uma afirmação sobre um $Y$ fixo e desconhecido. A solução compilada escreve $\forall Y:\ (A\subseteq Y\land B\subseteq Y)\implies X\subseteq Y$.

### A primeira inclusão afirmada sem argumento

De $A\subseteq X$ e $B\subseteq X$, a tentativa passou direto a $X\supseteq A\cup B$, e a versão geral, "$A\subseteq Y$ e $B\subseteq Y$ dão $\forall x\in A\cup B,\ x\in Y$", também ficou sem justificativa. O passo é verdadeiro, mas é metade da demonstração e pede o argumento: tomado $x\in A\cup B$, tem-se $x\in A$ ou $x\in B$, e em cada caso $x\in X$. A solução compilada faz essa prova por casos.

### A dupla inclusão sem justificativa

A tentativa enunciou que provar $X=A\cup B$ é provar as duas inclusões, sem dizer por quê. A justificativa é a antissimetria da inclusão (nota Subconjunto), que dá o critério de igualdade da nota Axioma da Extensão; a solução compilada a cita.

### As hipóteses não foram interpretadas

A tentativa reescreveu (1) e (2) em símbolos, mas não disse o que elas afirmam juntas: que $X$ é o menor conjunto que contém $A$ e $B$. É essa leitura que sugere a estratégia, porque cada propriedade dá uma das inclusões, e a solução compilada a apresenta antes da demonstração.
