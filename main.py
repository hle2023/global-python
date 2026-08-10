from fastapi import FastAPI
import asyncio
from pydantic import BaseModel

#init
app = FastAPI()


#about
@app.get("/about")
def read_about():
    return {"message": "Welcome to Hung's web test"}
    
    
async def sim_func_delay(item_id: int, q: str):
    #fetch a mock network request data
    await asyncio.sleep(2)
    print(f'receive request data {q} for {item_id}')
    return {'item_id': item_id, 'status': 'ok'}

@app.get("/PLCSim/{item_id}")
async def read_item(item_id: int, q:  str= None):
    result = await sim_func_delay(item_id, q)
    return result

# Define the Pydantic schema for data validation
class PayloadPost(BaseModel):
    id: int
    content: str
    published: bool = True
    status: str
    
@app.post("/posts")
async def post_item(payload: PayloadPost):
    post_dict = payload.model_dump()
    #simulate delay in saving to database
    await asyncio.sleep(5)
    return {
        'message': 'Post is successful!',
        'data': {**post_dict, 'id': post_dict['id']}
    }