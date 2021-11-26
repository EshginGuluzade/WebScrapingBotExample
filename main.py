from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2021-11-26',
                     check_out_date='2021-11-29')
    bot.select_adults(count=10)
    bot.click_search()
    bot.apply_filter()
