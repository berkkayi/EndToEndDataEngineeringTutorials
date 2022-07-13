
CREATE TABLE "taxi_trip.green_taxi_trip" (
	"VendorID" BIGINT, 
	lpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, 
	lpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, 
	store_and_fwd_flag TEXT, 
	"RatecodeID" FLOAT(53), 
	"PULocationID" BIGINT, 
	"DOLocationID" BIGINT, 
	passenger_count FLOAT(53), 
	trip_distance FLOAT(53), 
	fare_amount FLOAT(53), 
	extra FLOAT(53), 
	mta_tax FLOAT(53), 
	tip_amount FLOAT(53), 
	tolls_amount FLOAT(53), 
	ehail_fee TEXT, 
	improvement_surcharge FLOAT(53), 
	total_amount FLOAT(53), 
	payment_type FLOAT(53), 
	trip_type FLOAT(53), 
	congestion_surcharge FLOAT(53)
)

