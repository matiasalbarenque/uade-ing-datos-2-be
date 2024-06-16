from app.common.db_connectors.mongo_conn import MongoConnector
from app.dto.activities import ActivitiesDto
from pymongo.errors import PyMongoError
from typing import Dict
from app.common.utils.json import json_response

async def getActivitiesService(query_params: Dict):
    try:
        connector = MongoConnector()
        response = connector.find_documents(query_params) 
        documents = json_response(response)  # Convert documents to JSON serializable format
        print(documents)
        return response
    except PyMongoError as e:
        print(f"MongoDB error: {e}")
        return {"error": "Internal server error, please try again later."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}



async def addActivityService(req: ActivitiesDto):
    try:
        connector = MongoConnector()
        response = connector.insert_document(req.dict())
        return {"inserted_id": str(response)}
    except PyMongoError as e:
        print(f"MongoDB error: {e}")
        return {"error": "Internal server error, please try again later."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
    
async def addLikeService(activity_id: str, user_id: str):
    try:
        connector = MongoConnector()
        matched_count, modified_count = connector.add_like(activity_id, user_id)
        if matched_count == 0:
            return {"error": "Activity not found."}
        return {"matched_count": matched_count, "modified_count": modified_count}
    except PyMongoError as e:
        print(f"MongoDB error: {e}")
        return {"error": "Internal server error, please try again later."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Internal server error, please try again later."}
