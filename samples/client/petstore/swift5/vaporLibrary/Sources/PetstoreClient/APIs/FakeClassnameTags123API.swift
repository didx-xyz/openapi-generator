//
// FakeClassnameTags123API.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation
import Vapor
#if canImport(AnyCodable)
import AnyCodable
#endif

open class FakeClassnameTags123API {

    /**
     To test class name in snake case
     PATCH /fake_classname_test
     To test class name in snake case
     - API Key:
       - type: apiKey api_key_query (QUERY)
       - name: api_key_query
     - parameter body: (body) client model 
     - returns: `EventLoopFuture` of `ClientResponse` 
     */
    open class func testClassnameRaw(body: Client, headers: HTTPHeaders = PetstoreClientAPI.customHeaders, beforeSend: (inout ClientRequest) throws -> () = { _ in }) -> EventLoopFuture<ClientResponse> {
        let localVariablePath = "/fake_classname_test"
        let localVariableURLString = PetstoreClientAPI.basePath + localVariablePath

        guard let localVariableApiClient = Configuration.apiClient else {
            fatalError("Configuration.apiClient is not set.")
        }

        return localVariableApiClient.send(.PATCH, headers: headers, to: URI(string: localVariableURLString)) { localVariableRequest in
            try Configuration.apiWrapper(&localVariableRequest)
            
            
            try localVariableRequest.content.encode(body, using: Configuration.contentConfiguration.requireEncoder(for: Client.defaultContentType))
            
            try beforeSend(&localVariableRequest)
        }
    }

    public enum TestClassname {
        case http200(value: Client, raw: ClientResponse)
        case http0(raw: ClientResponse)
    }

    /**
     To test class name in snake case
     PATCH /fake_classname_test
     To test class name in snake case
     - API Key:
       - type: apiKey api_key_query (QUERY)
       - name: api_key_query
     - parameter body: (body) client model 
     - returns: `EventLoopFuture` of `TestClassname` 
     */
    open class func testClassname(body: Client, headers: HTTPHeaders = PetstoreClientAPI.customHeaders, beforeSend: (inout ClientRequest) throws -> () = { _ in }) -> EventLoopFuture<TestClassname> {
        return testClassnameRaw(body: body, headers: headers, beforeSend: beforeSend).flatMapThrowing { response -> TestClassname in
            switch response.status.code {
            case 200:
                return .http200(value: try response.content.decode(Client.self, using: Configuration.contentConfiguration.requireDecoder(for: Client.defaultContentType)), raw: response)
            default:
                return .http0(raw: response)
            }
        }
    }
}
