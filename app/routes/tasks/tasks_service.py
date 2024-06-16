from app.dto.tasks import TasksDto
from app.common.db_connectors.neo4j_conn import Neo4jConnector
from typing import Dict

async def getTasksService():
    try:
        connector = Neo4jConnector()
        response = connector.get_all_nodes('Task')
        return response
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}

async def addTaskService(req: TasksDto):
    try:
        connector = Neo4jConnector()
        connector.create_node('Task', req.dict())
        return {"inserted_id": req.dict()}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}

async def updateTaskService(req: TasksDto):
    try:
        connector = Neo4jConnector()
        properties = req.dict()
        value = properties['task_id']
        connector.update_node('Task','task_id',value, properties)
        return {"updated": value, "properties": properties}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
