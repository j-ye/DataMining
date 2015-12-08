"""
import holidays

class nyse_holidays(holidays.HolidayBase):
"""
import calendar
from datetime import datetime
from datetime import date

class nyse_holiday(object):
    def __init__(self, year):
        self.yr = year

    def new_year(self):
        return date( self.yr, 1, 1)

    def MLK(self): # the third monday of jan
        c = calendar.monthcalendar( self.yr, 1) #look at jan calendar
        first_week = c[ 0]
        second_week = c[ 1]
        third_week = c[ 2]
        forth_week = c[ 3]
        # if there is a Monday in the first week, the third Monday is
        # in the third week. If the first Monday is in the second week
        # the third Monday is in the forth week.
        if first_week[calendar.MONDAY]:
            MLK_day = third_week[calendar.MONDAY]
        else:
            MLK_day = forth_week[calendar.MONDAY]
        return date( self.yr, 1, MLK_day)

    def presidents_day(self):
        c = calendar.monthcalendar( self.yr, 2) # look at feb calendar
        first_week = c[ 0]
        second_week = c[ 1]
        third_week = c[ 2]
        forth_week = c[ 3]
        # if there is a Monday in the first week, the third Monday is
        # in the third week. If the first Monday is in the second week
        # the third Monday is in the forth week.
        if first_week[calendar.MONDAY]:
            p_day = third_week[calendar.MONDAY]
        else:
            p_day = forth_week[calendar.MONDAY]
        return date( self.yr, 2, p_day)

    # good friday
    # memorial day
    def memorial_day(self): # last friday of may
        c = calendar.monthcalendar( self.yr, 5)
        last_week = c[- 1]
        second_last_week = c[- 2]
        # if last week has a monday, then that's memroial day
        # if not, the monday in second to last week is memorial
        if last_week[calendar.MONDAY]:
            m_day = last_week[calendar.MONDAY]
        else:
            m_day = second_last_week[calendar.MONDAY]
        return date( self.yr, 5, m_day)

    def independence_day(self):
        ind_day = date( self.yr, 7, 4) # fall on sat
        if ind_day.weekday() == 5:
            return date( self.yr, 7, 3)
        if ind_day.weekday() == 6: # fall on sunday
            return date( self.yr, 7, 5)
            pass
        return ind_day

    def labor_day(self): # first monday of sept
        c = calendar.monthcalendar( self.yr, 9)
        first_week = c[ 0]
        second_week = c[ 1]
        if first_week[calendar.MONDAY]:
            l_day = first_week[calendar.MONDAY]
        else:
            l_day = second_week[calendar.MONDAY]
        return date( self.yr, 9, l_day)

    def thanksgiving(self): # forth thursday of nov
        c = calendar.monthcalendar( self.yr, 11)
        first_week = c[ 0]
        if first_week[calendar.THURSDAY]: #if there is a thursday in the first wk
            p_day = c[ 3][calendar.THURSDAY]
        else:
            p_day = c[ 4][calendar.THURSDAY]
        return date( self.yr, 11, p_day)

    def christmas(self):
        xmas_day = date( self.yr, 12, 25)
        if xmas_day.weekday() == 6: # if fall on sunday , mon is holiday
            return date( self.yr, 12, 26)
        if xmas_day.weekday() == 5: # if fall on sat, fri is holiday (2015 indep day)
            return date( self.yr, 12, 24)
        return xmas_day

    def good_friday(self):
        # http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/
        # some algo that calculates easter, modified for good friday
        a = self.yr % 19
        b = self.yr // 100
        c = self.yr % 100
        d = ( 19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = ( 32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 - 1
        return date( self.yr, month, day)

def main():
    holiday_obj = nyse_holiday( 2015)
    print holiday_obj.new_year()
    print holiday_obj.MLK()
    print holiday_obj.presidents_day()
    print holiday_obj.memorial_day()
    print holiday_obj.independence_day()
    print holiday_obj.labor_day()
    print holiday_obj.thanksgiving()
    print holiday_obj.christmas()
    print holiday_obj.good_friday()
if __name__ == '__main__':
    main()