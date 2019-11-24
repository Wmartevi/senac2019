from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime, timedelta
import json


class WordCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        (VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge)=line.split(',')
        if(tpep_pickup_datetime != 'tpep_pickup_datetime' and total_amount != 'total_amount'):
             str_date = tpep_pickup_datetime
             dates = datetime.strptime(str_date,'%d/%m/%y %H:%M').date()
             yield dates.day, float(total_amount)

    def reducer(self, key, values):
        print(values)
        yield key, sum(values)
            
if __name__ == '__main__':
    WordCount.run()

