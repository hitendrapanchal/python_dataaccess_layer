#Stricly follow the sequence for import
from data_access_layer.dbconnections import DB_CONN_AUTH, DB_CONN_ACCOUNTS
from data_access_layer.dbconnection_config import CONNECTION_CONFIG

#First Create connection and populate configs from .env
connection_config=CONNECTION_CONFIG()
connection_config.database_type_name="SQLLITE_MEMORY"
#connection_config.username="abc" -> Populate this from env config


#Now create database connection
from data_access_layer.dbconnections import CreateDatabaseConnection, CreateDatabaseConnectionForAccounts
CreateDatabaseConnection(connection_config)
CreateDatabaseConnectionForAccounts(connection_config)


#Now create tables on database
from data_access_layer.dbsetup.create_database import createTablesUserAuthentication,createTablesForAccounts
createTablesUserAuthentication()
createTablesForAccounts()


#Now you can use modesl/CRUD and DB operations
from test_app import testSqlLite
testSqlLite.createUser(DB_CONN_AUTH.DB_SESSION)
userlist=testSqlLite.showUser(DB_CONN_AUTH.DB_SESSION)
print(userlist[0].username)
print(userlist[0].first_name)

#Account DB
testSqlLite.createUserAccount(DB_CONN_ACCOUNTS.DB_SESSION)
userlist=testSqlLite.showUserAccount(DB_CONN_ACCOUNTS.DB_SESSION)
print(userlist[0].username)
print(userlist[0].first_name)