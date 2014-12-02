#import model
import csv

#insert data into the database


def load_users(session):
#populate users table with users        
    user_1 = ["Simon Says", "pass1"]

    user_2 = ["Black Mamba", "pass2"]
  
    user_3 = ["Matilda Berkhart", "pass3"]
    
    user_4 = ["Sesame Street", "pass4"]

    user_5 = ["Busta Move", "pass5"]

    user_6 = ["Monkey Butt", "pass6"]

    user_7 = ["Hakuna Matata", "pass7"]

    user_8 = ["Ape Attack", "pass8"]

    user_9 = ["Robot Ninja", "pass9"]

    user_10 = ["Turtle Dove", "pass10"]



    user1 = model.User(  
                        name =user_1[0],
                        room=room)
                   

    user2 = model.User( 
                        name =user_2[0],
                        password=user_2[1])

    user3 = model.User( 
                        name =user_3[0],
                        password=user_3[1])


    user4 = model.User( 
                        name =user_4[0],
                        password=user_4[1])

    user5 = model.User( 
                        name =user_5[0],
                        password=user_5[1])

    user6 = model.User( 
                        name =user_6[0],
                        password=user_6[1])

    user7 = model.User( 
                        name =user_7[0],
                        password=user_7[1])

    user8 = model.User( 
                        name =user_8[0],
                        password=user_8[1])

    user9 = model.User( 
                        name =user_9[0],
                        password=user_9[1])

    user10 = model.User( 
                        name =user_10[0],
                        password=user_10[1])


    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.add(user5)
    session.add(user6)
    session.add(user7)
    session.add(user8)
    session.add(user9)
    session.add(user10)

    session.commit()
    
def main(session):
    load_users(session)
   
   

if __name__ == "__main__":
    s = model.connect()
    main(s)