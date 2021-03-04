from flask import Flask
from data import db_session
from data.users import User
from data.info import info
from data.jobs import Jobs

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

    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.is_finished = False
    app.run()


if __name__ == '__main__':
    main()
