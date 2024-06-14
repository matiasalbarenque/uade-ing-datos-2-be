from app.dto.activities import ActivitiesDto
from app.common.db_connectors.mongo_conn import MongoConnector

def getActivitiesService():
    try:
        response = MongoConnector().find_document()
        return response
    except Exception as e:
        return e

def addActivity(req: ActivitiesDto):
    try:
        response = MongoConnector().insert_document(req)
        return response
    except Exception as e:
        return e
