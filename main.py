#print("Hello teacher")
#print("Homework №4 Banul")

#1. Користувач вводить рядок з клавіатури.Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.

#string = input("Enter a string: ")

#letter_count = 0
#digit_count = 0

#for char in string:
 #  if char.isalpha():
 #      letter_count += 1

  # elif char.isdigit():
     #  digit_count += 1

#print("Number of letters:", letter_count)
#print("Number of digits:", digit_count)

#########################################

#2.Користувач вводить з клавіатури рядок і символ для пошуку.Скільки разів у рядку зустрічається потрібний символ?

#string = input("Enter a string: ")
#char = input("Enter symbol for search: ")

#count = 0

#for c in string:
    #if c == char:
    # count += 1

#print(f"The symbol '{char}' appears {count} times in the string.")

######################################

#3.Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше.

string = input("Enter a string: ")
search_word = input("Enter the word to search for: ")
replace_word = input("Enter the word to replace it with: ")

words = string.split()

modified_words = []

for word in words:
   if word == search_word:
       modified_words.append(replace_word)
   else:
       modified_words.append(word)

modified_string = " ".join(modified_words)

print(modified_string)
