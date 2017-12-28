from config.config import ConfigParams
import pymysql

config_parameters=ConfigParams()
s,u,d,p = config_parameters.dbConfig()
conn=pymysql.connect(s,u,d,p,as_dict=True)
cursor=conn.cursor()