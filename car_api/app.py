from fastapi import FastAPI, status
import car_api.routers.users as users_router

app = FastAPI()

app.include_router(
    router=users_router.router,
    prefix="/api/v1/users",
    tags=["users"]
)
@app.get("/health_check",status_code=status.HTTP_200_OK)
def health_check():
    return {"status":"ok"}
