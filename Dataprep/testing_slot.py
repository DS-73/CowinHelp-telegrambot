from cowin_api import CoWinAPI

district_id = '141'
date = '03-05-2021'  # Optional. Takes today's date by default
min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
print(available_centers)