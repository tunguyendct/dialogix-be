from fastapi import APIRouter, HTTPException, status
from app.services.user import list_all_users as list_all_users_service, get_user_by_id as get_user_by_id_service

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