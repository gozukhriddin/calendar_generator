

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
        total_days =365*year
        total_days+=year//4-year//100+year//400
        
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


    def generate_calendar_year(self,year=1):
        calendar=str(year).center(68,' ')+'\n'
        month=['January','February','March','April','May','June','July','August','September','October','November','December']
        k=0
        for i in range(4):
            calendar+=month[k].center(20,' ')+'\t'+month[k+1].center(20,' ')+'\t'+month[k+2].center(20,' ')+'\n'
            calendar+='Su Mo Tu We Th Fr Sa\tSu Mo Tu We Th Fr Sa\tSu Mo Tu We Th Fr Sa\n'
            
            week_start_day={0:1,1:1,2:1}
            last_day=[self.get_days_in_month(k+1),self.get_days_in_month(k+2),self.get_days_in_month(k+3)]
            
            for month_day in range(1,7,1):
                if last_day[0]<week_start_day[0] and last_day[1]<week_start_day[1] and last_day[2]<week_start_day[2]:
                    calendar+='\n'
                    break
                else:
                    for l in range(3):
                        if last_day[l]<week_start_day[l]:
                            calendar+=' '*20+'\t'
                            continue

                        day=week_start_day[l]
                        
                        weekDay=0
                        while weekDay<7:
                       
                            if day==1:
                                week_start=self.get_start_day_of_month(month=k+1+l,year=year)-1
                                calendar+='   '*week_start
                                weekDay+=week_start

                            if weekDay==6:
                                if day<=last_day[l]:
                                    calendar+=f'{day:2d}'
                                else:
                                    calendar+='  '
                                
                            elif day<=last_day[l]:
                                calendar+=f'{day:2d} '
                            
                            else:
                                calendar+='   '
                            day+=1
                            weekDay+=1

                        week_start_day[l]=day
                        calendar+='\t'
                    calendar+='\n'
            k+=3
        return calendar
if __name__ == "__main__":
    cg = CalendarGenerator()
    print(cg.generate_calendar_year(2026))


        




