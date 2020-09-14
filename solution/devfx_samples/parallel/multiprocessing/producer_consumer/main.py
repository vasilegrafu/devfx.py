import devfx.core as core
import devfx.diagnostics as dgn
import devfx.parallel.processing as parallel

from devfx_samples.parallel.multiprocessing.producer_consumer.producer import Producer
from devfx_samples.parallel.multiprocessing.producer_consumer.consumer import Consumer

def main():
    sw = dgn.stopwatch().start()

    producer = Producer()
    consumer1 = Consumer(1)
    consumer2 = Consumer(2)

    queue = parallel.Queue()

    producer_process = parallel.Process().target(producer.run, queue)
    consumer1_process = parallel.Process().target(consumer1.run, queue)
    consumer2_process = parallel.Process().target(consumer2.run, queue)
    
    producer_process.start()  
    consumer1_process.start()
    consumer2_process.start()

    producer_process.join()
    consumer1_process.join()
    consumer2_process.join()

    if(producer_process.result.is_exception()):
        print(producer_process.result.value)

    if(consumer1_process.result.is_exception()):
        print(consumer1_process.result.value)

    if(consumer2_process.result.is_exception()):
        print(consumer2_process.result.value)

    print("time elapsed: ", sw.stop().elapsed)

if(__name__ == '__main__'):
    main()

