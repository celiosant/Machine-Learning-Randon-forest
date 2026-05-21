"""




Essa árvore é o "mapa mental" que o seu computador criou para decidir se um clone está Apto ou Defeituoso.
 Ela funciona como um jogo de perguntas e respostas (Sim/Não).Aqui está o passo a passo de como o seu modelo está pensando:1.
   O Ponto de Partida (A Raiz)A pergunta mais importante de todo o seu banco de dados é a Massa.Pergunta: A massa do clone é menor ou igual
     a 83.405 kg?Lado Direito (False): Se a massa for maior que isso, o modelo nem faz mais perguntas. Ele já classifica o clone como Apto.
       Note que 704.148 clones caíram aqui e todos são perfeitos (entropia 0.0).2. O Segundo Filtro (Estatura Alta)Se o clone for leve
         ($\leq 83.405$ kg), ele cai para o segundo nível.Pergunta: A estatura é menor ou igual a 180.555 cm?Lado Direito (False): 
         Se ele for alto (mais de 180.555 cm), ele volta a ser classificado como Apto. Aqui temos mais 139.394 clones.3. A Zona Crítica
           (Onde aparecem os defeitos)Se o clone for leve ($\leq 83.405$ kg) e baixo ($\leq 180.555$ cm),
             o modelo faz a pergunta final:Pergunta: A estatura é menor ou igual a 180.245 cm?Lado Esquerdo (True):
               Se for muito baixo (abaixo de 180.245 cm), ele ainda é Apto (53.107 clones).Lado Direito (False): Se a e
               statura estiver entre 180.245 e 180.335 cm, aqui é onde a maioria dos Defeituosos aparece (nó azul lá embaixo).O que os 
               termos técnicos dizem:Entropy (Entropia): É o grau de "dúvida" do modelo.entropy = 0.0: O modelo tem 100% de certeza.
                 O grupo está "puro".entropy = 0.846: No último nó azul, o modelo ainda tem uma pequena mistura de aptos e defeituosos,
                   mas a maioria (110.526) é defeituosa, por isso ele escolhe essa classe.Samples: É o número total de clones que passaram 
                   por aquele nó.Value: Mostra a contagem de cada classe. Exemplo no primeiro nó: [938193, 110526].
                     Significa que havia 938 mil aptos e 110 mil defeituosos no início.Class: É a decisão final daquele ramo.
                     Resumo da "Regra de Negócio":Para este modelo, um clone só corre risco de ser Defeituoso se ele for leve (até 83.4kg) 
                     e tiver uma estatura muito específica (entre 180.24cm e 180.33cm). Se ele fugir dessas medidas por 1 grama ou 1 milímetro,
                       o modelo o considera Apto.Ficou claro como ele isolou os defeituosos no nó azul? 
                       Isso explica por que sua acurácia é tão alta: as regras são muito bem definidas!









"""