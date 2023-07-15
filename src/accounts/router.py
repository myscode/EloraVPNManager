import logging
from sqlite3 import IntegrityError

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import src.accounts.service as service
import src.users.service as user_service
from src.accounts.schemas import AccountCreate, AccountResponse, AccountModify, AccountsResponse
from src.admins.schemas import Admin
from src.database import get_db

router = APIRouter()

logger = logging.getLogger('uvicorn.error')


@router.post("/accounts/", tags=["Account"], response_model=AccountResponse)
def add_account(account: AccountCreate,
                db: Session = Depends(get_db),
                admin: Admin = Depends(Admin.get_current)):
    db_user = user_service.get_user(db, account.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    logger.info(f"Account expired at {account.expired_at}")
    logger.info(f"Account data limit  {account.data_limit}")

    try:
        db_account = service.create_account(db=db, db_user=db_user, account=account)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Account already exists")

    return db_account


@router.put("/accounts/{account_id}", tags=["Account"], response_model=AccountResponse)
def modify_account(account_id: int, account: AccountModify,
                   db: Session = Depends(get_db),
                   admin: Admin = Depends(Admin.get_current)):
    db_account = service.get_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")

    return service.update_account(db=db, db_account=db_account, modify=account)


@router.get("/accounts/{account_id}", tags=["Account"],
            response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db),
                admin: Admin = Depends(Admin.get_current)):
    db_account = service.get_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")

    return db_account


@router.delete("/accounts/{account_id}", tags=["Account"])
def delete_account(account_id: int, db: Session = Depends(get_db),
                   admin: Admin = Depends(Admin.get_current)):
    db_account = service.get_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")

    service.remove_account(db=db, db_account=db_account)
    return {}


@router.get("/accounts/", tags=['Account'], response_model=AccountsResponse)
def get_accounts(
        db: Session = Depends(get_db),
        admin: Admin = Depends(Admin.get_current)
):
    accounts, count = service.get_accounts(db=db)

    return {"accounts": accounts, "total": count}