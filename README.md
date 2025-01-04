# Task 1: Automate Web Application Testing using Selenium WebDriver

## Internship Task Overview

This task involves automating the testing of a sample web application's login and navigation functionality using **Selenium WebDriver**.

The objective is to simulate user actions on the web application, including logging in, navigating through pages, and verifying certain functionality, ensuring that the application performs as expected.

### Task Requirements
1. **Web Application URL**: The task is based on a sample web application (e.g., "SauceDemo").
2. **Functionality to Test**:
   - Automate the login functionality.
   - Test the navigation functionality between pages (e.g., clicking on various elements, adding products to the cart, checking out).
3. **Selenium WebDriver**: The automation will be performed using Selenium WebDriver in Python.
4. **Deliverables**:
   - A **test automation script** that performs the login and navigation tests.
   - A **test execution report** that logs the results of the automation process.

## Setup Instructions

### Requirements

- **Python 3.x** (recommended version 3.11)
- **Selenium WebDriver**
- **ChromeDriver** (if using Google Chrome)

### Steps to Run the Script

1. Install the required Python packages:

    ```bash
    pip install selenium
    ```

2. Download **ChromeDriver** from:  
   [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/)

3. Place the **ChromeDriver** executable in your system path or in the same directory as the Python script.

4. Clone the repository (or copy the script) into your working directory.

5. Run the script:

    ```bash
    python saucedemo_test.py
    ```

### Test Automation Steps in the Script

1. **Launch Browser**: Open Chrome and navigate to the sample web application URL.
2. **Login Test**: Automate the login functionality by providing credentials and verifying successful login.
3. **Navigation Test**: Automate the navigation by adding products to the cart and proceeding to checkout.
4. **Error Handling**: Handle any potential errors (e.g., login failure, missing elements) and log the results.
5. **Logout**: Perform the logout action to ensure user can sign out correctly.

## Test Execution Report

The test execution results will be logged in an **HTML report**. This will contain detailed steps, any issues encountered, and whether each test step passed or failed.

### Sample Report Content
- **Login Test**: Success
- **Navigation Test**: Success
- **Logout**: Success

## Deliverables

1. **Test Automation Script** (`saucedemo_test.py`): A Python script using Selenium WebDriver.
2. **Test Execution Report**: An HTML file containing the results of the test execution.

## Conclusion

This task demonstrates the ability to automate web application testing using Selenium WebDriver, ensuring that basic functionalities such as login and navigation are tested properly.

## Additional Resources

- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)
- [Python Selenium Tutorial](https://selenium-python.readthedocs.io/)
