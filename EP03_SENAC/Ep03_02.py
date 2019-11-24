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
        if(tpep_pickup_datetime != 'tpep_pickup_datetime' and tpep_dropoff_datetime != 'tpep_dropoff_datetime'):
           # print(tpep_pickup_datetime)
             str_date = tpep_pickup_datetime
             str_fini = tpep_dropoff_datetime
             ini = datetime.strptime(str_date,'%d/%m/%y %H:%M')
             fim = datetime.strptime(str_fini,'%d/%m/%y %H:%M')
             minutes_diff = (fim - ini).total_seconds() / 60.0
             print(minutes_diff)
             yield ini.day, int(minutes_diff)

    def reducer(self, key, values):
        count = 0
        _sum = 0

        for value in values:
            count += 1
            _sum += int(value)

        avg = _sum/count    
        yield key, avg
             
            
if __name__ == '__main__':
    WordCount.run()

   