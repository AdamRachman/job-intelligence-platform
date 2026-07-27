import subprocess
import time


command = [
    "python",
    "-m",
    "tests.linkedin.connector_test"
]


result = subprocess.run(command)


if result.returncode != 0:
    print("First run failed. Restarting...")

    time.sleep(3)

    subprocess.run(command)