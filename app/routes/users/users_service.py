from app.common.db_connectors.mysql import MysqlConn
from app.common.utils.json import json_response

conn = MysqlConn()

def getUsersService():
    query = "select * from users"
    params = ()
    data = conn.fetch(query, params)
    return json_response(data)

def getUserInfoService(email: str):
    query = "select firstname, lastname, email, roles_id from users where email = %s"
    params = (email,)
    data = conn.fetch(query, params)
    return json_response(data)