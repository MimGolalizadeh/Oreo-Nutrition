discription = """\n\033[1;37mHello world)
This application helps you to calculate how much calories, sodium, carbohydrate, fat you have consumed.
with eating each Oreo Coockie by asking you some questions. Please answer the questions carefully to have correct answers.
At the End it gives you final information and some advices \n"""
print(discription)

# Getting information from user
name = input("\033[1;38mWhat is your name? ").title()
number_of_coockie = int(input("\033[1;38mHow many cookies have you got " + name +"? "))

# Defining variables
calories = int((number_of_coockie) * 160)
calories_limit = 2000
sodium = int((number_of_coockie) * 190)
carbohydrate = int((number_of_coockie) * 25)
fat = int((number_of_coockie) * 7)

# Show the result
consumption_calculator = f"\033[1;35m{'-' * 50} \n\033[1;33m{name} ,you have got {number_of_coockie} coockie(s) \nYour consumption details: \033[1;32m \nCalories:        {calories} \nSodium:          {sodium}mg \nCarbohydrate:    {carbohydrate}gr \nFat:             {fat}gr"
print(consumption_calculator)
print("\033[1;35m-" * 50)

# Show the Warning or message - two different conditions for less/more than 2000kcal consumption
if calories < calories_limit:
    message = f"\033[1;34mWell done {name}, you have got less than {calories_limit}kcal,\033[1;31m*** eating more than {calories_limit}kcal per day might be unhealthy."
else:
    message = f"\033[1;31m*** Please notice that eating more than {calories_limit}kcal per day might be unhealthy. Your health condition is matter."

print(message)
