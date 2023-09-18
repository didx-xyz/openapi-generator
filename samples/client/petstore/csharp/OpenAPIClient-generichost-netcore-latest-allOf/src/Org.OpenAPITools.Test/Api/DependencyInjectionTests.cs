/*
 * Example
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using System.Collections.Generic;
using System.Security.Cryptography;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Extensions;
using Xunit;

namespace Org.OpenAPITools.Test.Api
{
    /// <summary>
    ///  Tests the dependency injection.
    /// </summary>
    public class DependencyInjectionTest
    {
        private readonly IHost _hostUsingConfigureWithoutAClient = 
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureApi((context, services, options) =>
            {
                
            })
            .Build();

        private readonly IHost _hostUsingConfigureWithAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureApi((context, services, options) =>
            {
                
                options.AddApiHttpClients(client => client.BaseAddress = new Uri(ClientUtils.BASE_ADDRESS));
            })
            .Build();

        private readonly IHost _hostUsingAddWithoutAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureServices((host, services) =>
            {
                services.AddApi(options =>
                {
                    
                });
            })
            .Build();

        private readonly IHost _hostUsingAddWithAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureServices((host, services) =>
            {
                services.AddApi(options =>
                {
                    
                    options.AddApiHttpClients(client => client.BaseAddress = new Uri(ClientUtils.BASE_ADDRESS));
                });
            })
            .Build();

        /// <summary>
        /// Test dependency injection when using the configure method
        /// </summary>
        [Fact]
        public void ConfigureApiWithAClientTest()
        {
            var defaultApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the configure method
        /// </summary>
        [Fact]
        public void ConfigureApiWithoutAClientTest()
        {
            var defaultApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the add method
        /// </summary>
        [Fact]
        public void AddApiWithAClientTest()
        {
            var defaultApi = _hostUsingAddWithAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the add method
        /// </summary>
        [Fact]
        public void AddApiWithoutAClientTest()
        {
            var defaultApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
        }
    }
}
