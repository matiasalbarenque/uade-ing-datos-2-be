from app.common.db_connectors.mysql import MysqlConn
from app.common.utils.json import json_response

conn = MysqlConn()

def getRolesService():
    query = "select * from roles"
    params = ()
    data = conn.fetch(query, params)
    return json_response(data)

def getUserPermissions(userId: str):
    try:
        query = "select r.* from roles r join users on roles_id = r.id where users.id = %s"
        params = (userId)
        data = conn.fetch(query, params)
        return json_response(data[0])
    except Exception as error:
            raise Exception(error)
    
