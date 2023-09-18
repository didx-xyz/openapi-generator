=begin
#OpenAPI Petstore

#This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

The version of the OpenAPI document: 1.0.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 7.0.0-SNAPSHOT

=end

require 'spec_helper'

describe Petstore::Configuration do
  let(:config) { Petstore::Configuration.new }

  before(:each) do
    # uncomment below to setup host and base_path
    # require 'URI'
    # uri = URI.parse("http://petstore.swagger.io:80/v2")
    # Petstore.configure do |c|
    #   c.host = uri.host
    #   c.base_path = uri.path
    # end
  end

  describe '#base_url' do
    it 'should have the default value' do
      expect(config.base_url).to eq("http://petstore.swagger.io/v2")
    end

    it 'returns default value when invalid operation is passed' do
      expect(config.base_url('invalid_operation')).to eq('http://petstore.swagger.io/v2')
    end

    it 'returns proper URL default server_index' do
      expect(config.base_url(:'PetApi.add_pet')).to eq('http://petstore.swagger.io/v2')
    end

    it 'returns proper URL when server_index is set' do
      config.server_index = 1
      expect(config.base_url(:'PetApi.add_pet')).to eq('http://path-server-test.petstore.local/v2')
    end

    it 'returns proper URL when server_operation_index is set' do
      config.server_operation_index = {
        :'PetApi.add_pet' => 1
      }
      expect(config.base_url(:'PetApi.add_pet')).to eq('http://path-server-test.petstore.local/v2')
    end

    it 'returns proper URL from server_settings when server_index is set' do
      config.server_index = 1
      expect(config.base_url).to eq('https://localhost:8080/v2')
    end

    it 'throws argument error when attempting to use a server index that is out of bounds' do
      config.server_operation_index = {
        :'PetApi.add_pet' => 10
      }
      expect {
        config.base_url(:'PetApi.add_pet')
      }.to raise_error(ArgumentError, 'Invalid index 10 when selecting the server. Must not be nil and must be less than 3')
    end

    it 'should remove trailing slashes' do
      [nil, '', '/', '//'].each do |base_path|
        config.base_path = base_path
        # uncomment below to test trailing slashes
        # expect(config.base_url).to eq("http://petstore.swagger.io:80/v2")
      end
    end
  end
end
