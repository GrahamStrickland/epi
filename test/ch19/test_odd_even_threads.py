#!/usr/bin/env python3


from odd_even_threads import *


monitor = OddEvenMonitor()
odd_thread = OddThread(monitor)
even_thread = EvenThread(monitor)


odd_thread.run()
even_thread.run()
