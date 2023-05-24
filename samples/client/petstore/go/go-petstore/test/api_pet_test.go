/*
OpenAPI Petstore

Testing PetApiService

*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech);

package petstore

import (
    "context"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/require"
    "testing"
    openapiclient "./openapi"
)

func Test_petstore_PetApiService(t *testing.T) {

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)

    t.Run("Test PetApiService AddPet", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        resp, httpRes, err := apiClient.PetApi.AddPet(context.Background()).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService DeletePet", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        var petId int64

        resp, httpRes, err := apiClient.PetApi.DeletePet(context.Background(), petId).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService FindPetsByStatus", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        resp, httpRes, err := apiClient.PetApi.FindPetsByStatus(context.Background()).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService FindPetsByTags", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        resp, httpRes, err := apiClient.PetApi.FindPetsByTags(context.Background()).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService GetPetById", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        var petId int64

        resp, httpRes, err := apiClient.PetApi.GetPetById(context.Background(), petId).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService UpdatePet", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        resp, httpRes, err := apiClient.PetApi.UpdatePet(context.Background()).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService UpdatePetWithForm", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        var petId int64

        resp, httpRes, err := apiClient.PetApi.UpdatePetWithForm(context.Background(), petId).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService UploadFile", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        var petId int64

        resp, httpRes, err := apiClient.PetApi.UploadFile(context.Background(), petId).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

    t.Run("Test PetApiService UploadFileWithRequiredFile", func(t *testing.T) {

        t.Skip("skip test")  // remove to run test

        var petId int64

        resp, httpRes, err := apiClient.PetApi.UploadFileWithRequiredFile(context.Background(), petId).Execute()

        require.Nil(t, err)
        require.NotNil(t, resp)
        assert.Equal(t, 200, httpRes.StatusCode)

    })

}
