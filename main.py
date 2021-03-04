from flask import Flask
from data import db_session
from data.users import User
from data.info import info

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for users in info:
        user = User()
        user.surname = users[0]
        user.name = users[1]
        user.age = users[2]
        user.position = users[3]
        user.speciality = users[4]
        user.address = users[5]
        user.email = users[6]
        user.hashed_password = users[7]
        db_sess.add(user)
        db_sess.commit()

#
    # user1 = User()
    # user1.surname = "Ridley"
    # user1.name = "Max"
    # user1.age = 21
    # user1.position = "colonist"
    # user1.speciality = "research engineer"
    # user1.address = "module_2"
    # user1.email = "MaxMars@mars.org"
    # user1.hashed_password = "max"
    # db_sess.add(user1)
    # db_sess.commit()
#
    # user2 = User()
    # user2.surname = "Cook"
    # user2.name = "Bob"
    # user2.age = 21
    # user2.position = "cook"
    # user2.speciality = "cook"
    # user2.address = "module_2"
    # user2.email = "book.cook@mars.org"
    # user2.hashed_password = "bobcok"
    # db_sess.add(user2)
    # db_sess.commit()
#
    # user3 = User()
    # user3.surname = "Scott"
    # user3.name = "Adam"
    # user3.age = 21
    # user3.position = "doctor"
    # user3.speciality = "doctor"
    # user3.address = "module_2"
    # user3.email = "scott_doc@mars.org"
    # user3.hashed_password = "doc"
    # db_sess.add(user3)
    # db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
