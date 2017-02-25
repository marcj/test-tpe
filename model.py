import aetros.backend
import math
import time

job = aetros.backend.start_job('marcj/test-tpe')

kpi = job.create_channel('kpi', kpi=True, main=True, max_optimization=False)
kpi.send(1, 1)
print('kpi 1')
time.sleep(2)
kpi.send(2, math.sin(job.get_parameter('x')))
print('kpi ' + str(math.sin(job.get_parameter('x'))))
time.sleep(2)

print('done')
job.done()
