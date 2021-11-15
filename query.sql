select drivername.driver_id, driver_forename, driver_surname, points
	from drivername join results on (Drivername.driver_id = Results.driver_id) 
		where points > 9

select driver_forename, driver_surname, points from Drivername join Results on (Drivername.driver_id = Results.driver_id)

select Drivername.driver_id, points from Drivername join Results on (Drivername.driver_id = Results.driver_id)