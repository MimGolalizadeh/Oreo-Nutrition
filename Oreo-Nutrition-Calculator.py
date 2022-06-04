description = """\nHello world)
This application helps you to calculate how much calories, sodium, carbohydrate, fat you have consumed.
with eating each Oreo cookie by asking you some questions. Please answer the questions carefully to have 
correct answers.
At the End it gives you final information and some advices \n"""
print(description)

# Getting information from user
name = input("What is your name? ").title()
number_of_cookie = int(input("How many cookies have you got " + name +"? "))

# Defining variables
calories = int((number_of_cookie) * 160)
calories_limit = 2000
sodium = int((number_of_cookie) * 190)
carbohydrate = int((number_of_cookie) * 25)
fat = int((number_of_cookie) * 7)

# Show the result
consumption_calculator = f"{'-' * 50} \n{name} ,you have got {number_of_cookie} cookie(s) \n" \
                         f"Your consumption details:  \nCalories:        {calories} \n" \
                         f"Sodium:          {sodium}mg \nCarbohydrate:    {carbohydrate}gr \nFat:             {fat}gr"
print(consumption_calculator)
print("-" * 50)

# Show the Warning or message - two different conditions for less/more than 2000kcal consumption
if calories < calories_limit:
    message = f"Well done {name}, you have got less than {calories_limit}kcal,*** eating more" \
              f" than {calories_limit}kcal per day might be unhealthy."
else:
    message = f"*** Please notice that eating more than {calories_limit}kcal per day might be unhealthy. " \
              f"Your health condition is matter."

print(message)
