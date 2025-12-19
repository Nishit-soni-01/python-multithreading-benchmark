# ⚡ Python Multithreading Benchmark: I/O Concurrency vs. Sequential

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Focus](https://img.shields.io/badge/Focus-Performance_Optimization-red?style=for-the-badge)

A data engineering case study demonstrating the impact of **Multithreading** on I/O-bound tasks. This project benchmarks two different approaches to downloading high-resolution images: a standard synchronous loop versus a concurrent `ThreadPoolExecutor` implementation.

---

## 📊 The Result: 5x Speed Increase

I conducted a benchmark downloading **20 High-Res Images** from a placeholder API.

| Approach | Execution Type | Time Taken | Status |
| :--- | :--- | :--- | :--- |
| **Sequential** | Single-Threaded | ~42.70.0 seconds | 🐢 Slow |
| **Concurrent** | Multi-Threaded (5 Workers) | **~17.23 seconds** | ⚡ **500% Faster** |

> **Note:** *Results may vary based on internet bandwidth and CPU architecture.*


---

## 🛠️ How It Works

### 1. The Slow Way (`sequential_downloader.py`)
This script iterates through URLs one by one. The CPU sits idle while waiting for the server to respond to the previous request before sending the next one.
* **Mechanism:** Simple `for` loop.
* **Bottleneck:** Network latency (I/O).

### 2. The Fast Way (`concurrent_downloader.py`)
This script uses **Python's `concurrent.futures` module**. It spawns a pool of worker threads. When one thread is waiting for a server response (I/O), the CPU switches to another thread to initiate a new request.
* **Mechanism:** `ThreadPoolExecutor` with `max_workers=5`.
* **Optimization:** Overlapping I/O wait times.

---

## ⚙️ Installation & Usage


1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Benchmark**
    
    **🐢 Test the Slow Version:**
    ```bash
    python sequential_downloader.py
    ```

    **⚡ Test the Fast Version:**
    ```bash
    python concurrent_downloader.py
    ```

---



https://github.com/user-attachments/assets/c9f412ea-a20f-4855-a693-973f86309a01


## 📂 Project Structure

```text
├── sequential_downloader.py   # Single-threaded implementation (Control)
├── concurrent_downloader.py   # Multi-threaded implementation (Variable)
├── requirements.txt           # Dependencies (requests, tqdm)
├── README.md                  # Project documentation
├── assets/                    # Graphs and screenshots
└── downloaded_images/         # Output directory (Auto-generated)
