/*Analyse data using SQL*/
select Course,Year,
number_of_enrolments as Curr_Yr_Enrolments,
LEAD(number_of_enrolments ,1,0) over (partition by course order by year) 
as Next_Yr_Enrolments,
LAG(number_of_enrolments ,1,0) over (partition by course order by year) 
as Prev_Yr_Enrolments
from
(select count(distinct name)number_of_enrolments,
course,year 
from dbo.Enrolments
group by course,year 
)allrecs order by course,year;

select Course,Country,Number_of_enrolments
from
(select count(*)number_of_enrolments,
course,country 
from dbo.Enrolments
group by course,country 
)allrecs; 


create view dbo.Vw_CourseEnrolmentsByYear
as
(select Course,Year,
number_of_enrolments as Curr_Yr_Enrolments,
LEAD(number_of_enrolments ,1,0) over (partition by course order by year) 
as Next_Yr_Enrolments,
LAG(number_of_enrolments ,1,0) over (partition by course order by year) 
as Prev_Yr_Enrolments
from
(select count(distinct name)number_of_enrolments,
course,year 
from dbo.Enrolments
group by course,year 
)allrecs 
);