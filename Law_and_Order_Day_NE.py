#Note to Participants
print ("Hello! Welcome to the Law & Order Focus Day Jeopardy Game!")
print ("There are three categories in this game: Trial Terms, Supreme Court and Other Facts and five levels in each")
print ("Draw on the board a chart with six rows and three coloums")
print ("Write in the three categories into the first row")
print ("Write 100 in the second")
print ("Write 200 in the third")
print ("Write 300 in the fourth")
print ("Write 400 in the fifth")
print ("Write 500 in the sixth")
print ("Be sure to follow the instructions and in your responses remember spelling and capitilization")
print ("Erase the corresponding box when a question is answered")
print ("Seperate yourselves into three teams")
v = input("Ready?")
#for loop counts to 4
if v == ("yes"):
    x=0
    for x in range (1,4,1):
      print (x)

print("Let's test your knowledge!")
#def of function contains questions and input of answers
def jeopardy(team1_win, team2_win, team3_win):
    x = input("Choose Your Category: Trial Terms, Supreme Court or Other Facts ")
    if x == ("Trial Terms") or x == ("trial terms"):
       y = input("Choose Your Level (100, 200, 300, 400, 500)")
       if y== ("100"):
           print ("Capital Offense")
           c= input ("What is ")
           my_list= ["A crime punishable by death","a crime punishable by death", "crime punishable by death"]
           if c in my_list:
               print ("You Get 100 Points!")
               s= (input("What Team Are You?"))
               if s in my_list1:
                   team1_win= team1_win + 100
                   print ("Team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 100
                   print ("Team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 100
                   print ("Team 3: "+ str(team3_win))
           else:
               print ("You Lose 100 Points!")
               print (my_list)
               s= (input("What Team Are You?"))
               if s in my_list1:
                   team1_win= team1_win - 100
                   print ("Team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 100
                   print ("Team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 100
                   print ("Team 2: "+ str(team2_win))
       if y== ("200"):
           print ("Cross Examine")
           c= input ("What is ")
           my_list= ["Questioning of a witness by the attorney for the other side", "questioning of a witness by the opposing counsel", "questioning of a witness"]
           if c in my_list:
               print ("You Get 200 Points!")
               s= (input("What Team Are You?"))
               if s in my_list1:
                   team1_win= team1_win + 200
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 200
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 200
                   print ("team 3: "+ str(team3_win))
           else:
               print ("you lose 200 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 200
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 200
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 200
                   print ("team 3: "+ str(team2_win))
       if y== ("300"):
           print ("A written statement confirmed by oath or affirmation, for use as evidence in court.")
           c= input ("What is ")
           my_list= ["Affidavit", "affidavit"]
           if c in my_list:
               print ("you get 300 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 300
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 300
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 300
                   print ("team 3: "+ str(team3_win))
           else:
               print ("you lose 300 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 300
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 300
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 300
                   print ("team 3: "+ str(team2_win))
       if y== ("400"):
           print ("a person who brings a case against another in a court of law")
           c= input ("What is ")
           my_list= ["Plaintiff"]
           if c in my_list:
               print ("you get 400 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 400
                   print ("team 3: "+ str(team3_win))
           else:
               print ("you lose 400 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 400
                   print ("team 3: "+ str(team2_win))
       if y== ("500"):
           print ("The process of giving sworn evidence")
           c= input ("What is ")
           my_list= ["Deposition"]
           if c in my_list:
               print ("you get 500 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 500
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 500
                   print ("team 3: "+ str(team3_win))
           else:
               print ("you lose 500 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 500
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 500
                   print ("team 3: "+ str(team2_win))
    if x == ("Supreme Court"):
       y = input ("Choose Your Level (100, 200, 300, 400, 500)")
       if y== ("100"):
           print ("There are ___ judges on the Supreme Court")
           c= input ("What is ")
           my_list= ["9", "nine", "Nine"]
           if c in my_list:
               print ("you get 100 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 100
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 100
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 100
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 100 points!")
               s= (input("what team are you?"))
               print (my_list)
               if s in my_list1:
                   team1_win= team1_win - 100
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 100
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 100
                   print ("team 3: "+ str(team2_win))
       if y== ("200"):
          print ("The Supreme Court has the responsibility to do: A. Interpret the Constitution B. Elect legislators C. Appoint new justices")
          c= input ("What is ")
          my_list= ["A", "a"]
          if c in my_list:
               print ("you get 200 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 200
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 200
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 200
                   print ("team 3: "+ str(team3_win))
          else:
               print ("you lose 200 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 200
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 200
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 200
                   print ("team 3: "+ str(team2_win))
       if y== ("300"):
           print ("The U.S. Supreme Court can hear appeals from the state supreme courts: Answer True or False")
           c= input ("What is ")
           my_list= ["True", "true"]
           if c in my_list:
               print ("you get 300 points!")
               s = (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 300
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 300
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 300
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 300 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 300
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 300
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 300
                   print ("team 3: "+ str(team3_win))
       if y== ("400"):
           print ("How many women are currently on the Supreme Court?")
           c= input ("What is ")
           my_list= ["3", "Three", "three"]
           if c in my_list:
               print ("you get 400 points!")
               s = (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 400
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 400 points!")
               print (my_list)
               s = (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 400
                   print ("team 3: "+ str(team3_win))
       if y== ("500"):
           print ("Name someone currently on the Supreme Court (Remember to Capitilize Names)")
           c= input ("What is ")
           my_list= ["Brett Kavanaugh", "Kavanaugh", "Neil Gorsuch", "Gorsuch", "Elena Kagan", "Kagan", "Sonia Sotomayor", "Sotomayor", "Samuel Alito", "Alito", "Stephen Breyer", "Breyer", "Ruth Bader Ginsburg", "RBG", "Clarence Thomas", "Thomas", "John Roberts", "Roberts"]
           if c in my_list:
               print ("you get 500 points!")
               s = (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 500
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 500
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 500 points!")
               print (my_list)
               s = (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 500
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 500
                   print ("team 3: "+ str(team3_win))
    if x == ("Other Facts"):
        y = input ("Choose Your Level (100, 200, 300, 400, 500)")
        if y== ("100"):
            print ("Which party gets to make the opening and closing statement as well as the calls the first witnesses?")
            c= input ("What is ")
            my_list= ["Prosecution"]
            if c in my_list:
               print ("you get 100 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 100
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 100
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 100
                   print ("team 3: "+ str(team3_win))
            else: 
               print ("you lose 100 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 100
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 100
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 100
                   print ("team 3: "+ str(team2_win))
        if y== ("200"):
            print ("What is the highest federal court that makes decisions which are final?")
            c= input ("What is ")
            my_list= ["The Supreme Court"]
            if c in my_list:
                print ("you get 200 points!")
                s= (input("what team are you?"))
                if s in my_list1:
                   team1_win= team1_win + 200
                   print ("team 1: "+ str(team1_win))
                elif s in my_list2:
                    team2_win= team2_win + 200
                    print ("team 2: "+ str(team2_win))
                elif s in my_list3:
                    team3_win= team3_win + 200
                    print ("team 3: "+ str(team3_win))
            else: 
                print ("you lose 200 points!")
                print (my_list)
                s= (input("what team are you?"))
                if s in my_list1:
                    team1_win= team1_win - 200
                    print ("team 1: "+ str(team1_win))
                elif s in my_list2:
                   team2_win= team2_win - 200
                   print ("team 2: "+ str(team2_win))
                elif s in my_list3:
                   team3_win= team3_win - 200
                   print ("team 3: "+ str(team2_win))
        if y== ("300"):
           print ("True or false: A jury is mandatory in a criminal case?")
           c= input ("What is ")
           my_list= ["True", "true"]
           if c in my_list:
               print ("you get 300 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 300
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 300
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 300
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 300 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                  team1_win= team1_win - 300
                  print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                  team2_win= team2_win - 300
                  print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                  team3_win= team3_win - 300
                  print ("team 3: "+ str(team3_win))
        if y== ("400"):
           print ("What is the job of an appeals/appellate court?")
           c= input ("What is ")
           my_list= ["to review decisions made in lower courts"]
           if c in my_list:
               print ("you get 400 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 400
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 400 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 400
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win - 400
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win - 400
                   print ("team 3: "+ str(team3_win))
        if y== ("500"):
           print ("In an _____ system, the judge plays a more active role")
           c= input ("What is ")
           my_list= ["Inquisitional"]
           if c in my_list:
               print ("you get 500 points!")
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win + 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                   team2_win= team2_win + 500
                   print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                   team3_win= team3_win + 500
                   print ("team 3: "+ str(team3_win))
           else: 
               print ("you lose 500 points!")
               print (my_list)
               s= (input("what team are you?"))
               if s in my_list1:
                   team1_win= team1_win - 500
                   print ("team 1: "+ str(team1_win))
               elif s in my_list2:
                  team2_win= team2_win - 500
                  print ("team 2: "+ str(team2_win))
               elif s in my_list3:
                  team3_win= team3_win - 500
                  print ("team 3: "+ str(team3_win))
    i= input ("play again?") #point system 
    return(team1_win, team2_win, team3_win, i)
#score
team1_win=0
team2_win=0
team3_win=0

#for deciphering who g
my_list1 = ["team one", "team 1", "1"]
my_list2 = ["team two", "team 2", "2"]
my_list3 = ["team three","team 3", "3"]

i = "yes"

while i == ("yes"):
    score = jeopardy (team1_win, team2_win, team3_win)
#print score
    team1_win=score[0]
    team2_win=score[1]
    team3_win=score[2]
    i= score[3]
if i != "yes":
      print(team1_win, team2_win, team3_win)
#else:
#print (team1_win, team2_win, team3_win)

#call funtion
