from copy import deepcopy
import os
import os.path
import shutil
import docutils.core
from functools import lru_cache

try: # py2
    basestring
except NameError: # py3k
    basestring = str

@lru_cache(maxsize=1000)
def _rest_preprocess_core(string, writer_name):
    parts = docutils.core.publish_parts(string.replace("\n", "\n\n"),
                                        writer_name=writer_name)
    body = parts["body"]
    if "tex" in writer_name.lower():
        # horrible, horrible, fragile hacks:
        body = body.replace("\item", "\item[-]")
    return body.strip()

def rest_preprocess(string, writer_name):
    # only process it if it is a large block of text
    if string.endswith("\n"):
        return _rest_preprocess_core(string, writer_name)
    else:
        return string

def rest_preprocess_recursive(obj, writer_name):
    if isinstance(obj, basestring):
        return rest_preprocess(obj, writer_name)
    try:
        for k in (obj.keys() if hasattr(obj, "keys") else range(len(obj))):
            obj[k] = rest_preprocess_recursive(obj[k], writer_name)
    except TypeError:
        pass
    return obj

def preprocess(data, rest_writer_name):
    data = deepcopy(data)
    # convert ReST blocks to fancy formatted text
    data = rest_preprocess_recursive(data, rest_writer_name)
    if "experiences" in data:
        data["experiences"].sort(key=lambda ex: ex["priority"])
    return data

def process(config, template_path, output_path, data):
    # shutil.rmtree(output_path)
    try:
        os.makedirs(output_path)
    except OSError:
        pass
    
    for f in config["copy_data"]:
        shutil.copyfile(os.path.join(template_path, "data", f),
                        os.path.join(output_path, f))
