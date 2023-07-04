from fastapi import FastAPI, status
from api.routers import users


app = FastAPI()

app.include_router(users.router, prefix='/users', tags=['Users'])


@app.get("/", tags=['HealthCheck'], status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'alive'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost",
                port=8003, reload=True)
