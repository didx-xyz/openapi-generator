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

from typing import Dict, List, Optional, Union # noqa: F401

from .uplink_util import bool_query

from openapi_client.model.api_response import ApiResponse
from openapi_client.model.pet import Pet

class PetApi(Consumer):

    async def add_pet(self, *, body: Pet):
        """Add a new pet to the store"""
        return await self.__add_pet(
            body=body,
        )

    async def delete_pet(self, *, pet_id: int, api_key: Optional[str] = None):
        """Deletes a pet"""
        return await self.__delete_pet(
            petId=pet_id,
            api_key=api_key,
        )

    async def find_pets_by_status(self, *, status: List[str]) -> List[Pet]:
        """Finds Pets by status"""
        return await self.__find_pets_by_status(
            status=status,
        )

    async def find_pets_by_tags(self, *, tags: List[str]) -> List[Pet]:
        """Finds Pets by tags"""
        return await self.__find_pets_by_tags(
            tags=tags,
        )

    async def get_pet_by_id(self, *, pet_id: int) -> Pet:
        """Find pet by ID"""
        return await self.__get_pet_by_id(
            petId=pet_id,
        )

    async def update_pet(self, *, body: Pet):
        """Update an existing pet"""
        return await self.__update_pet(
            body=body,
        )

    async def update_pet_with_form(self, *, pet_id: int, name: Optional[str] = None, status: Optional[str] = None):
        """Updates a pet in the store with form data"""
        return await self.__update_pet_with_form(
            petId=pet_id,
            name=name,
            status=status,
        )

    async def upload_file(self, *, pet_id: int, additional_metadata: Optional[str] = None, file: Optional[str] = None) -> ApiResponse:
        """uploads an image"""
        return await self.__upload_file(
            petId=pet_id,
            additional_metadata=additional_metadata,
            file=file,
        )

    @json
    @post("/pet")
    def __add_pet(self, *, body: Body(type=Pet)):
        """Internal uplink method for add_pet"""

    @delete("/pet/{petId}")
    def __delete_pet(self, *, petId: int, api_key: Header(None)):
        """Internal uplink method for delete_pet"""

    @returns.json
    @get("/pet/findByStatus")
    def __find_pets_by_status(self, *, status: Query) -> List[Pet]:
        """Internal uplink method for find_pets_by_status"""

    @returns.json
    @get("/pet/findByTags")
    def __find_pets_by_tags(self, *, tags: Query) -> List[Pet]:
        """Internal uplink method for find_pets_by_tags"""

    @returns.json
    @get("/pet/{petId}")
    def __get_pet_by_id(self, *, petId: int) -> Pet:
        """Internal uplink method for get_pet_by_id"""

    @json
    @put("/pet")
    def __update_pet(self, *, body: Body(type=Pet)):
        """Internal uplink method for update_pet"""

    @post("/pet/{petId}")
    def __update_pet_with_form(self, *, petId: int, name: Form(None), status: Form(None)):
        """Internal uplink method for update_pet_with_form"""

    @returns.json
    @post("/pet/{petId}/uploadImage")
    def __upload_file(self, *, petId: int, additional_metadata: Form(None), file: Form(None)) -> ApiResponse:
        """Internal uplink method for upload_file"""
