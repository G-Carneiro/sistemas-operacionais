# Substituição de Páginas
- na fifo, o que acontece quando a página requisitada já está na fila?
  - FIFO: [0, 1, 2, 3], pag. requisitada 0.
  - FIFO: [0, 1, 2, 3], pag. requisitada 1.
- quando múltiplas páginas são referenciadas no período, isso ocorre em paralelo ou em sequência?
  - Aging: [2, 3, 4, 5]
  - Página a ser substituída: 2.

|  Periodo  |   Pags    |
|:---------:|:---------:|
|     0     |  1, 2, 3  |


# Projeto e implementação de paginação
- ao utilizar _copy on write_, somente a parte escrita recebe uma cópia e o restante continua compartilhado?
- Imagine que um processo A tenha alocado unicamente um array unidimensional de tamanho 89 MB em seu heap. Então, o processo A realiza uma chamada de sistema fork(), criando um novo processo B. Se o processo B realizar operações de escrita em 44% da memória alocada para o array, qual será o total de memória física alocada para os heaps dos processos (A + B) se o sistema utilizar a técnica de copy on write? Utilize duas casas decimais com arredondamento padrão.

# T2
- Se o ponteiro der uma volta completa em C1, então executa o algoritmo clássico do relógio em C2. No caso de uma substituição de página em C2, a nova página deverá ser encadeada na posição imediatamente anterior a pagina apontada pelo ponteiro C1.