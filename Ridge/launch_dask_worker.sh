#!/bin/sh
#SBATCH --nodes=1  # Number of worker nodes
#SBATCH --mem=200G          # Memory per worker node
#SBATCH --cpus-per-task=64   # Number of CPUs per worker
#SBATCH --time=80:00:00     # Wall-clock time limit (adjust as needed)

set -e
set -u

NTHREADS=8

export APPTAINERENV_OMP_NUM_THREADS=${NTHREADS}
export APPTAINERENV_MKL_NUM_THREADS=${NTHREADS}
export APPTAINERENV_OPENBLAS_NUM_THREADS=${NTHREADS}

# Calculate the total memory for each worker (200GB)
MEMORY_PER_WORKER=200e9

srun singularity exec $1 dask-worker --scheduler-file dask-scheduler.json --nthreads 1  --memory-limit $MEMORY_PER_WORKER --resources "MEM=${MEMORY_PER_WORKER}"


