"""
Pydantic Models for Users.
"""
from pydantic import BaseModel, EmailStr, constr


class UserRequest(BaseModel):
    """
    Represents a the parameters needed to create a new user
    """

    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    """
    Represents a user, with the password not included
    """

    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserWithPw(BaseModel):
    """
    Represents a user with password included
    """

    id: int
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
