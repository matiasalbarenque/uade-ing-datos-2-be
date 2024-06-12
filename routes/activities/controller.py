from fastapi import APIRouter
from utils.schemas.activities import Activities
from utils.connectors.mongo_conn import MongoConnector

routes_activities = APIRouter()
db=[]
@routes_activities.post("/", response_model=Activities)
def create(activities: Activities):
    try:
        MongoConnector().insert_document(activities.dict())
        return activities
    except Exception as e:
        return e

# @routes_activities.get("/product/{id}")
# def get(id: str):
#     try:
#         # OPERATION CACHE
#         data = get_hash(key=id)

#         if len(data) == 0:
#             # OPERATION DB
#             product = list(filter(lambda field: field["id"] == id, db))[0]

#             # OPERATION CACHE
#             save_hash(key=id, data=product)

#             return product
#         return data
#     except Exception as e:
#         return e


# @routes_activities.delete("/delete/{id}")
# def delete(id: str):
#     # OPERACION DB
#     product = list(filter(lambda field: field["id"] == id, db))

#     if len(product) != 0:
#         db.remove(product[0])
#     # OPERACION CACHE
#     delete_hash(key=id, keys=["id","name","price","date"])
#     return {
#         "message": "success removed"
#     }