import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11702324")

API_HASH = os.environ.get("API_HASH", "2e836e9f9cd82a0c1d8627f2e70da7f8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5979241264:AAFOnNVm2ht0zJpWVxf500gq4hw2aJZxSLQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001861252300") 

DB_NAME = os.environ.get("DB_NAME","Ghmn")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://mahmoudelwaseaf:1020304050m@ghmn.gghxo6y.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1433077364').split()]

PORT = os.environ.get("PORT", "8080")
