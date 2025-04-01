# splitter.py
# First module of NeuroMash - splits into microtaks

def split_job(job_data: str, num_chunks: int = 4) -> list[str]:
    """
    Splits a job into smaller chunks.

    Args:
        job_data (str): The content to split.
        num_chunks (int): How many chunks to create.

    Returns:
        list[str]: The job split into parts.
    """
    # Step 1: Get the total length of the job string
    total_length = len(job_data)
    
    # Step 2: Calculate how big each chunk should be (minimum 1)
    chunk_size = total_length // num_chunks
    if chunk_size == 0:
        chunk_size = 1 # Prevent zero-size chunks
    
    # Step 3: Create a list of chunks using a loop
    chunks = []
    for start in range(0, total_length, chunk_size):
        end = start + chunk_size
        chunk = job_data[start:end]
        chunks.append(chunk)
    
    # Step 4: Return the list of chunks
    return chunks
    
if __name__ == "__main__":
    job = "THIS_IS_A_DEMO_AI_JOB_PAYLOAD"
    chunks = split_job(job, 4)
    print("Chunks:", chunks)