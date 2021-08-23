/**
 * Example
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { DogAllOf } from './DogAllOf';
import { HttpFile } from '../http/http';

export class Dog {
    'bark'?: boolean;
    'breed'?: DogBreedEnum;

    static readonly discriminator: string | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "bark",
            "baseName": "bark",
            "type": "boolean",
            "format": ""
        },
        {
            "name": "breed",
            "baseName": "breed",
            "type": "DogBreedEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return Dog.attributeTypeMap;
    }

    public constructor() {
    }
}


export type DogBreedEnum = "Dingo" | "Husky" | "Retriever" | "Shepherd" ;

