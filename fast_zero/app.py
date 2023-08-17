from fastapi import FastAPI, HTTPException

from fast_zero.schemas import UserDB, UserPublic, UserSchema, UsersList

app = FastAPI()

database = []


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UsersList)
def get_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail="User not found")

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id