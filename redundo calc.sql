BEGIN TRAN

declare @startdate date
declare @enddate date
declare @salary decimal(9,2)

set @startdate ='2017-10-04' --date you started
set @enddate = '2022-10-10'  --date you finished
set @salary =00.00				--salary


Select 
*,
case when Years <2 then 0 else 
convert(decimal(9,2),WeeklyWage * WeeksDue) end as [RedundancyCalcd]
from
(
SELECT 
convert(decimal(14,2),DATEDIFF(dd, @startdate,@enddate)/365.0) as Years,
-- Whole months
        convert(decimal(14,2),DATEDIFF(m, @STARTDATE, @ENDDATE) - 1
        +
        -- Part of the month at beginning  of the period
        (1.0*((DAY(EOMONTH(@STARTDATE))) - DATEPART(DAY, @STARTDATE) + 1)
        / DAY(EOMONTH(@STARTDATE))) -- Number of days in first month
        + 
        -- Part of the month at the end of the period
        (1.0*DATEPART(DAY, @ENDDATE)
        / DAY(EOMONTH(@ENDDATE))))as Months, -- Number of days in last month 
convert(decimal(14,2),FLOOR(DATEDIFF(dd,@startdate,@enddate))/7.00 +
    CASE DATEDIFF(dd,@startdate,@enddate)%7.00 WHEN 0 THEN 0 ELSE 1 END)  as NumWeeks
	,(convert(decimal(14,2),DATEDIFF(dd, @startdate,@enddate)/365.0) *2)+1 as WeeksDue
	,convert(decimal(14,2),case when @salary/52 >600 then 600 else @salary/52 end) as WeeklyWage
) x

ROLLBACK

