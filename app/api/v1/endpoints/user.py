from fastapi import APIRouter, HTTPException, status
from app.services.user import list_all_users as list_all_users_service, get_user_by_id as get_user_by_id_service, create_user as create_user_service
from app.models.user import UserRequest

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def list_users():
  return list_all_users_service()
  
@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(id: str):
  if not id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")
    
  user = get_user_by_id_service(id)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return get_user_by_id_service(id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest):
  if not user.name:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User name is required")
  if len(user.name) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User name must be at least 1 character long")
  
  return create_user_service(user)