#from sqlalchemy import URL
from sqlalchemy import create_engine
from data_access_layer.dbconnection_config import CONNECTION_CONFIG
#dbName: set/get this from application configuration 
dbName="SQLLITE_MEMORY"  ## POSTGRESQL, MYSQL, ORACLE, MSSQL, SQLLITE,SQLLITE_MEMORY
       
    
def createDBEngine(connection_config:CONNECTION_CONFIG):
    try:
        db_url = createURL(connection_config)
        print(db_url)
        engine = create_engine(db_url)
        return engine
    except Exception as exp:
        raise exp
    else:
        pass    
    
    
def createURL(connection_config:CONNECTION_CONFIG):
    try:
        dbName=connection_config.database_type_name
        if (dbName=='POSTGRESQL'):
            dbURL=GetURLforPostreSQL()
        elif (dbName=='MYSQL'):
            dbURL=GetURLforMySQL()
        elif (dbName=='ORACLE'):
            dbURL=GetURLforOracle()
        elif (dbName=='MSSQL'):
            dbURL=GetURLforMicrosoftSQLServer()
        elif (dbName=='SQLLITE'):
            dbURL=GetURLforSQLite()
        elif (dbName=='SQLLITE_MEMORY'):
            dbURL=GetURLforSQLiteInMemory()
            
        #Creating URLs Programmatically
        # url_object = URL.create(
        # "postgresql+pg8000",
        # username="dbuser",
        # password="kx@jj5/g",  # plain (unescaped) text
        # host="pghost10",
        # database="appdb",
        # )
        return dbURL
    except Exception as exp:
        raise exp
    else:
        pass    
    
        

def GetURLforPostreSQL():
    # default
    url = "postgresql://scott:tiger@localhost/mydatabase"
    # # psycopg2
    # "postgresql+psycopg2://scott:tiger@localhost/mydatabase"

    # # pg8000
    # "postgresql+pg8000://scott:tiger@localhost/mydatabase"
    return url
    
def GetURLforMySQL():
    # default
    url = "mysql://scott:tiger@localhost/foo"
 
    # # mysqlclient (a maintained fork of MySQL-Python)
    # "mysql+mysqldb://scott:tiger@localhost/foo"

    # # PyMySQL
    # "mysql+pymysql://scott:tiger@localhost/foo"
    
    return url
    
def GetURLforOracle():
    # default
    url = "oracle://scott:tiger@127.0.0.1:1521/sidname"
    #"oracle+cx_oracle://scott:tiger@tnsname"
    
    return url
    
def GetURLforMicrosoftSQLServer():
    # default
    url = "mssql+pyodbc://scott:tiger@mydsn"
    
    # # pyodbc
    # "mssql+pyodbc://scott:tiger@mydsn"
    # # pymssql
    # "mssql+pymssql://scott:tiger@hostname:port/dbname"
    return url
    
def GetURLforSQLite():
    # default
    url = "sqlite:///foo.db"

    # # Unix/Mac - 4 initial slashes in total
    # "sqlite:////absolute/path/to/foo.db"
    # # Windows
    # "sqlite:///C:\\path\\to\\foo.db"
    # # Windows alternative using raw string
    # r"sqlite:///C:\path\to\foo.db"

    return url

def GetURLforSQLiteInMemory():
    # default
    url = "sqlite://"
    return url





# Database URLs:
# ====================
# dialect+driver://username:password@host:port/database

# Below are  Dialects:
# ~~~~~~~~~~~~~~~~~~~
# SQLite:
# ======
# # sqlite://<nohostname>/<path>
# # where <path> is relative:
# engine = create_engine("sqlite:///foo.db")

# # Unix/Mac - 4 initial slashes in total
# engine = create_engine("sqlite:////absolute/path/to/foo.db")

# # Windows
# engine = create_engine("sqlite:///C:\\path\\to\\foo.db")

# # Windows alternative using raw string
# engine = create_engine(r"sqlite:///C:\path\to\foo.db")

# SQLite :memory
# ======
# engine = create_engine("sqlite://")

# PostgreSQL:
# ==========
# # default
# engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")
# # psycopg2
# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")
# # pg8000
# engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")

# MySQL:
# ==========
# # default
# engine = create_engine("mysql://scott:tiger@localhost/foo")
# # mysqlclient (a maintained fork of MySQL-Python)
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")
# # PyMySQL
# engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")

# Oracle:
# ==========
# engine = create_engine("oracle://scott:tiger@127.0.0.1:1521/sidname")
# engine = create_engine("oracle+cx_oracle://scott:tiger@tnsname")

# Microsoft SQL Server:
# ====================
# # pyodbc
# engine = create_engine("mssql+pyodbc://scott:tiger@mydsn")
# # pymssql
# engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname")