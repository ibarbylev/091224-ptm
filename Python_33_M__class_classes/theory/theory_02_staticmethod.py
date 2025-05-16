class MyTimer:
    @staticmethod
    def get_current_year():
        from datetime import datetime
        """Print current year"""
        print(f"current year: {datetime.now().year}")


MyTimer.get_current_year()  # Static method
