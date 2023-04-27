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
import {ApiClient} from "../ApiClient";
import {Model200PriceDeletedResponse} from '../model/Model200PriceDeletedResponse';
import {Model201PriceCreatedResponse} from '../model/Model201PriceCreatedResponse';
import {Model400BadRequestResponse} from '../model/Model400BadRequestResponse';
import {Model401UnauthorizedResponse} from '../model/Model401UnauthorizedResponse';
import {Model403ForbiddenResponse} from '../model/Model403ForbiddenResponse';
import {Model404NotFoundResponse} from '../model/Model404NotFoundResponse';
import {Model409ConflictResponse} from '../model/Model409ConflictResponse';
import {Model503ServerUnavailableResponse} from '../model/Model503ServerUnavailableResponse';
import {PriceDetails} from '../model/PriceDetails';
import {PriceInfo} from '../model/PriceInfo';

/**
* Prices service.
* @module api/PricesApi
* @version 1.0.0
*/
export class PricesApi {

    /**
    * Constructs a new PricesApi. 
    * @alias module:api/PricesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the addPrice operation.
     * @callback moduleapi/PricesApi~addPriceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Model201PriceCreatedResponse{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add price to cars
     * @param {Object} opts Optional parameters
     * @param {module:model/PriceInfo} opts.body Adding price
     * @param {module:api/PricesApi~addPriceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    addPrice(opts, callback) {
      opts = opts || {};
      let postBody = opts['body'];

      let pathParams = {
        
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Model201PriceCreatedResponse;

      return this.apiClient.callApi(
        '/prices', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the deletePrice operation.
     * @callback moduleapi/PricesApi~deletePriceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Model200PriceDeletedResponse{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete price
     * @param {String} priceId 
     * @param {module:api/PricesApi~deletePriceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    deletePrice(priceId, callback) {
      
      let postBody = null;
      // verify the required parameter 'priceId' is set
      if (priceId === undefined || priceId === null) {
        throw new Error("Missing the required parameter 'priceId' when calling deletePrice");
      }

      let pathParams = {
        'price_id': priceId
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Model200PriceDeletedResponse;

      return this.apiClient.callApi(
        '/price/{price_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the getPrice operation.
     * @callback moduleapi/PricesApi~getPriceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PriceDetails{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get unique id
     * @param {String} priceId 
     * @param {module:api/PricesApi~getPriceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    getPrice(priceId, callback) {
      
      let postBody = null;
      // verify the required parameter 'priceId' is set
      if (priceId === undefined || priceId === null) {
        throw new Error("Missing the required parameter 'priceId' when calling getPrice");
      }

      let pathParams = {
        'price_id': priceId
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PriceDetails;

      return this.apiClient.callApi(
        '/price/{price_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the getPrices operation.
     * @callback moduleapi/PricesApi~getPricesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PriceDetails{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get prices
     * @param {module:api/PricesApi~getPricesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    getPrices(callback) {
      
      let postBody = null;

      let pathParams = {
        
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['applications/json', 'application/json'];
      let returnType = PriceDetails;

      return this.apiClient.callApi(
        '/prices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}