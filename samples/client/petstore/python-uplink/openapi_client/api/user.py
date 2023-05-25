from uplink import (
    Consumer,
    Path,
    Query,
    Body,
    Header,
    get,
    post,
    patch,
    put,
    delete,
    returns,
    json,
)

from typing import Any, Dict, List, Optional, Union # noqa: F401

from .uplink_util import bool_query

from openapi_client.model.user import User

class UserApi(Consumer):

    async def create_user(self, *, body: User):
        """Create user"""
        return await self.__create_user(
            body=body,
        )

    async def create_users_with_array_input(self, *, body: List[User]):
        """Creates list of users with given input array"""
        return await self.__create_users_with_array_input(
            body=body,
        )

    async def create_users_with_list_input(self, *, body: List[User]):
        """Creates list of users with given input array"""
        return await self.__create_users_with_list_input(
            body=body,
        )

    async def delete_user(self, *, username: str):
        """Delete user"""
        return await self.__delete_user(
            username=username,
        )

    async def get_user_by_name(self, *, username: str) -> User:
        """Get user by user name"""
        return await self.__get_user_by_name(
            username=username,
        )

    async def login_user(self, *, username: str, password: str) -> str:
        """Logs user into the system"""
        return await self.__login_user(
            username=username,
            password=password,
        )

    async def logout_user(self):
        """Logs out current logged in user session"""
        return await self.__logout_user(
        )

    async def update_user(self, *, username: str, body: User):
        """Updated user"""
        return await self.__update_user(
            username=username,
            body=body,
        )

    @post("/user")
    def __create_user(self, *, body: Body(type=User)):
        """Internal uplink method for create_user"""

    @post("/user/createWithArray")
    def __create_users_with_array_input(self, *, body: Body(type=List[User])):
        """Internal uplink method for create_users_with_array_input"""

    @post("/user/createWithList")
    def __create_users_with_list_input(self, *, body: Body(type=List[User])):
        """Internal uplink method for create_users_with_list_input"""

    @delete("/user/{username}")
    def __delete_user(self, *, username: str):
        """Internal uplink method for delete_user"""

    @returns.json
    @get("/user/{username}")
    def __get_user_by_name(self, *, username: str) -> User:
        """Internal uplink method for get_user_by_name"""

    @returns.json
    @get("/user/login")
    def __login_user(self, *, username: Query, password: Query) -> str:
        """Internal uplink method for login_user"""

    @get("/user/logout")
    def __logout_user(self):
        """Internal uplink method for logout_user"""

    @put("/user/{username}")
    def __update_user(self, *, username: str, body: Body(type=User)):
        """Internal uplink method for update_user"""
