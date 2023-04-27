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

/**
 * The Model404NotFoundResponse model module.
 * @module model/Model404NotFoundResponse
 * @version 1.0.0
 */
export class Model404NotFoundResponse {
  /**
   * Constructs a new <code>Model404NotFoundResponse</code>.
   * @alias module:model/Model404NotFoundResponse
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>Model404NotFoundResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Model404NotFoundResponse} obj Optional instance to populate.
   * @return {module:model/Model404NotFoundResponse} The populated <code>Model404NotFoundResponse</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new Model404NotFoundResponse();
      if (data.hasOwnProperty('code'))
        obj.code = ApiClient.convertToType(data['code'], 'Number');
      if (data.hasOwnProperty('message'))
        obj.message = ApiClient.convertToType(data['message'], 'String');
    }
    return obj;
  }
}

/**
 * @member {Number} code
 * @default 404
 */
Model404NotFoundResponse.prototype.code = 404;

/**
 * @member {String} message
 * @default 'NOT_FOUND'
 */
Model404NotFoundResponse.prototype.message = 'NOT_FOUND';

