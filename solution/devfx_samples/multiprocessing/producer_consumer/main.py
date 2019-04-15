import devfx.multiprocessing as mproc
import devfx.diagnostics as dgn
import devfx.reflection as refl
from devfx_samples.multiprocessing.producer_consumer.producer import Producer
from devfx_samples.multiprocessing.producer_consumer.consumer import Consumer

def main():
    sw = dgn.stopwatch().start()

    producer = Producer()
    consumer = Consumer()

    queue = mproc.Queue()

    producer_process = mproc.Process(target=producer.run, args=(queue, ))
    producer_process.start()

    consumer_process = mproc.Process(target=consumer.run, args=(queue, ))
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    if(producer_process.result.is_exception()):
        print(producer_process.result.value)

    if(consumer_process.result.is_exception()):
        print(consumer_process.result.value)

    print("time elapsed: ", sw.stop().elapsed)

if(__name__ == '__main__'):
    main()

