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
import {OfferDetails} from './OfferDetails';

/**
 * The Model200OfferDeletedResponse model module.
 * @module model/Model200OfferDeletedResponse
 * @version 1.0.0
 */
export class Model200OfferDeletedResponse {
  /**
   * Constructs a new <code>Model200OfferDeletedResponse</code>.
   * @alias module:model/Model200OfferDeletedResponse
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>Model200OfferDeletedResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Model200OfferDeletedResponse} obj Optional instance to populate.
   * @return {module:model/Model200OfferDeletedResponse} The populated <code>Model200OfferDeletedResponse</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new Model200OfferDeletedResponse();
      if (data.hasOwnProperty('code'))
        obj.code = ApiClient.convertToType(data['code'], 'Number');
      if (data.hasOwnProperty('message'))
        obj.message = ApiClient.convertToType(data['message'], 'String');
      if (data.hasOwnProperty('data'))
        obj.data = ApiClient.convertToType(data['data'], [OfferDetails]);
    }
    return obj;
  }
}

/**
 * @member {Number} code
 * @default 200
 */
Model200OfferDeletedResponse.prototype.code = 200;

/**
 * @member {String} message
 * @default 'ok'
 */
Model200OfferDeletedResponse.prototype.message = 'ok';

/**
 * @member {Array.<module:model/OfferDetails>} data
 */
Model200OfferDeletedResponse.prototype.data = undefined;

