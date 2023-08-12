from data_access_layer.dbmodels.models import User,UserAccount
from data_access_layer.dbconnections import DB_CONN_AUTH, DB_CONN_ACCOUNTS
    
def createTablesUserAuthentication():
    try:
        DB_CONN_AUTH.DB_BASE.metadata.create_all(DB_CONN_AUTH.DB_ENGINE)
    except Exception as exp:
        raise exp
    else:
        pass
                
    

def createTablesForAccounts():
    try:
        DB_CONN_ACCOUNTS.DB_BASE.metadata.create_all(DB_CONN_ACCOUNTS.DB_ENGINE)
    except Exception as exp:
        raise exp
    else:
        pass    
