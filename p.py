import subprocess

conversion_command = f"python convert.py darknet191.cfg darknet19.weights model_data/darknet19editv2.h5"
subprocess.run(conversion_command, shell=True)


