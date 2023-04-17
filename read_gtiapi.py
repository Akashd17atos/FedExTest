import shlex
import subprocess
import json

def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))


if __name__ == '__main__':
    curl = '''curl - X
    POST - d
    '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.2/32", "nw_proto": "ICMP", "actions": "ALLOW", "priority": "10"}'
    http: // localhost: 8080 / firewall / rules / 0000000000000001 '''
    output = call_curl(curl)
    print(output)