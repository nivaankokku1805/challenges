import random

class FruitQuiz:
    
    def __init__(self):
        
        
        self.fruits={'apple':'red',
                     'orange': 'ornage'
                     'watermelon': 'red and green and black'
                     'banana': 'yellow'}
    
def quiz(self):
    while(True):
        fruit,color = random.choice(list(self.fruits.items()))
        print("What is the color of{}".format(fruit))
        user_answer = input()
        
        if(user_anser.lower() == color):
            print("Correct anser")
            
        else:
            print("Wrong answer")
            
        option = int(input("enter 0, if you want to play again otherwise 1 to quit the game :"))
        
        if (option):
            break
        
print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()
