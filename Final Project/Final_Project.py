print("Quiz")

question = "Who invented the telephone?"
options = "a.Myslef\nb. My grandpa \nc.Donald Trump \nd. Alexander Graham Bell\n"

print(question)
print(options)

while True:
    response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

    if response == "d":
        print("Congrats you earned 10 points.")
    else:
        print("Incorrect! Try again.")
       
      

