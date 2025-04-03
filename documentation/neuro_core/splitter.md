# 🧠 splitter.py — GPU-Enhanced Task Splitter

## Overview

`splitter.py` is the foundational component of the NeuroMesh Engine. It divides a compute-intensive job into smaller **GPU-executed chunks**, allowing for distributed, verifiable, and throttled task execution across hardware.

Unlike traditional simulators or CPU-based jobs, this module **executes real PyTorch GPU workloads** and logs each chunk's compute behavior.

---

## 💡 Key Features

- ✅ Real matrix math on GPU (`torch.matmul`)
- ✅ Adaptive chunk splitting for multi-stage jobs
- ✅ Logs task ID, duration, device, and timestamp
- ✅ Generates a verifiable `.json` proof-of-execution file
- ✅ Runs safely on CPU if no GPU is available

---

## 🧪 What It Actually Does

- Accepts a job like `"demo_job"` and number of `chunks`
- Performs real GPU tensor multiplications per chunk
- Measures how long each takes, and on which device
- Saves full logs to `logs/demo_job_xxxxxxxx.json`

---

## ⚙️ Parameters

| Argument     | Description                             |
|--------------|-----------------------------------------|
| `job_name`   | Custom identifier for this session       |
| `chunks`     | Number of slices to divide the job into |
| `matrix_size`| Matrix dimension (e.g. 512 = 512x512)   |
| `passes`     | How many compute passes per chunk       |

---

## 🖥️ Sample Output Log

```json
[
  {
    "task_id": "demo_job_chunk_1",
    "device": "cuda",
    "matrix_size": "512x512",
    "passes": 10,
    "duration_sec": 1.3081,
    "timestamp": "2025-03-31T23:15:23.821Z"
  }
]
