Feature: Nexus Infinity Core Application
  As a user of the Nexus Infinity Core Application
  I want to ensure that the application works as expected
  So that I can rely on its functionality

Scenario: Successful Application Startup
  Given the application is started
  When the application is initialized
  Then the application should be running successfully

Scenario: Data Retrieval and Storage
  Given the application is running
  When I retrieve data from the data repository
  Then the data should be retrieved successfully
  When I store data in the data repository
  Then the data should be stored successfully

Scenario: Security Authentication and Authorization
  Given the application is running
  When I attempt to authenticate with valid credentials
  Then I should be authenticated successfully
  When I attempt to access a secured resource
  Then I should be authorized to access the resource
