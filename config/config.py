
import os


class Configs:
    SCREENSHOTS_PATH = os.path.join('screenshots')
    LOGFILE_PATH = os.path.abspath("logs")
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    API_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php"
    EXCEL_PATH = os.path.abspath("test_data/test_data.xlsx")  # Excel file path for data-driven testing
    EMPLOYMENT_STATUS_GETURL = f"{API_ENDPOINT}/api/v2/admin/employment-statuses/1"
    EMPLOYMENT_STATUS_POSTURL = f"{API_ENDPOINT}/api/v2/admin/employment-statuses"
    HEADERS = {
        "Authorization": f"Bearer def502001f64fdfdc63165f8f62269dba1e133d0727e6ef8c84b9ce32ca18ee0a9f05f7f63f3704af82ed481dcf76956ea382fabf8b66a5668e94d190071d6d1d2e1eed28ac86645eb6d4b0900efcf6e5da9e9dfd87527a2b2da77019089b3be8a2cc8a8f9ff073f8a64933cc54967ce440462c01142766f071771d19fcd37015cb6de198df5be6ed000fd6ef1408f32641769d8746d3539cd52c8b53c3ea442fafafce0",
        "Content-Type": "application/json"
    }
    NEW_EMPLOYMENT_STATUS = {"name": "Test123"}
    EMPLOYMENT_STATUS_LIST = ['AutoStatus', 'Freelance', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Probation', 'Part-Time Contract', 'Part-Time Internship', 'Test']
