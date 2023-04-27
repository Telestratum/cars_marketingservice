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
    describe('PriceInfo', function() {
      beforeEach(function() {
        instance = new MarketingManagementService.PriceInfo();
      });

      it('should create an instance of PriceInfo', function() {
        // TODO: update the code to test PriceInfo
        expect(instance).to.be.a(MarketingManagementService.PriceInfo);
      });

      it('should have the property modelId (base name: "model_id")', function() {
        // TODO: update the code to test the property modelId
        expect(instance).to.have.property('modelId');
        // expect(instance.modelId).to.be(expectedValueLiteral);
      });

      it('should have the property price (base name: "price")', function() {
        // TODO: update the code to test the property price
        expect(instance).to.have.property('price');
        // expect(instance.price).to.be(expectedValueLiteral);
      });

      it('should have the property startDate (base name: "start_date")', function() {
        // TODO: update the code to test the property startDate
        expect(instance).to.have.property('startDate');
        // expect(instance.startDate).to.be(expectedValueLiteral);
      });

      it('should have the property endDate (base name: "end_date")', function() {
        // TODO: update the code to test the property endDate
        expect(instance).to.have.property('endDate');
        // expect(instance.endDate).to.be(expectedValueLiteral);
      });

    });
  });

}));