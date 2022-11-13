# Projeto Introdução à Computação 2022/2023

## Autoria: Nuno Martins Nº22109510 e Pedro Coutinho Nº21905323

### O que cada um fez no projeto:

#### Nuno
    - Criação do repositório no github
    - Class dice
    - Intanciação de vários orcs baseado baseado num valor "numOfOrcs"
    - Método "calcTurnOrder" na class Characters 
    - Método "casSpell" na class PlayerCharacters
    - Método "testSpell" na class PlayerCharacters
    - Verificar se jogador quer começar nova ronda
    - Adicionar escolha de alvo para ataque do jogador

#### Pedro
    - Criação das classes "Characters" e "PlayerCharacters"
    - Método "__lt__" para comparação de Characters
    - Método "attack" para o ataque dos Characters
    - Basic game loop logic
    - Escolha de spell e alvos para o mesmo
    - Alvo para ataque dos orcs
    - Nomes random para os orcs
    - Settings de dificuldade e numero de rondas
    - Prints coloridos
    - Correção de bugs

### Arquitetura da solução

Temos a class "Program" que é onde se faz o main loop do jogo, onde se trata dos inputs do jogador e por sua fez chama os métodos corretos. A class "Characters" trata da criação das personagens, que tem, um construtor que inicializa todos os parâmetros respetivos à personagem, o método "lt" para personagens poderem ser reorganizadas numa lista com list.sort(), método "calcTurnOrder" que serve para randomizar a ordem no turno, método "attack" que recebe uma outra personagem que é o target, e por ultimo o método "inpectChar" que simplesmente imprime a informação da personagem. A class "PlayerCharacters" é derivada da class "Characters" que por sua vez faz com que implemente todos os parâmetros e métodos que "Character" impletementa, implemtenta tambem mais um parâmetro este sendo "spells" e mais dois métodos, "castSpells" que recebe uma string "spell" e um Character "target", neste método o é selecionado o spell correto, aplicado o seu efeito e o seu custo. No método "testSpell" é verificado se o PlayerCharacter tem mana suficiente para dar cast ao spell. A class "Dice" serve unicamente para instanciar random e gerar um random de 1 a "maxValue" incluindo ambos os limites.

### [Repositório Git](https://github.com/NunoAfonsoM/Projeto-IC-2022-2023.git)

### Referências

Não foram usadas referências.