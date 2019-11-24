from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime, timedelta



class WordCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        (VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge)=line.split(',')
        if(tpep_pickup_datetime != 'tpep_pickup_datetime' and tpep_dropoff_datetime != 'tpep_dropoff_datetime' and len(tpep_dropoff_datetime)=+ 18 and len(tpep_pickup_datetime) =+ 18:
             str_date = tpep_pickup_datetime
             str_fini = tpep_dropoff_datetime
             ini = datetime.strptime(str_date,'%d/%m/%y %H:%M')
             fim = datetime.strptime(str_fini,'%d/%m/%y %H:%M')
             minutes_diff = (fim - ini).total_seconds() / 60.0
             media = (float(total_amount)/int(minutes_diff))*15
             yield ini.day, media

    def reducer(self, key, values):   
        yield key, sum(values)
             
            
if __name__ == '__main__':
    WordCount.run()

   