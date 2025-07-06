from fastapi import APIRouter, HTTPException, status, Depends
from app.services.user import UserService
from app.models.user import UserRequest, UserResponse
from app.api.deps import get_user_service

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def list_users(user_service: UserService = Depends(get_user_service)):
  return await user_service.list_all_users()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(id: str, user_service: UserService = Depends(get_user_service)):
  if not id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")
    
  user = user_service.get_user_by_id(id)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return await user_service.get_user_by_id(id)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, user_service: UserService = Depends(get_user_service)):
  if not user.name:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User name is required")
  if len(user.name) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User name must be at least 1 character long")
  
  return await user_service.create_user(user)