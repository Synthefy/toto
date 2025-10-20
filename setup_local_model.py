#!/usr/bin/env python3
"""
Setup script to download Toto model files to a local directory with custom name.
This creates ~/models--Synthefy--tt-Open-Base-1.0/ containing the model files.
"""

import os
from huggingface_hub import hf_hub_download

def setup_local_model():
    """Download Toto model files to local directory with custom name."""
    local_dir = os.path.expanduser("~/models--Synthefy--tt-Open-Base-1.0")
    
    print(f"Creating local model directory: {local_dir}")
    os.makedirs(local_dir, exist_ok=True)
    
    print("Downloading model.safetensors...")
    model_file = hf_hub_download(
        repo_id="Datadog/Toto-Open-Base-1.0",
        filename="model.safetensors",
        local_dir=local_dir,
        local_dir_use_symlinks=False
    )
    print(f"Downloaded: {model_file}")
    
    print("Downloading config.json...")
    config_file = hf_hub_download(
        repo_id="Datadog/Toto-Open-Base-1.0",
        filename="config.json",
        local_dir=local_dir,
        local_dir_use_symlinks=False
    )
    print(f"Downloaded: {config_file}")
    
    print(f"\nSetup complete! Model files are now available at: {local_dir}")
    print("You can now use this path with Toto.from_pretrained()")

if __name__ == "__main__":
    setup_local_model()
