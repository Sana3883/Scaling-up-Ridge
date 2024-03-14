!/bin/sh
set -e
set -u

singularity exec $1 dask-scheduler --scheduler-file dask-scheduler.json --host $(hostname)

