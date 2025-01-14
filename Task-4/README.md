# Task-4: Load Testing with Gatling

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: Prajwal Shivputra Halle  

**INTERN ID**: CT08HLI  

**DOMAIN**: Software Testing  

**BATCH DURATION**: January 9th, 2025 to February 9th, 2025  

**MENTOR NAME**: Neela Santhosh Kumar  

---
## Overview
This document provides instructions for performing load testing on a web application using Gatling.

## Prerequisites
- Ensure that [Gatling](https://gatling.io/open-source) is installed on your system.
- Have a running instance of the web application you want to test.

## Gatling Simulation Script
The load test script is located at `Task-4/gatling_load_test.scala`. This script defines the load testing parameters and scenarios.

### Key Components
- **HTTP Protocol**: Configures the base URL and headers.
- **Scenario**: Defines the actions to be performed during the test, such as submitting a form.
- **Load Configuration**: Specifies the number of users and the ramp-up time.

## Running the Load Test
1. Navigate to the Gatling installation directory.
2. Run the following command to execute the load test:
   ```bash
   ./bin/gatling.sh -sf Task-4 -s LoadTestSimulation
   ```
3. Monitor the console output for test progress and results.

## Analyzing Results
After the test completes, Gatling generates a detailed report in the `results` directory. Open the HTML report to analyze performance metrics, including response times and error rates.

## Conclusion
This README provides a basic guide to load testing with Gatling. For more advanced configurations, refer to the [Gatling documentation](https://gatling.io/docs/current/).
