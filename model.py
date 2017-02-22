import aetros.backend
import math

job = aetros.backend.start_job('marcj/test-tpe')

kpi = job.create_channel('kpi', kpi=True, main=True, max_optimization=False)
kpi.send(1, math.sin(job.get_parameter('x')) + job.get_parameter('y'))

job.done()