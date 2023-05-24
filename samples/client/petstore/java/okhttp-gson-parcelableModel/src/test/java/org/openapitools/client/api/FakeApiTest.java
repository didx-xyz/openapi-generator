/*
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.math.BigDecimal;
import org.openapitools.client.model.Client;
import java.io.File;
import org.openapitools.client.model.FileSchemaTestClass;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import org.openapitools.client.model.OuterComposite;
import org.openapitools.client.model.User;
import org.openapitools.client.model.XmlItem;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FakeApi
 */
@Ignore
public class FakeApiTest {

    private final FakeApi api = new FakeApi();

    
    /**
     * creates an XmlItem
     *
     * this route creates an XmlItem
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createXmlItemTest() throws ApiException {
        XmlItem xmlItem = null;
        api.createXmlItem(xmlItem);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Test serialization of outer boolean types
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void fakeOuterBooleanSerializeTest() throws ApiException {
        Boolean body = null;
        Boolean response = api.fakeOuterBooleanSerialize(body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Test serialization of object with outer number type
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void fakeOuterCompositeSerializeTest() throws ApiException {
        OuterComposite body = null;
        OuterComposite response = api.fakeOuterCompositeSerialize(body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Test serialization of outer number types
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void fakeOuterNumberSerializeTest() throws ApiException {
        BigDecimal body = null;
        BigDecimal response = api.fakeOuterNumberSerialize(body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Test serialization of outer string types
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void fakeOuterStringSerializeTest() throws ApiException {
        String body = null;
        String response = api.fakeOuterStringSerialize(body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * For this test, the body for this request much reference a schema named &#x60;File&#x60;.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testBodyWithFileSchemaTest() throws ApiException {
        FileSchemaTestClass body = null;
        api.testBodyWithFileSchema(body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testBodyWithQueryParamsTest() throws ApiException {
        String query = null;
        User body = null;
        api.testBodyWithQueryParams(query, body);

        // TODO: test validations
    }
    
    /**
     * To test \&quot;client\&quot; model
     *
     * To test \&quot;client\&quot; model
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testClientModelTest() throws ApiException {
        Client body = null;
        Client response = api.testClientModel(body);

        // TODO: test validations
    }
    
    /**
     * Fake endpoint for testing various parameters  假端點  偽のエンドポイント  가짜 엔드 포인트
     *
     * Fake endpoint for testing various parameters  假端點  偽のエンドポイント  가짜 엔드 포인트
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testEndpointParametersTest() throws ApiException {
        BigDecimal number = null;
        Double _double = null;
        String patternWithoutDelimiter = null;
        byte[] _byte = null;
        Integer integer = null;
        Integer int32 = null;
        Long int64 = null;
        Float _float = null;
        String string = null;
        File binary = null;
        LocalDate date = null;
        OffsetDateTime dateTime = null;
        String password = null;
        String paramCallback = null;
        api.testEndpointParameters(number, _double, patternWithoutDelimiter, _byte, integer, int32, int64, _float, string, binary, date, dateTime, password, paramCallback);

        // TODO: test validations
    }
    
    /**
     * To test enum parameters
     *
     * To test enum parameters
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testEnumParametersTest() throws ApiException {
        List<String> enumHeaderStringArray = null;
        String enumHeaderString = null;
        List<String> enumQueryStringArray = null;
        String enumQueryString = null;
        Integer enumQueryInteger = null;
        Double enumQueryDouble = null;
        List<String> enumFormStringArray = null;
        String enumFormString = null;
        api.testEnumParameters(enumHeaderStringArray, enumHeaderString, enumQueryStringArray, enumQueryString, enumQueryInteger, enumQueryDouble, enumFormStringArray, enumFormString);

        // TODO: test validations
    }
    
    /**
     * Fake endpoint to test group parameters (optional)
     *
     * Fake endpoint to test group parameters (optional)
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testGroupParametersTest() throws ApiException {
        Integer requiredStringGroup = null;
        Boolean requiredBooleanGroup = null;
        Long requiredInt64Group = null;
        Integer stringGroup = null;
        Boolean booleanGroup = null;
        Long int64Group = null;
        api.testGroupParameters(requiredStringGroup, requiredBooleanGroup, requiredInt64Group)
                .stringGroup(stringGroup)
                .booleanGroup(booleanGroup)
                .int64Group(int64Group)
                .execute();

        // TODO: test validations
    }
    
    /**
     * test inline additionalProperties
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testInlineAdditionalPropertiesTest() throws ApiException {
        Map<String, String> param = null;
        api.testInlineAdditionalProperties(param);

        // TODO: test validations
    }
    
    /**
     * test json serialization of form data
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testJsonFormDataTest() throws ApiException {
        String param = null;
        String param2 = null;
        api.testJsonFormData(param, param2);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * To test the collection format in query parameters
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void testQueryParameterCollectionFormatTest() throws ApiException {
        List<String> pipe = null;
        List<String> ioutil = null;
        List<String> http = null;
        List<String> url = null;
        List<String> context = null;
        api.testQueryParameterCollectionFormat(pipe, ioutil, http, url, context);

        // TODO: test validations
    }
    
}
