from app.dto.tasks import TasksDto
from app.dto.assignation import AssignDto

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
    
async def getTaskResponsibleService(query_params: Dict):
    try:
        connector = Neo4jConnector()
        task_id = query_params['task_id']
        response = connector.get_nodes_with_direct_relationship('User', 'TASK_ASSIGNED_TO', 'Task','task_id', task_id)
        return response
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}

async def getTaskCandidatesService(query_params: Dict):
    try:
        connector = Neo4jConnector()
        availability = query_params['availability']
        skill_id = query_params['skill_id']
        response = connector.get_nodes_with_property_greater_than_and_relationship('User', 'availability',availability, 'HAS_SKILL', 'Skill','skill_id', skill_id)
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
    
async def addTaskAssignationService(req: AssignDto):
    try:
        connector = Neo4jConnector()
        params = req.dict()
        start_node = params['start_node']
        end_node = params['end_node']
        relationship = 'TASK_ASSIGNED_TO'
        connector.create_relationship('User', 'user_id', start_node, relationship, 'Task', 'task_id', end_node)
        return {"assignation": f'User {start_node} -- {relationship} -- {end_node}'}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
