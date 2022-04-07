#Step 1, AULA 071
import random
import palavras
import figuras
from replit import clear

print(figuras.logo)
print("\n")

chosen_word = random.choice(palavras.word_list)
live = 6
#print(f"Pss.. a palavra é {chosen_word}")
display = []
length = (len(chosen_word))

for letter in chosen_word:
  display += "_"
  

end_game = True

while end_game: 
  guess = input("Escolha uma letra: ").lower()
  clear()

  if guess in display:
    print(f"A letra {guess} já foi digitada, tente outra ;)\n")
    
  for position in range(length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  

  print(f"{' '.join(display)}\n")
  

  if guess not in chosen_word:
    print(f"A letra '{guess}' não faz parte da palavra, você perdeu uma vida!\n")
    live -= 1
    
    
    if live == 0:
      end_game = False
      print("FIM DO JOGO!\n")
    

  if not "_" in display:
    
      end_game = False
      print("Você ganhou...")
  
  print(figuras.stages[live])
 

