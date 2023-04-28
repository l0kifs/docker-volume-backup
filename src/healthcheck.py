import os

# Get the exit code of the previous container
exit_code = int(os.environ.get('EXIT_CODE', 0))

# Check if the exit code is non-zero
if exit_code != 0:
    raise Exception('Container restarted due to an exception')