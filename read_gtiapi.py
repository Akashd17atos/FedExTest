import requests

import json

comment = "This is a console output"

comment_dict = {"body":comment}

comments_json_string = json.dumps(comment_dict)

headers = {

'Authorization': 'token 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',

'Content-Type': 'application/x-www-form-urlencoded',

}


data = comments_json_string


response = requests.post(

'https://api.github.com/repos/AishwaryaAtos/Demo_github_actions/issues/1/comments',

headers=headers,

data=data,

)


print("This is test")

print(response)
