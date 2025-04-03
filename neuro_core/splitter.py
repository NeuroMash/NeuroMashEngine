"""
splitter.py

REAL GPU TASK SPLITTER — EXECUTES FRACTIONAL GPU TASKS

- Splits a large math job (matrix multiplication) into smaller pieces (chunks).
- Runs each piece on the computer's fast math processor (GPU) if available, or the main processor (CPU).
- Records how long each piece takes and what processor it used.
- Saves this record as proof that the job was done.
"""

import torch  # type: ignore # Library for doing math with GPUs
import time  # Library for measuring time
import json  # Library for saving data in a readable format
import os  # Library for working with files and folders
from datetime import datetime  # Library for getting the current date and time
import uuid  # Library for creating unique IDs

def run_gpu_chunk(task_id: str, size: int = 256, passes: int = 5) -> dict:
    """
    Runs a piece of the math job (matrix multiplication) and records information about it.

    Args:
        task_id (str): A unique name for this piece of the job.
        size (int): The size of the grids of numbers to multiply (e.g., 256 means 256x256 grids).
        passes (int): How many times to multiply the grids together.

    Returns:
        dict: A record (dictionary) of what happened during this piece of the job.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Check if a GPU is available, use it if it is, otherwise use CPU.
    start_time = time.time()  # Record the time when this piece of the job started.

    x = torch.rand(size, size).to(device)  # Create a grid of random numbers and put it on the GPU (or CPU).
    y = torch.rand(size, size).to(device)  # Create another grid of random numbers and put it on the GPU (or CPU).

    for _ in range(passes):  # Repeat the multiplication 'passes' number of times.
        x = x @ y  # Multiply the two grids together and store the result in 'x'.

    torch.cuda.synchronize() if device.type == "cuda" else None  # If using a GPU, wait until it finishes all its work.

    end_time = time.time()  # Record the time when the chunk finished.

    log = {  # Create a record (dictionary) of what happened.
        "task_id": task_id,  # The unique name of this piece of the job.
        "device": str(device),  # The processor used (GPU or CPU).
        "matrix_size": f"{size}x{size}",  # The size of the grids.
        "passes": passes,  # How many multiplications were done.
        "duration_sec": round(end_time - start_time, 4),  # How long it took, in seconds.
        "timestamp": datetime.utcnow().isoformat() + "Z"  # The date and time when this piece was done.
    }

    return log  # Return the record.

def split_and_run(job_name: str, chunks: int, size: int = 256, passes: int = 5):
    """
    Splits a real matrix job into GPU-powered chunks and logs results.
    """
    results = []  # List to store the results of each chunk.
    os.makedirs("logs", exist_ok=True)  # Create a 'logs' folder if it doesn't exist.
    print(f"📦 Starting job: {job_name}")  # Print a message indicating the start of the job.

    for i in range(chunks):  # Loop through each chunk.
        task_id = f"{job_name}_chunk_{i+1}"  # Create a unique ID for the chunk.
        print(f"  🚀 Running chunk {i+1}/{chunks}...")  # Print a message indicating the start of the chunk.
        log = run_gpu_chunk(task_id, size=size, passes=passes)  # Run the chunk and get the log.
        results.append(log)  # Add the log to the results list.

    # Save proof
    output_file = f"logs/{job_name}_{uuid.uuid4().hex[:8]}.json"  # Create a unique filename for the log file.
    with open(output_file, "w") as f:  # Open the file for writing.
        json.dump(results, f, indent=2)  # Save the results as a JSON file.

    print(f"✅ Finished all chunks. Log saved to {output_file}")  # Print a message indicating the end of the job and where the log is saved.

if __name__ == "__main__":
    # Customize here:
    JOB_NAME = "demo_job"  # Name of the job.
    CHUNKS = 3  # Split into 3 tasks.
    MATRIX_SIZE = 512  # Use small size to avoid heavy GPU usage.
    PASSES = 10  # Do 10 matrix multiplications per chunk.

    split_and_run(JOB_NAME, CHUNKS, MATRIX_SIZE, PASSES)  # Run the job.