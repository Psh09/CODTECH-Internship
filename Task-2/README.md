# Task-2: Test RESTful APIs using Postman  

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: Prajwal Shivputra Halle  

**INTERN ID**: CT08HLI  

**DOMAIN**: Software Testing  

**BATCH DURATION**: January 9th, 2025 to February 9th, 2025  

**MENTOR NAME**: Neela Santhosh Kumar  

---

## Internship Task Overview
This task involves testing RESTful APIs for functionalities like authentication and data retrieval using **Postman**. The objective is to test various endpoints of a sample API, ensuring they handle valid and invalid requests correctly, and check how they manage errors and data retrieval.

---

## Task Requirements

### API to Test:
- **ReqRes API**: A public API for testing various operations such as login, user creation, data retrieval, and error handling.

### Functionalities to Test:
1. **Authentication Testing**: Test the login functionality with valid and invalid credentials.
2. **Data Retrieval Testing**: Test retrieving data from the API with valid and invalid parameters.
3. **Create User Testing**: Simulate the creation of new user data.
4. **Update User Testing**: Test updating user data through the API.
5. **Delete User Testing**: Test deleting a user via the API.
6. **Error Testing**: Simulate various error conditions and verify how the API responds.

---

## Deliverables:
- **Postman Collection**: A collection of API tests for all the endpoints.
- **Test Documentation**: Detailed documentation of each test case, including requests, expected responses, and actual results.
- **Test Execution Report**: A report summarizing the test results, including passed and failed tests.

---

## Setup Instructions

### Requirements:
- **Postman**: A platform for testing APIs.
- **Internet Access**: To make requests to the API.

### Steps to Run the Tests:

1. Install **Postman** from [here](https://www.postman.com/downloads/).
2. Import the provided **Postman collection**.
3. Set up the tests by configuring the request parameters and bodies as per the specifications for each test case.
4. Run the collection to perform the tests.
5. Review the results in **Postman** or export the results for documentation.

---

## Test Steps in the Postman Collection

1. **Authentication Testing**:
   - Test the login endpoint using both valid and invalid credentials to verify authentication behavior.
   
2. **Data Retrieval**:
   - Retrieve a list of users or specific user data using GET requests.
   
3. **Invalid Data Retrieval**:
   - Simulate an invalid request (e.g., requesting a non-existent page) and verify the response is as expected.

4. **Create User**:
   - Use the POST method to create a new user and verify if the API correctly stores and returns the new user data.

5. **Update User**:
   - Update the data for an existing user via PUT and verify if the change is successful.

6. **Delete User**:
   - Use the DELETE method to remove a user and verify the API responds appropriately.

7. **Error Testing**:
   - Simulate scenarios where the API should return an error (e.g., invalid ID, incorrect endpoint) and confirm that the error is handled correctly.

---

## Test Execution Report

The results of each test are recorded, detailing the request made, the response received, and whether the test passed or failed.

- **Authentication Test**: 
   - Status: Success
   - Response: `200 OK`
- **Data Retrieval Test (Valid)**:
   - Status: Success
   - Response: List of users with details.
- **Data Retrieval Test (Invalid)**:
   - Status: Success
   - Response: Empty data array with support message.
- **Create User Test**:
   - Status: Success
   - Response: `201 Created` with user details.
- **Update User Test**:
   - Status: Success
   - Response: `200 OK` with updated details.
- **Delete User Test**:
   - Status: Success
   - Response: `204 No Content`
- **Error Testing**:
   - Status: Success
   - Response: `404 Not Found`

---

## Conclusion

This task helped in mastering the process of testing RESTful APIs using Postman. By simulating login, data retrieval, creation, update, deletion, and error scenarios, it provides an overall understanding of how to ensure that APIs function correctly under various conditions.

---

## Additional Resources

- [ReqRes API Documentation](https://reqres.in/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [Postman Collection for ReqRes API](https://github.com/reqres/reqres-in)

---
