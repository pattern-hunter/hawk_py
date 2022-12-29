import subprocess

def core_temperatures():
    result = subprocess.run(["sensors"], capture_output=True)
    return result.stdout.decode('utf-8')