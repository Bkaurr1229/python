import random
from data_container import data
current_score=0
play_again=True
B= random.choice(data)
while play_again:
    A=B
    B= random.choice(data)
    if A==B:
        B=random.choice(data)

    # score increase
    print(f"COMPARE A- name:{A['name']}\n description:{A['description']}")
    print(f"COMPARE B-{B['name']}\n description:{B['description']}")
    
    answer=input("who has more followers? Type'A'or'B'")
    follower_a=A['subscribers']
    follower_b=B['subscribers']
    current_score+=1
    if follower_a > follower_b and answer == 'A' or follower_b>follower_a and answer =='B' :
        print(f"you are right your score:{current_score}")
    else:
        play_again=False
        print(f"sorry,you lose your score is {current_score}")
