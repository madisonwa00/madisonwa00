name= input('What is your name?: ')
print()
print("Welcome " +name+ "! Are you an extrovert or introvert?? \n"
                        "Answer the following questions to find out!")
persquestions =[
    "Question 1:\n"
    "(A) Would you say you're focused on details and facts?\n"
    "(B) Would you describe yourself as unplanned and spontaneous?",
    "(A) Are you interested in the external world?\n"
    "(B) Are you interested in the internal world?",
    "(A) Would you describe yourself as enthusiastic?\n"
    "(B) Would you describe yourself as reserved?",
    "(A) Do you engage in thrill-seeking or high risk-taking "
    "behaviors?\n"
    "(B) Do you always find yourself asking the question 'why'"
    " in most situations?",
    "(A) Would you describe yourself as confident, analytical, and ambitious?\n"
    "(B) DO you like to exert control by planning, organizing, and"
    "making decisions as early as possible?",
    "(A) Do you like to socialize a lot?\n"
    "(B)Do you have a small circle of friends?",
    "(A)Do you prefer abstract concepts and tend to focus on "
    "one big picture rather than concrete details?\n"
    "(B) Would you say you're focused on details and facts?",
    "(A) Would you describe yourself as open to criticism?\n"
    "(B) Would you describe yourself as sensitive?"

]

answera= persquestions.count("A")
answerb= persquestions.count("B")
print("You answered 'A'" + str(answera) + " times and you answered 'B'"
      +str(answerb)+ " times.")

if answera>answerb:
    print("Based on your responses you are an EXTROVERT!")
elif answerb>answera:
    print("Based on your responses, you are an INTROVERT!")
