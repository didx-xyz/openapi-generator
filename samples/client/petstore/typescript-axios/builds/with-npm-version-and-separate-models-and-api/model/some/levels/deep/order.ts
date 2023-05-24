/* tslint:disable */
/* eslint-disable */
/**
 * OpenAPI Petstore
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */



/**
 * An order for a pets from the pet store
 * @export
 * @interface Order
 */
export interface Order {
    /**
     * 
     * @type {number}
     * @memberof Order
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof Order
     */
    'petId'?: number;
    /**
     * 
     * @type {number}
     * @memberof Order
     */
    'quantity'?: number;
    /**
     * 
     * @type {string}
     * @memberof Order
     */
    'shipDate'?: string;
    /**
     * Order Status
     * @type {string}
     * @memberof Order
     */
    'status'?: OrderStatusEnum;
    /**
     * 
     * @type {boolean}
     * @memberof Order
     */
    'complete'?: boolean;
}

export const OrderStatusEnum = {
    Placed: 'placed',
    Approved: 'approved',
    Delivered: 'delivered'
} as const;

export type OrderStatusEnum = typeof OrderStatusEnum[keyof typeof OrderStatusEnum];


