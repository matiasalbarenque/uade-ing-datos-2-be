from app.dto.projects import ProjectDto
from app.dto.assignation import AssignDto

from app.common.db_connectors.neo4j_conn import Neo4jConnector
from typing import Dict


async def getProjectService():
    try:
        connector = Neo4jConnector()
        response = connector.get_all_nodes('Project')
        return response
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
    
async def addProjectService(req: ProjectDto):
    try:
        connector = Neo4jConnector()
        connector.create_node('Project', req.dict())
        #TO DO: crear la relacion OWNS con el user que ejecuto la creacion del proyecto
        return {"inserted_id": req.dict()}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}

async def updateProjectService(req: ProjectDto):
    try:
        connector = Neo4jConnector()
        properties = req.dict()
        value = properties['project_id']
        connector.update_node('Project','project_id',value, properties)
        return {"updated": value, "properties": properties}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
    
    
async def addProjectTaskService(req: AssignDto):
    try:
        connector = Neo4jConnector()
        connector.create_relationship('Task', 'task_id', 'TSK02','TASK_ASSIGNED_TO','Project', 'project_id', 'P1')
        return {"inserted_id": 'OK'}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}