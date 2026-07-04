import datetime

class DateHelper:
    @staticmethod
    def get_today_iso():
        return datetime.date.today().isoformat()

    @staticmethod
    def get_today_compact():
        return datetime.date.today().isoformat().replace("-", "")

    @staticmethod
    def format_date_str(date_obj):
        return date_obj.isoformat()
