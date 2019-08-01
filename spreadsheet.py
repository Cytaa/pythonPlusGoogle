import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


sheet = client.open("Copy of Legislators 2017").sheet1


