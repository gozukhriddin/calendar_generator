

class CalendarGenerator:

    def is_leap_year(self,year=1):
        return (year%4==0 and year%100!=0) or year%400==0

    def get_days_in_month(self,month=1, year=1) -> int:
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4,6,9,11]:
            return 30
        elif month==2:
            return 29 if self.is_leap_year(year) else 28
        else: return 0

    def get_start_day_of_month(self, month=1, year=1):
        total_days =366*year
        total_days=total_days-total_days//4+total_days//100+total_days//400
        for m in range(1, month):
            total_days += self.get_days_in_month(m, year)
        return (total_days + 1) % 7

    def build_grid_string(self, start_day_index=0,total=0):
        grid=''
        grid+='Su Mo Tu We Th Fr Sa\n'
        for i in range(1,total+1):
            weekday_index = (start_day_index + i - 1) % 7
            if i==1:
                grid+='   '*start_day_index
            if weekday_index==0 and i!=1:
                grid+='\n'
            if i<10:
                grid+=' '+str(i)+' '
            else:
                grid+=str(i)+' '
        return grid
    
    def generate_calendar(self, month=1, year=1) -> str:
        return self.build_grid_string(
            self.get_start_day_of_month(month, year),
            self.get_days_in_month(month, year)
        )

if __name__ == "__main__":
    cg = CalendarGenerator()
    print(cg.generate_calendar(2,2025))


        




