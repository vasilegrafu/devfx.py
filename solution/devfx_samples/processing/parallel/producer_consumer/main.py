import devfx.core as core
import devfx.diagnostics as dgn
import devfx.processing as processing

from devfx_samples.processing.parallel.producer_consumer.producer import Producer
from devfx_samples.processing.parallel.producer_consumer.consumer import Consumer

def main():
    sw = dgn.stopwatch().start()

    producer1 = Producer(id=1)
    producer2 = Producer(id=2)
    consumer = Consumer()

    queue = processing.parallel.Queue()

    producer_processes = processing.parallel.Processes([processing.parallel.Process(fn=fn, args=(queue,)) for fn in (producer1.run, producer2.run)])
    consumer_process = processing.parallel.Process(fn=consumer.run, args=(queue,))
    
    producer_processes.start()  
    consumer_process.start()

    producer_processes.wait()
    consumer_process.wait()

    print(producer_processes.results)
    print(consumer_process.result)

    print("time elapsed: ", sw.stop().elapsed)

if(__name__ == '__main__'):
    main()

