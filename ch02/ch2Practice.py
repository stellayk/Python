fat = int(input("Enter grams of fat: "))
carb = int(input("Enter grams of carbohydrate: "))
protein = int(input("Enter grams of protein: "))
total = fat*9 + protein*4 + carb*4
print("Total calories: {:,} cal".format(total))



word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word3 = input("Enter third word: ")
print("First word: ", word1.capitalize())
print("Second word: ", word2.capitalize())
print("Third word: ", word3.capitalize())

abbr = word1[0]+word2[0]+word3[0]
print("Abbreviation: ",abbr.upper())
