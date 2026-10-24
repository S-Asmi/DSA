class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        if (leaveAlice[:2] < arriveBob[:2] or
                arriveAlice[:2] > leaveBob[:2]):
            return 0
        start_date = max(arriveAlice, arriveBob)
        end_date = min(leaveAlice, leaveBob)
        if end_date[:2] == start_date[:2]:
            end_day = int(end_date[3:])
            start_day = int(start_date[3:])

            if end_day < start_day:
                return 0
            return end_day - start_day + 1
        start_month = int(start_date[:2])
        end_month = int(end_date[:2])
        start_day = int(start_date[3:])
        end_day = int(end_date[3:])

        total_days = 0
        for month in range(start_month + 1, end_month):
            total_days += days_in_month[month - 1]
        total_days += days_in_month[start_month - 1] - start_day
        total_days += end_day
        return total_days + 1

    
        