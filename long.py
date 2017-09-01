import aetros.backend
import math
import time

job = aetros.backend.start_job('marcj/test:tpe')
kpi = job.create_channel('kpi', kpi=True, main=True, max_optimization=False)

for i in range(1, 2000):
	kpi.send(i, i*233/4*time.time())
	job.progress(i, 1000)
	time.sleep(2)

print('done')
job.done()
