# Diagnóstico e revisão

Leia a tentativa pelo conteúdo matemático e pela intenção sustentada pelo contexto. A classificação ajuda a indicar a correção adequada; não mede a capacidade do estudante nem define seções obrigatórias do documento final.

## Antes de julgar a passagem

Confira enunciado, hipóteses, tese, convenções e versões. O símbolo amplo do Elon é adaptado para $\subseteq$; não atribua uma inclusão estrita apenas pela forma do traço. Localize no material teórico a definição ou resultado que decide o ponto.

Distinga o que está efetivamente escrito, o que o contexto permite interpretar e o que ainda depende de esclarecimento. Se a dúvida de leitura mudar a avaliação, exponha as leituras possíveis e esclareça antes de classificar. Uma inserção de revisão pode corrigir um trecho específico sem substituir todos os rascunhos anteriores.

## Três tipos de problema

| Tipo | Critério | Impacto e tratamento |
|---|---|---|
| Escrita ou atenção | A fórmula escrita diverge do raciocínio demonstrado no contexto. | Localize o lapso e indique o ajuste pontual. Diga se o argumento, interpretado corretamente, continua válido. |
| Conceitual | O próprio raciocínio depende de definição, hipótese, objeto ou inferência incorreta. | Explique qual conclusão falha, ensine seu fundamento e indique o retrabalho necessário. |
| Omissão ou gap | Uma conclusão pode ser verdadeira, mas falta um passo, hipótese, justificativa ou explicitação exigida pela teoria. | Mostre exatamente a dependência ausente e o que precisa ser desenvolvido para fechar o argumento. |

O símbolo isolado não decide o tipo. Escrever $\lor$ onde deveria haver $\land$ pode ser um lapso quando o raciocínio seleciona corretamente os elementos comuns; se a inferência usa a disjunção, há um erro conceitual. Quantificadores errados também exigem esse exame do contexto.

Os tipos podem coexistir. Corrigir uma fórmula pode revelar que a demonstração continua incompleta. Não apresente uma troca simbólica como suficiente para fechar um gap independente; também não invente um gap quando a definição ou um passo já presente o resolveu.

## Feedback preciso e proporcional

Cada apontamento deve permitir recuperar, sem impor um formulário rígido:

- o local e a afirmação examinada, transcrita ou descrita fielmente;
- o tipo de problema, a evidência e eventual incerteza;
- o fundamento nas notas e o impacto exato no argumento;
- a parte válida que permanece e a alteração necessária;
- o próximo trabalho: correção pontual ou desenvolvimento a refazer.

Comece pelo bloqueio de que os próximos passos dependem. Explique com detalhe proporcional à dificuldade, usando pistas progressivas, exemplos e contraexemplos. Um contraexemplo ao enunciado inteiro precisa satisfazer suas hipóteses; um exemplo que refuta apenas uma passagem isolada deve ser apresentado com esse limite.

Para retrabalho ou aprofundamento, indique a abertura vermelha e o trecho a desenvolver, preservando o restante válido. Se a concepção inteira for inviável, explique por que a correção local não basta e proponha seu descarte ou reformulação, com os elementos aproveitáveis. A nova elaboração cabe ao usuário.

## Exemplo: lapso e gap na dupla inclusão

As expressões

$$
X\subseteq A\cap B
\qquad\text{e}\qquad
A\cap B\supseteq X
$$

dizem a mesma coisa. A nota Subconjunto permite conferir isso pelos elementos: ambas começam com um elemento de $X$ e concluem sua pertinência à interseção.

Se o contexto ou o esclarecimento da intenção mostra que a segunda expressão deveria ser $A\cap B\subseteq X$, há um **lapso de escrita** a corrigir. Isso não prova que a inclusão pretendida foi demonstrada. Se ainda não há argumento para ela, existe também uma **omissão**. Pela antissimetria, desenvolvida nas notas Subconjunto e Axioma da Extensão, a igualdade depende das duas inclusões.

O feedback deve separar os efeitos: a troca de símbolo corrige o registro da intenção; a justificativa da inclusão contrária completa a demonstração. Se essa justificativa já estiver em outra parte válida da tentativa, basta relacioná-la ao alvo e corrigir a escrita. Se o raciocínio realmente tratar uma inclusão repetida como suficiente para a igualdade, há um **erro conceitual**, que não pode ser reduzido à grafia.

Já o par $X\subseteq A\cap B$ e $A\cap B\subseteq X$ expressa corretamente os dois sentidos e não é redundante.

## Reavaliar sem reabrir o que foi resolvido

Aguarde a reformulação e releia o argumento ou os arquivos efetivamente alterados. Confira as condições da passagem, a correção anterior e eventuais novos problemas. Diga o que passou a estar justificado, identificando seu fundamento concreto.

Por exemplo, dizer que $Y$ possui somente elementos de $A\cap B$ garante $Y\subseteq A\cap B$. Definir $Y=\{y:y\in A\land y\in B\}$ seleciona exatamente a interseção e já garante também $A\cap B\subseteq Y$. Não mantenha esse segundo ponto aberto apenas porque uma frase explicativa mais fraca permaneceu ao lado da definição correta. Fundamentação: notas Operações de Conjuntos e Subconjunto.

Um OK à explicação ou um aviso de correção não substitui a revisão da nova tentativa. Tampouco se deve exigir uma redação particular se outra formulação válida fornece a justificativa necessária. O fechamento é matemático e fundamentado, não a reprodução de uma dica.

## Evidências e documento final

Na memória de trabalho, conserve a localização, o diagnóstico, as notas consultadas, as orientações e revisões observadas, o argumento de fechamento e as aprovações. Não invente uma reformulação ou uma compreensão autônoma não demonstrada. Esse controle de procedência serve à continuidade e à escolha fiel do conteúdo.

No Processo de resolução, transforme esse material em exposição técnica: qual era o problema, que fundamento o decide, como a correção se desenvolve e por que o resultado é adequado. Exemplos e pistas que esclarecem a matemática podem permanecer; ações dos participantes, ferramentas, pedidos e cronologia do chat ficam fora. Veja o contrato em [Arquivos e memória de trabalho](arquivos.md).
