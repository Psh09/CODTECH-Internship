from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Initialize WebDriver
driver = webdriver.Chrome()

results = []

# Helper to retry and time element search
def find_element_with_retry(by, value, retries=3, wait_time=2):
    start_time = time.time()
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))
            driver.execute_script("arguments[0].style.border='3px solid red'", element)  # Highlight
            duration = time.time() - start_time
            return element, round(duration, 2)
        except (NoSuchElementException, TimeoutException):
            time.sleep(wait_time)
    duration = time.time() - start_time
    return None, round(duration, 2)

# Login
def login():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    start_time = time.time()
    time.sleep(2)

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        WebDriverWait(driver, 5).until(EC.url_contains("inventory"))
        duration = round(time.time() - start_time, 2)
        results.append(f"<tr><td>Login</td><td style='color:green;'>Successful</td><td>{duration} s</td></tr>")
    except Exception as e:
        driver.save_screenshot("login_error.png")
        results.append(f"<tr><td>Login</td><td style='color:red;'>Failed</td><td>{duration} s</td></tr>")

# Add Items to Cart
def add_items_to_cart():
    items = ["add-to-cart-sauce-labs-backpack", "add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)"]
    for item in items:
        element, duration = find_element_with_retry(By.ID, item)
        if element:
            element.click()
            time.sleep(2)
            results.append(f"<tr><td>{item}</td><td style='color:green;'>Added to Cart</td><td>{duration} s</td></tr>")
        else:
            driver.save_screenshot(f"{item}_error.png")
            results.append(f"<tr><td>{item}</td><td style='color:red;'>Failed to Add</td><td>{duration} s</td></tr>")

# Proceed to Checkout
def checkout():
    cart, duration = find_element_with_retry(By.CSS_SELECTOR, "#shopping_cart_container > a")
    if cart:
        cart.click()
        time.sleep(2)
        results.append(f"<tr><td>Cart</td><td style='color:green;'>Opened</td><td>{duration} s</td></tr>")
    else:
        results.append(f"<tr><td>Cart</td><td style='color:red;'>Failed</td><td>{duration} s</td></tr>")
        return
    
    checkout_button, duration = find_element_with_retry(By.ID, "checkout")
    if checkout_button:
        checkout_button.click()
        time.sleep(2)
        results.append(f"<tr><td>Checkout</td><td style='color:green;'>Completed</td><td>{duration} s</td></tr>")
    else:
        results.append(f"<tr><td>Checkout</td><td style='color:red;'>Failed</td><td>{duration} s</td></tr>")

# Logout
def logout():
    menu_button, duration = find_element_with_retry(By.ID, "react-burger-menu-btn")
    if menu_button:
        menu_button.click()
        time.sleep(2)
        logout_link, duration = find_element_with_retry(By.ID, "logout_sidebar_link")
        if logout_link:
            logout_link.click()
            time.sleep(2)
            results.append(f"<tr><td>Logout</td><td style='color:green;'>Successful</td><td>{duration} s</td></tr>")
        else:
            results.append(f"<tr><td>Logout</td><td style='color:red;'>Failed</td><td>{duration} s</td></tr>")
    else:
        results.append(f"<tr><td>Menu</td><td style='color:red;'>Failed to Open</td><td>{duration} s</td></tr>")

# Generate HTML Report
def generate_html_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = f"""
    <html>
    <head>
        <title>Test Execution Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #2E86C1; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
            th {{ background-color: #f4f4f4; }}
        </style>
    </head>
    <body>
        <h1>Test Execution Report</h1>
        <p><strong>Date:</strong> {timestamp}</p>
        <table>
            <tr>
                <th>Step</th>
                <th>Status</th>
                <th>Execution Time</th>
            </tr>
            {''.join(results)}
        </table>
    </body>
    </html>
    """
    
    with open("test_report.html", "w") as report_file:
        report_file.write(report_content)
    print("HTML report generated: test_report.html")

# Main Flow
try:
    login()
    add_items_to_cart()
    checkout()
    logout()
finally:
    generate_html_report()
    driver.quit()
