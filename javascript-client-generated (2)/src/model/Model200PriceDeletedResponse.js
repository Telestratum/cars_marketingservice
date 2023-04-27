/*
 * Marketing Management Service
 * A service for adding carmodels, offers and prices for cars
 *
 * OpenAPI spec version: 1.0.0
 * Contact: hariprasath.narayanasamy@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.42
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from '../ApiClient';
import {PriceDetails} from './PriceDetails';

/**
 * The Model200PriceDeletedResponse model module.
 * @module model/Model200PriceDeletedResponse
 * @version 1.0.0
 */
export class Model200PriceDeletedResponse {
  /**
   * Constructs a new <code>Model200PriceDeletedResponse</code>.
   * @alias module:model/Model200PriceDeletedResponse
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>Model200PriceDeletedResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Model200PriceDeletedResponse} obj Optional instance to populate.
   * @return {module:model/Model200PriceDeletedResponse} The populated <code>Model200PriceDeletedResponse</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new Model200PriceDeletedResponse();
      if (data.hasOwnProperty('code'))
        obj.code = ApiClient.convertToType(data['code'], 'Number');
      if (data.hasOwnProperty('message'))
        obj.message = ApiClient.convertToType(data['message'], 'String');
      if (data.hasOwnProperty('data'))
        obj.data = ApiClient.convertToType(data['data'], [PriceDetails]);
    }
    return obj;
  }
}

/**
 * @member {Number} code
 * @default 200
 */
Model200PriceDeletedResponse.prototype.code = 200;

/**
 * @member {String} message
 * @default 'ok'
 */
Model200PriceDeletedResponse.prototype.message = 'ok';

/**
 * @member {Array.<module:model/PriceDetails>} data
 */
Model200PriceDeletedResponse.prototype.data = undefined;
