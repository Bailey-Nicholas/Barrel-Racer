from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.database import User
from utils.exceptions import UserDatabaseException
from pydantic import EmailStr
from models.users import UserWithPw
from typing import Optional

class UserQueries:
    def __init__(self, db: Session):

        """
        Initialize the UserQueries with a database session.

        Args:
            db (Session): An SQLAlchemy database session.

        Attributes:
            db (Session): The database session.
        """
        self.db = db

    def get_by_username(self, username: str) -> Optional[UserWithPw]:
        """
        Gets a user from the database by username

        Returns None if the user isn't found

        Raises a UserDatabaseException if getting the user fails
        """
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if not user:
                return None
            return UserWithPw(
                id=user.id, username=user.username, email=user.email,
                password=user.password, first_name=user.first_name,
                last_name=user.last_name
            )
        except SQLAlchemyError as e:
            print(e)
            raise UserDatabaseException(f"Error getting user {username}")

    def get_by_id(self, id: int) -> Optional[UserWithPw]:
        """
        Gets a user from the database by user id

        Returns None if the user isn't found

        Raises a UserDatabaseException if getting the user fails
        """
        try:
            user = self.db.query(User).filter(User.id == id).first()
            if not user:
                return None
            return UserWithPw(
                id=user.id, username=user.username, email=user.email,
                password=user.password, first_name=user.first_name,
                last_name=user.last_name
            )
        except SQLAlchemyError as e:
            print(e)
            raise UserDatabaseException(f"Error getting user with id {id}")

    def create_user(self, username: str, email: EmailStr, hashed_password: str, first_name: str, last_name: str) -> UserWithPw:
        """
        Creates a new user in the database

        Raises a UserDatabaseException if creating the user fails
        """
        try:
            user = User(
                username=username,
                email=email,
                password=hashed_password,
                first_name=first_name,
                last_name=last_name
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return UserWithPw(
                id=user.id, username=user.username, email=user.email,
                password=user.password, first_name=user.first_name,
                last_name=user.last_name
            )
        except SQLAlchemyError:
            self.db.rollback()
            raise UserDatabaseException(f"Could not create user with username {username}")
