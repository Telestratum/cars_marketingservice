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
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.MarketingManagementService);
  }
}(this, function(expect, MarketingManagementService) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('PriceDetails', function() {
      beforeEach(function() {
        instance = new MarketingManagementService.PriceDetails();
      });

      it('should create an instance of PriceDetails', function() {
        // TODO: update the code to test PriceDetails
        expect(instance).to.be.a(MarketingManagementService.PriceDetails);
      });

      it('should have the property priceId (base name: "price_id")', function() {
        // TODO: update the code to test the property priceId
        expect(instance).to.have.property('priceId');
        // expect(instance.priceId).to.be(expectedValueLiteral);
      });

    });
  });

}));