import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.processing.parallel as pp

"""------------------------------------------------------------------------------------------------
"""
def worker(n, channel_end):
    obj = [0]*1024*1024
    i = 0
    while(True):
        i += 1
        channel_end.send((n, i, obj))       

if __name__ == '__main__':
    channel = pp.Channel()
    process = pp.Processes.create(n=8, fn=lambda i: worker, args=lambda i: ((i+1), channel.end2))
    process.start()

    while(True):
        (n, i, obj) = channel.end1.receive()
        print((n, i, len(obj)))

    channel.close()
    process.join()

