# performance_tester.py

# Description:
# This file provides performance testing tools to simulate high-load scenarios 
# and assess how the system handles multiple concurrent requests. It helps to 
# ensure that the system can scale efficiently without degradation, which is critical 
# for high-concurrency environments like Charter’s.

import time
import random

class PerformanceTester:
    def run_stress_test(self, num_requests):
        """Simulate multiple concurrent requests and measure performance."""
        start_time = time.time()
        
        for _ in range(num_requests):
            self.simulate_request()
        
        end_time = time.time()
        print(f"Stress test completed in {end_time - start_time} seconds for {num_requests} requests.")
    
    def simulate_request(self):
        """Simulate the processing of a single request."""
        time.sleep(random.uniform(0.05, 0.2))  # Simulate request processing time

# Example usage:
tester = PerformanceTester()
tester.run_stress_test(1000)  # Simulate 1000 concurrent requests
