"""
Compute Resource Tracker
=========================

Track GPU hours, costs, and resource usage for experiments.

Author: UW MSIM Team
Date: November 2025
"""

import time
import psutil
from typing import Dict, Optional, List
import logging

logger = logging.getLogger(__name__)


class ComputeTracker:
    """
    Track compute resources and costs.

    Parameters
    ----------
    cost_per_hour : float
        Cost per GPU-hour in USD
    gpu_type : str
        GPU type (e.g., 'H200', 'A100', 'L40S')
    """

    def __init__(self, cost_per_hour: float = 0.90, gpu_type: str = 'H200'):
        self.cost_per_hour = cost_per_hour
        self.gpu_type = gpu_type
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.gpu_usage_log: List[Dict] = []

    def start(self):
        """Start tracking."""
        self.start_time = time.time()
        self.gpu_usage_log = []
        logger.info(f"Compute tracking started (GPU: {self.gpu_type}, ${self.cost_per_hour}/hr)")

    def log_gpu_usage(self):
        """Log current GPU usage."""
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()

            for gpu in gpus:
                self.gpu_usage_log.append({
                    'timestamp': time.time(),
                    'gpu_id': gpu.id,
                    'gpu_load': gpu.load * 100,
                    'memory_used_mb': gpu.memoryUsed,
                    'memory_total_mb': gpu.memoryTotal,
                    'memory_util': (gpu.memoryUsed / gpu.memoryTotal) * 100,
                    'temperature': getattr(gpu, 'temperature', None)
                })
        except ImportError:
            logger.warning("GPUtil not installed, GPU tracking unavailable")
        except Exception as e:
            logger.warning(f"GPU logging failed: {e}")

    def stop(self) -> Dict:
        """
        Stop tracking and calculate costs.

        Returns
        -------
        summary : dict
            Elapsed time, costs, and GPU usage summary
        """
        self.end_time = time.time()

        elapsed_hours = (self.end_time - self.start_time) / 3600
        total_cost = elapsed_hours * self.cost_per_hour

        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()

        summary = {
            'elapsed_hours': elapsed_hours,
            'cost_usd': total_cost,
            'cost_per_hour': self.cost_per_hour,
            'gpu_type': self.gpu_type,
            'cpu_percent': cpu_percent,
            'memory_percent': memory_info.percent,
            'memory_used_gb': memory_info.used / (1024 ** 3),
            'gpu_logs_count': len(self.gpu_usage_log)
        }

        # Average GPU utilization
        if self.gpu_usage_log:
            summary['avg_gpu_load'] = np.mean([log['gpu_load'] for log in self.gpu_usage_log])
            summary['avg_gpu_memory_util'] = np.mean([log['memory_util'] for log in self.gpu_usage_log])

        logger.info(f"Compute tracking stopped: {elapsed_hours:.2f} hours, ${total_cost:.2f}")

        return summary
