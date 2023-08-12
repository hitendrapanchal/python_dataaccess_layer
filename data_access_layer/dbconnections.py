# dbconnections.py is responsible to give you connection(engine,base,session) for each seperate databases 
# if you have multiple databases 

   
#Create two database if your requirement is more than one database 
# e.g 
# 1) sqllite:for authentification
# 2) postgrel: for account/sales/marketing etc
# See at bottom you have two instances of class DB_CONN_AUTH & DB_CONN_ACCOUNTS

"""Create SQLAlchemy engine and session objects."""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data_access_layer.dbfactory import createDBEngine
from data_access_layer.dbconnection_config import CONNECTION_CONFIG
from sqlalchemy.future.engine import Engine

  
class DBConnections:
    DATABASE_TYPE_NAME:str
    DATABASE_INSTANCE_NAME:str
    DB_ENGINE:Engine
    DB_SESSION:None
    DB_BASE:None
    
    DB_CONNECTION_STATUS:str

    def __init__(self):
        pass

    def connect(self, connection_config:CONNECTION_CONFIG):
        try:
            self.DATABASE_TYPE_NAME=connection_config.database_type_name
            
            # Create database engine
            self.DB_ENGINE = createDBEngine(connection_config)
            
            # Create database session
            Session = sessionmaker(bind=self.DB_ENGINE)
            self.DB_SESSION=Session()

            # Create database base
            self.DB_BASE = declarative_base()
        except Exception as exp:
            self.DB_CONNECTION_STATUS="FAILED"
            raise exp
        else:
            self.DB_CONNECTION_STATUS="SUCCESS"


DB_CONN_AUTH=DBConnections()
DB_CONN_ACCOUNTS=DBConnections()

def CreateDatabaseConnection(connection_config:CONNECTION_CONFIG):
    try:
        global DB_CONN_AUTH
        DB_CONN_AUTH.connect(connection_config)
    except Exception as exp:
        raise exp
    else:
        pass    

def CreateDatabaseConnectionForAccounts(connection_config:CONNECTION_CONFIG):
    try:
        global DB_CONN_ACCOUNTS
        DB_CONN_ACCOUNTS.connect(connection_config)
    except Exception as exp:
        raise exp
    else:
        pass    
    