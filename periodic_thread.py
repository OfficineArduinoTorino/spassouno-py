import logging
from threading import Thread
import threading
import traceback
import time

class PeriodicThread(object):

    def __init__(self, callback=None, period=1,  *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.callback = callback
        self.period = period
        self.stop = True
        self.worker = None
        self.schedule_lock = threading.Lock()
        self.worker = Thread(target=self._run, args=())
        self.worker.setDaemon(True)

    def start(self):
        if self.worker:
            self.worker.start()
            self.stop = False
        return not self.stop

    def run(self):
        if self.callback is not None:
            self.callback()

    def _run(self):
        print "_run {0}".format(self.stop)
        while not self.stop:
            try:
                self.run()
                time.sleep(self.period)
            except Exception, e:
                logging.error(traceback.format_exc())

    def change_period(self, period):
        with self.schedule_lock:
            self.period = period

    def cancel(self):
        with self.schedule_lock:
            self.stop = True
            if self.worker is not None:
                while self.worker.is_alive():
                    pass
                self.worker = Thread(target=self._run, args=())


if __name__ == '__main__':
    import time

    def cb():
        print "CB"

    p = PeriodicThread(callback=cb, period=0.3, name="t")
    p.start()
    time.sleep(3)
    print "change"
    p.change_period(1)
    time.sleep(7)

