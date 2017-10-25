import aetros.backend
import math
import time

job = aetros.backend.context()

kpi = job.create_channel('kpi', kpi=True, main=True, max_optimization=False)
kpi.send(1, 1)
job.progress(1,3)
print('kpi 1')

time.sleep(5)
kpi.send(2, math.sin(job.get_parameter('x')))
job.progress(2, 3)

print('kpi ' + str(math.sin(job.get_parameter('x'))))
time.sleep(5)
job.progress(3, 3)

print('done')
job.done()
