#written by megan 
listOfScores=[] #makes empty list 


#written by boo
from time import sleep 

print("You all of a sudden are faced with a giant mountain")
print("you have to get to the top but before you do that answer this question... ")
sleep(1)
#written by megan
while True:
    q1=input(" Where do Muslims go to pray ? A) the north pole B) a mosque or C) outside ")
    q1=q1.lower()

    if q1=="a":
         print("That is incorrect ")
         print ("seriously doode are you mad ")
         print (" you will now restart the question ")
         question1score=0
         

    elif q1=="b":
        print (" well done that is the right answer")
        print("you can now move on a few steps")
        question1score=3
        break


    elif q1=="c":
        print ("that is incorrect")
        print (" you will now restart the question ")
        question1score=1
        
print("heres your score")
listOfScores.append(question1score)#adds to list 
print(listOfScores)#prints list 

#written by boo
print("Once you have done your first few steps you are next going to have to move a bolder that is in your way,")
print("Another question is most defenitly on it's way...")
sleep(1)
#written by megan
while True:
    q2=input(" True or false . Jesus told parables to make people hate god. ")
    q2=q2.lower()

    if q2=="true ":
         print("That is incorrect ")
         print ("seriously doode are you mad ")
         print (" you will now restart the question ")
         question2score=0

    elif q2=="false ":
        print (" well done that is the right answer")
        print("you can now move on a few steps")
        question2score=3
        break
listOfScores.append(question2score)#adds to list 
print(listOfScores)#prints list 

#written by boo
print("The questions are going to keep getting harder the more you play so be prepared...")
sleep(1)

#written by megan 
while True:
    q3=input(" where was Jesus born according to the christian bible a) tesco b) Bethleham   or c) Jurusalem ")
    q3=q3.lower()

    if q3=="a":
         print("That is incorrect ")
         print ("seriously doode are you mad ")
         print (" you will now restart the question ")
         question3score=0

    elif q3=="b":
        print (" well done that is the right answer")
        print("you can now move on a few steps")
        question3score=3
        break


    elif q3=="c":
        print ("that is incorrect")
        print (" you will now restart the question ")
        question3score=1
        
listOfScores.append(question3score)#adds to list 
print(listOfScores)#prints list 
        
#written by boo 
print("Since you have been so good at answering your tricky questions so far you are given a helping hand,")
print("which is...")
sleep(1)
print("You get to now get closer and closer to the top of the mountain without any question.")

#written by megan 
print ("Ok your halfway there only a few more questions left ")
print ("unfortunatly we cannot offer you anymore help so heres ur next question ")
while True:
	q4=input(" in the time of jesus how many gods did the Romans worship a)one b)many gods or c)  no gods  ")
	q4=q4.lower()
	
	
	if q4=="a":
		print("That is incorrect ")
		print("sorry you'll have to try again '")
		print (" you will now restart the question ")
		question4score=0
         

	elif q4=="b":
		print (" well done that is the right answer")
		print("you can now move on a few steps")
		question4score=3
		break

	elif q4=="c":
		print ("that is incorrect")
		print (" you will now restart the question ") 
		question4score=1
		
listOfScores.append(question4score)#adds to list 
print(listOfScores)#prints list 
        
print ("well done you will now move on to harder questions thta may just catch you out ")
print ("good luck ") 
while True:
	q5=input("During the time of jesus did the seducees a) eat cake b) live in the dessert or c) run the temple ")
	q5=q5.lower()
	
	
	if q5=="a":
		print("That is incorrect ")
		print("sorry you'll have to try again '")
		print (" you will now restart the question ")
		question5score=0
         

	elif q5=="c":
		print (" well done that is the right answer")
		print("you can now move on a few steps")
		question5score=3
		break


	elif q5=="b":
		print ("that is incorrect")
		print (" you will now restart the question ") 
		question5score=0
		
listOfScores.append(question5score)#adds to list 
print(listOfScores)#prints list 
        
       
while True :
	q6=input("During the time of jesus did the essences  a) eat cake b) live in the dessert or c) run the temple ")
		q6=q6.lower()
		
		
		 if q6=="a":
	         print("That is incorrect ")
	         print("sorry you'll have to try again '")
	         print (" you will now restart the question ")
	         question6score=0
	         
	         
	         
	
	    elif q6=="b":
	        print (" well done that is the right answer")
	        print("you can now move on a few steps")
	        question6score=3
	        break
	
	
	    elif q6=="c":
	        print ("that is incorrect")
	        print (" you will now restart the question ") 
	        question6score=0
        
listOfScores.append(question6score)#adds to list 
print(listOfScores)#prints list 
