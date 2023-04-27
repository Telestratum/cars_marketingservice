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
import {PriceInfo} from './PriceInfo';

/**
 * The PriceDetails model module.
 * @module model/PriceDetails
 * @version 1.0.0
 */
export class PriceDetails extends PriceInfo {
  /**
   * Constructs a new <code>PriceDetails</code>.
   * @alias module:model/PriceDetails
   * @class
   * @extends module:model/PriceInfo
   * @param modelId {} 
   * @param price {} 
   * @param startDate {} 
   * @param endDate {} 
   */
  constructor(modelId, price, startDate, endDate) {
    super(modelId, price, startDate, endDate);
  }

  /**
   * Constructs a <code>PriceDetails</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PriceDetails} obj Optional instance to populate.
   * @return {module:model/PriceDetails} The populated <code>PriceDetails</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PriceDetails();
      PriceInfo.constructFromObject(data, obj);
      if (data.hasOwnProperty('price_id'))
        obj.priceId = ApiClient.convertToType(data['price_id'], 'String');
    }
    return obj;
  }
}

/**
 * @member {String} priceId
 */
PriceDetails.prototype.priceId = undefined;

