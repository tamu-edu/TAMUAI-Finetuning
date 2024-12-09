"""
title: Self-Supervised Finetuning
author: Chuck Zuo, Ph.D.
date: 2024-12-09
"""

import argparse
import logging
import sys
from training_core.ssl_training_core import train_model

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('finetune.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Add command line argument parsing
        parser = argparse.ArgumentParser(description='LLM training script')
        parser.add_argument('--resume-checkpoint', 
                          help='Checkpoint name to resume from, e.g.: checkpoint-32 (optional)')
        parser.add_argument('--num-epochs', 
                          type=int,
                          default=10,
                          help='Total number of training epochs (default: 10)')
        args = parser.parse_args()
        
        logger.info("Program started running...")
        result = train_model(
            resume_checkpoint=args.resume_checkpoint,
            num_epochs=args.num_epochs
        )
        logger.info(f"Program ended: {result}")
        
    except Exception as e:
        logger.error("Program exited with an exception", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
