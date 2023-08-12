#from data_access_layer.dbconnection import global_db_session_obj
from data_access_layer.dbmodels import models
from data_access_layer.dbmodels_dao import user_model_dao

def createUser(session):
    """
    Create a user record via SQLAlchemy's ORM, and subsequently delete it.

    :return: None
    """
    user = models.User(
        username="admin",
        password="Password123lol",
        email="admin@example.com",
        first_name="Todd",
        last_name="Birchard",
        bio="I write tutorials on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    )
    user = user_model_dao.createUser(session,user)

def createUserAccount(session):
    """
    Create a user record via SQLAlchemy's ORM, and subsequently delete it.

    :return: None
    """
    user = models.User(
        username="admin_account",
        password="Password123lol",
        email="admin@example.com",
        first_name="Hitendra",
        last_name="Panchal",
        bio="I write tutorials on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    )
    user = user_model_dao.createUser(session,user)
   
def showUser(session):
    course_query = session.query(models.User)
    return course_query.all()

def showUserAccount(session):
    course_query = session.query(models.UserAccount)
    return course_query.all()