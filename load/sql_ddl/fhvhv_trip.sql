
CREATE TABLE "taxi_trip.fhvhv_trip" (
	hvfhs_license_num TEXT, 
	dispatching_base_num TEXT, 
	originating_base_num TEXT, 
	request_datetime TIMESTAMP WITHOUT TIME ZONE, 
	on_scene_datetime TIMESTAMP WITHOUT TIME ZONE, 
	pickup_datetime TIMESTAMP WITHOUT TIME ZONE, 
	dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, 
	"PULocationID" BIGINT, 
	"DOLocationID" BIGINT, 
	trip_miles FLOAT(53), 
	trip_time BIGINT, 
	base_passenger_fare FLOAT(53), 
	tolls FLOAT(53), 
	bcf FLOAT(53), 
	sales_tax FLOAT(53), 
	congestion_surcharge FLOAT(53), 
	airport_fee FLOAT(53), 
	tips FLOAT(53), 
	driver_pay FLOAT(53), 
	shared_request_flag TEXT, 
	shared_match_flag TEXT, 
	access_a_ride_flag TEXT, 
	wav_request_flag TEXT, 
	wav_match_flag TEXT
)

