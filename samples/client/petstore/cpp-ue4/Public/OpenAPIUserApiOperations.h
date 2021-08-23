/**
 * OpenAPI Petstore
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator
 * https://github.com/OpenAPITools/openapi-generator
 * Do not edit the class manually.
 */

#pragma once

#include "OpenAPIBaseModel.h"
#include "OpenAPIUserApi.h"

#include "OpenAPIUser.h"

namespace OpenAPI
{

/* Create user
 *
 * This can only be done by the logged in user.
*/
class OPENAPI_API OpenAPIUserApi::CreateUserRequest : public Request
{
public:
    virtual ~CreateUserRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* Created user object */
	OpenAPIUser Body;
};

class OPENAPI_API OpenAPIUserApi::CreateUserResponse : public Response
{
public:
    virtual ~CreateUserResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

/* Creates list of users with given input array

*/
class OPENAPI_API OpenAPIUserApi::CreateUsersWithArrayInputRequest : public Request
{
public:
    virtual ~CreateUsersWithArrayInputRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* List of user object */
	TArray<OpenAPIUser> Body;
};

class OPENAPI_API OpenAPIUserApi::CreateUsersWithArrayInputResponse : public Response
{
public:
    virtual ~CreateUsersWithArrayInputResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

/* Creates list of users with given input array

*/
class OPENAPI_API OpenAPIUserApi::CreateUsersWithListInputRequest : public Request
{
public:
    virtual ~CreateUsersWithListInputRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* List of user object */
	TArray<OpenAPIUser> Body;
};

class OPENAPI_API OpenAPIUserApi::CreateUsersWithListInputResponse : public Response
{
public:
    virtual ~CreateUsersWithListInputResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

/* Delete user
 *
 * This can only be done by the logged in user.
*/
class OPENAPI_API OpenAPIUserApi::DeleteUserRequest : public Request
{
public:
    virtual ~DeleteUserRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* The name that needs to be deleted */
	FString Username;
};

class OPENAPI_API OpenAPIUserApi::DeleteUserResponse : public Response
{
public:
    virtual ~DeleteUserResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

/* Get user by user name

*/
class OPENAPI_API OpenAPIUserApi::GetUserByNameRequest : public Request
{
public:
    virtual ~GetUserByNameRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* The name that needs to be fetched. Use user1 for testing. */
	FString Username;
};

class OPENAPI_API OpenAPIUserApi::GetUserByNameResponse : public Response
{
public:
    virtual ~GetUserByNameResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    OpenAPIUser Content;
};

/* Logs user into the system

*/
class OPENAPI_API OpenAPIUserApi::LoginUserRequest : public Request
{
public:
    virtual ~LoginUserRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* The user name for login */
	FString Username;
	/* The password for login in clear text */
	FString Password;
};

class OPENAPI_API OpenAPIUserApi::LoginUserResponse : public Response
{
public:
    virtual ~LoginUserResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    FString Content;
};

/* Logs out current logged in user session

*/
class OPENAPI_API OpenAPIUserApi::LogoutUserRequest : public Request
{
public:
    virtual ~LogoutUserRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

};

class OPENAPI_API OpenAPIUserApi::LogoutUserResponse : public Response
{
public:
    virtual ~LogoutUserResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

/* Updated user
 *
 * This can only be done by the logged in user.
*/
class OPENAPI_API OpenAPIUserApi::UpdateUserRequest : public Request
{
public:
    virtual ~UpdateUserRequest() {}
	void SetupHttpRequest(const FHttpRequestRef& HttpRequest) const final;
	FString ComputePath() const final;

	/* name that need to be deleted */
	FString Username;
	/* Updated user object */
	OpenAPIUser Body;
};

class OPENAPI_API OpenAPIUserApi::UpdateUserResponse : public Response
{
public:
    virtual ~UpdateUserResponse() {}
	void SetHttpResponseCode(EHttpResponseCodes::Type InHttpResponseCode) final;
	bool FromJson(const TSharedPtr<FJsonValue>& JsonValue) final;

    
};

}
