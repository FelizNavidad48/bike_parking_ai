import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('bike-parking-ai-51943007dace.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('4WB00 Locations')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)



###
#FIrst value = row
#Second value = column



def add_row(y, x, data):
    sheet_instance.update_cell(y, x, data)


