/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OuterComposite model module.
 * @module model/OuterComposite
 * @version 1.0.0
 */
class OuterComposite {
    /**
     * Constructs a new <code>OuterComposite</code>.
     * @alias module:model/OuterComposite
     */
    constructor() { 
        
        OuterComposite.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OuterComposite</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OuterComposite} obj Optional instance to populate.
     * @return {module:model/OuterComposite} The populated <code>OuterComposite</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OuterComposite();

            if (data.hasOwnProperty('my_number')) {
                obj['my_number'] = ApiClient.convertToType(data['my_number'], 'Number');
            }
            if (data.hasOwnProperty('my_string')) {
                obj['my_string'] = ApiClient.convertToType(data['my_string'], 'String');
            }
            if (data.hasOwnProperty('my_boolean')) {
                obj['my_boolean'] = ApiClient.convertToType(data['my_boolean'], 'Boolean');
            }
        }
        return obj;
    }


}

/**
 * @member {Number} my_number
 */
OuterComposite.prototype['my_number'] = undefined;

/**
 * @member {String} my_string
 */
OuterComposite.prototype['my_string'] = undefined;

/**
 * @member {Boolean} my_boolean
 */
OuterComposite.prototype['my_boolean'] = undefined;






export default OuterComposite;

