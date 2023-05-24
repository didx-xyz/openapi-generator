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

from openapi_client.model.order import Order

class StoreApi(Consumer):

    async def delete_order(self, *, order_id: str):
        """Delete purchase order by ID"""
        return await self.__delete_order(
            orderId=order_id,
        )

    async def get_inventory(self) -> Dict[str, int]:
        """Returns pet inventories by status"""
        return await self.__get_inventory(
        )

    async def get_order_by_id(self, *, order_id: int) -> Order:
        """Find purchase order by ID"""
        return await self.__get_order_by_id(
            orderId=order_id,
        )

    async def place_order(self, *, body: Order) -> Order:
        """Place an order for a pet"""
        return await self.__place_order(
            body=body,
        )

    @delete("/store/order/{orderId}")
    def __delete_order(self, *, orderId: str):
        """Internal uplink method for delete_order"""

    @returns.json
    @get("/store/inventory")
    def __get_inventory(self) -> Dict[str, int]:
        """Internal uplink method for get_inventory"""

    @returns.json
    @get("/store/order/{orderId}")
    def __get_order_by_id(self, *, orderId: int) -> Order:
        """Internal uplink method for get_order_by_id"""

    @returns.json
    @post("/store/order")
    def __place_order(self, *, body: Body(type=Order)) -> Order:
        """Internal uplink method for place_order"""
