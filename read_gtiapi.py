import shlex
import subprocess
import json

def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))


if __name__ == '__main__':
    curl = '''curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/Akashd17atos/FedExTest/issues/comments/COMMENT_ID \
  -d '{"body":"Me too"}' '''
    output = call_curl(curl)
    print(output)