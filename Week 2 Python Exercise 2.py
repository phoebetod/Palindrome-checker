#Palindrome exercise
#Step 1 - Ask user for a word

word = input("Type in a word and I will tell you whether it is a palindrome or not")

#Step 2 - Think of the word as an index. Count how many letters are in the index.

i = 0
for letter in word:
    i = i + 1
#    print(i)

#Step 3 - Half this number (keeping it as a whole number - so turn it into an interger not a float)
halfLength = int(i / 2)
#print(halfLength)

#Compare the first and last characters in the index, compare the second and second to last characters, and continue up to the number of half the characters in the word. If these are all equal then the word is a palindrome. Return statement to the user saying whether the word is a palindrome or not.


for letter in word:
    otherside = word[i-1]
    i = i - 1

    if letter != otherside:
        print("That is not a palindrome!")
        break

    if i == halfLength:
        print("Welldone that is a palindrome!")
        break


    
