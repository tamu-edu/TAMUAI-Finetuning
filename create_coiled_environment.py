"""
title: Create Coiled Environment
author: Chuck Zuo, Ph.D.
date: 2024-12-09
"""

import coiled
try:
    coiled.delete_software_environment("llm-training-env")
    print("environment deleted")
except Exception as e:
    print(f"Error deleting environment: {str(e)}")
    
coiled.create_software_environment(
    name="llm-training-env",
    pip=[
        "torch",
        "transformers",
        "datasets",
        "coiled",
        "PyMuPDF",
        "tqdm",
        "google-cloud-storage",
        "aiohttp",
        "accelerate>=0.26.0",
        "safetensors",
        "bitsandbytes",
        "numpy>=2.1.3",
        "dask==2024.10.0",
        "distributed==2024.10.0",
    ]
)
