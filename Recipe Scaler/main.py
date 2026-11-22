def scale_recipe(ingredients, scale):
    finalArray = []

    for ingredient in ingredients:
       
        ingredientArray = ingredient.split(" ")

        ingredientArray[0] = str(float(ingredientArray[0]) * scale).replace(".0", "")

        print(ingredientArray[0])

        finalArray.append(" ".join(ingredientArray))
        

    return finalArray

print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2))  

print(scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5))

print(scale_recipe(["3 C Milk", "2 C Oats"], 0.5))

print(scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5))
