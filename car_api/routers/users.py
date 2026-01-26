from fastapi import APIRouter, status
from car_api.schemas.users import UserListPublicSchema

router = APIRouter()

@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=UserListPublicSchema,
)
async def list_users():
    return {
        "users": [
            {
                'id': 1,
                'username': 'joao',
                'email': 'joao@gmail.com',
            },
            {
                'id': 2,
                'username': 'alice',
                'email': 'alice@gmail.com',
            },
            {
                'id': 3,
                'username': 'fernando',
                'email': 'fernando@gmail.com',
            }

        ]
    }