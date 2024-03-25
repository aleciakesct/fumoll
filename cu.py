from selenium.webdriver.common.by import By

def click_Xpath(driver, index, xpath):
    """Clicks the element at the given index using an Xpath.

    Args:
        driver: The WebDriver instance.
        index: The index of the element to click.
        xpath: The Xpath of the element to click.
    """

    elements = driver.find_elements(By.XPATH, xpath)
    if index < len(elements):
        elements[index].click()
    else:
        raise IndexError("Index out of range.")
