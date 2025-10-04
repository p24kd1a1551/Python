#python program to check whether the given letter is vowel or not
word = input("Enter a letter : ")
if word.lower() in "aeiou" :
    print(f"yes,{word} is vowel!")
else :
    print(f"No,{word} not vowel!") 