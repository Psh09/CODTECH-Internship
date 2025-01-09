
---

## **ReqRes API Test Cases Documentation**

---

### **1. POST: Authentication Testing (Simulated Login)**  

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input                                                   | Expected Output                              | Status Code |
|--------------|------------------------------|---------------------------------------------------------|----------------------------------------------|-------------|
| TC001        | Valid Login                  | `{ "email": "eve.holt@reqres.in", "password": "cityslicka" }` | `{"token": "QpwL5tke4Pnpja7X4"}`             | 200 OK      |
| TC002        | Invalid Login - Missing Password | `{ "email": "eve.holt@reqres.in" }`                    | `{"error": "Missing password"}`              | 400 Bad Request |

---

### **2. GET: Data Retrieval Testing**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input (Query Params) | Expected Output                              | Status Code |
|--------------|------------------------------|-----------------------|----------------------------------------------|-------------|
| TC003        | Valid Page Data              | `page=2`             | Non-empty `data` array                       | 200 OK      |
| TC004        | Invalid Page Number          | `page=999`           | Empty `data` array                           | 200 OK      |

---

### **3. POST: CREATE User**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input                                                   | Expected Output                              | Status Code |
|--------------|------------------------------|---------------------------------------------------------|----------------------------------------------|-------------|
| TC005        | Valid User Creation          | `{ "name": "John Doe", "job": "Software Engineer" }`    | `{"name": "John Doe", "job": "Software Engineer", "id": "123", "createdAt": "..."}` | 201 Created |
| TC006        | Invalid User Creation        | `{}`                                                   | `{"error": "Invalid input"}` (or similar)    | 400 Bad Request |

---

### **4. GET: Retrieve User**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input (Path Params) | Expected Output                              | Status Code |
|--------------|------------------------------|----------------------|----------------------------------------------|-------------|
| TC007        | Retrieve Existing User       | `/users/5`          | User details in the `data` object            | 200 OK      |
| TC008        | Retrieve Non-existing User   | `/users/999`        | `{"error": "User not found"}`                | 404 Not Found |

---

### **5. PUT: Update User**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input                                                   | Expected Output                              | Status Code |
|--------------|------------------------------|---------------------------------------------------------|----------------------------------------------|-------------|
| TC009        | Valid User Update            | `{ "name": "Jane Doe", "job": "Product Manager" }`      | Updated user details                         | 200 OK      |
| TC010        | Invalid User Update          | `{}`                                                   | `{"error": "Invalid input"}` (or similar)    | 400 Bad Request |

---

### **6. DELETE: Delete User**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input (Path Params) | Expected Output                              | Status Code |
|--------------|------------------------------|----------------------|----------------------------------------------|-------------|
| TC011        | Valid User Deletion          | `/users/2`          | No content                                   | 204 No Content |
| TC012        | Delete Non-existing User     | `/users/999`        | `{"error": "User not found"}`                | 404 Not Found |

---

### **7. GET: Testing Error Cases**

#### **Test Cases**  

| Test Case ID | Test Scenario                | Input (Path Params) | Expected Output                              | Status Code |
|--------------|------------------------------|----------------------|----------------------------------------------|-------------|
| TC013        | Invalid User Retrieval       | `/users/999`        | `{"error": "User not found"}`                | 404 Not Found |

---

These test cases ensure that all possible scenarios (valid and invalid) for each API endpoint are covered. You can implement and validate these using Postman by sending requests and verifying the responses against the expected outputs.
