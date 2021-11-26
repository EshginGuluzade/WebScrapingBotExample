from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilter:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_start_rating(self, *start_values):
        start_filter_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        start_child_element = start_filter_box.find_elements_by_css_selector(
            '*'
        )
        for start_value in start_values:
            for start_element in start_child_element:
                if str(start_element.get_attribute('innerHTML')).strip() == f'{start_value} stars':
                    self.driver.execute_script("arguments[0].click();", start_element)

    def sort_price_lowest_first(self):
        lowest_price = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        self.driver.execute_script("arguments[0].click();", lowest_price)



