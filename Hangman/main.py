#Step 2
import random
import hangman_words
import hangman_art
print(hangman_art.logo)
word_list = hangman_words.word_list
# word_list = ["aardvark", "baboon", "camel"]
random_of_list = random.randint(0,len(word_list)-1)
random_word = word_list[random_of_list]
print(random_word)
random_word_len = len(random_word)
#Testing code
print(f'Pssst, the solution is {random_word}.')
# OPS
life_count=6
y=0
the_word = []
for y in range(random_word_len):
  the_word = ['_'] * random_word_len
  y+=1
end = 0
while not end:
  x=0
  guessin = input("your letter?").lower()
  guess = str(guessin)
  life_count_tac = 100
  while x in range(random_word_len):
    if guess == random_word[x]:
      the_word[x]=guess
      life_count_tac -= 1
    x+=1
  print(the_word)
  if '_' not in the_word:
    end = 1
    print('You Win Lol !')
  if life_count_tac == 100:
    life_count-=1
    print(f"your intered is {guess} and it's wrong")
    print(hangman_art.stages[life_count])

  if life_count == 0:
    end = 1
    print('You Losssss Lol !')
  