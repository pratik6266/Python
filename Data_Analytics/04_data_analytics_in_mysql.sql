show databases;
show tables;

/*
set operatin are union and union all 
use use not in for except and in for intersection
*/

select * from salary_data;

create or replace view mine as
select * from salary_data where age > 25;

-- view help use to save work and start from there as a virtual table;
select * from mine;


-- precedure
Delimiter &&
create procedure get_data(in dat int)
begin
	select * from salary_data where age > dat;
end &&
Delimiter ;

drop procedure get_data;

call get_data(21);

Delimiter &&
create procedure get_max(out dat int)
begin
select max(salary) from salary_data;
end &&
Delimiter ;

set @maxi = 0;
call get_max(@maxi);
select @maxi;
set @dataa = 124; -- use this when you have to go with inout varible so this is how you set data before passing it as argument
select @dataa;



Delimiter &&
create procedure just_a_loop()
begin
	declare i int default 1;
    
    simple_loop : loop
		if i > 5 then
			leave simple_loop;
		end if;
        
        select i;
        set i = i + 1;
    end loop;
end &&
Delimiter ;

call just_a_loop();

drop procedure cursor_into;
drop table if exists alphaa;

Delimiter &&
create procedure cursor_into(in dat int)
begin
	declare a float;
    declare b float;
    declare c int;
    declare done int default 0;
	declare c1 cursor for
		select * from salary_data;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	create table alphaa(
		a float,
        b float,
        c int
    );
        
    open c1;
    read_loop: loop
		fetch c1 into a, b, c;
        if done then
			leave read_loop;
		end if;
        insert into alphaa values(a, b, c);
    end loop;
    
    select * from alphaa;
    DROP TEMPORARY TABLE IF EXISTS alphaa;
end;
&& Delimiter ;

call cursor_into(2);
