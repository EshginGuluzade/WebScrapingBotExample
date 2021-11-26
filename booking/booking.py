from selenium import webdriver
from booking.booking_filter import BookingFilter


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        # self.driver = webdriver.Chrome()
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com/")

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        self.execute_script("arguments[0].click();", first_result)

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        self.execute_script("arguments[0].click();", check_in_element)

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        self.execute_script("arguments[0].click();", check_out_element)

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        self.execute_script("arguments[0].click();", selection_element)

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            self.execute_script("arguments[0].click();", decrease_adults_element)
            adults_value_element = self.find_element_by_id('group_adults')
            adult_value = adults_value_element.get_attribute('value')
            if int(adult_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count-1):
            self.execute_script("arguments[0].click();", increase_button_element)

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        self.execute_script("arguments[0].click();", search_button)

    def apply_filter(self):
        filter = BookingFilter(driver=self)
        filter.apply_start_rating(3)
        filter.sort_price_lowest_first()


