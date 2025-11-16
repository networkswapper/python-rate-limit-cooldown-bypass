# These are not codes, they are functions that can help you.
# These are not codes, they are functions that can help you.

can_run = (lambda last, cd, now: now-last>=cd)

tick = lambda: int(__import__("time").time()*1000)

qpc = lambda: __import__("time").perf_counter()

rate_ok = lambda calls, limit, interval, now: (calls:= [t for t in calls if now-t<interval]) or len(calls)<limit

sleep = lambda s: __import__("time").sleep(s)
