# TC-war-project

This is a project for war game

## To-do:
- Print word battle
- Print the last items of each player's card stack lists at once
- Pop the cards of the players' lists and put it into a table list
- While both players have at least one card:
- If:
- Pn has a higher value card, remove both cards from table list and add it to the beginning of P1's card stack list
- P1 and P2 have even cards:
  - print war
    - while both of the players have more than one card:
      - print one closed card (<code>stack[-1]</code>) as [??] and one open card (<code>stack[-2]</code>) as open card for both players
      - Pop the cards of the players' lists and put it into a table list
      - Do until one of the player's has a higher value card or:
        - Remove all cards from the table list and add it to the beginning of the winner's card stack list


