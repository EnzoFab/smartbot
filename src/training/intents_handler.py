import os
import json

root_abs_path = os.path.dirname(os.path.abspath(__file__)).split('/src')[0]

json_file = json.loads(open("%s/intents.json" % root_abs_path).read())

intents = json_file.get("intents", [])