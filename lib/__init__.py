import os.path
import yaml

def open_yaml(name):
    f = open(name, "r")
    if f is None:
        return None
    return yaml.load(f)

def deep_merge_dicts(*dicts):
    """Merges two dictionaries, giving priority to the latter dictionaries. This
    is useful when you have multiple configuration files, which may be
    conflicting in certain places. Merging is done recursively."""
    merged = {}
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError
        for k, v in d.items():
            if k not in merged:
                merged[k] = v
            else:
                try:
                    merged[k] = deep_merge_dicts(merged[k], v)
                except TypeError:
                    if isinstance(v, list):
                        merged[k].extend(v)
                    else:
                        merged[k] = v
    return merged

def open_yamls(*names, search_paths=["."]):
    data = []
    datatype = None
    for n in names:
        y = open_yaml(n)
        if y is None:
            continue
        data.append(y)
        if datatype is None:
            datatype = type(y)
        elif not isinstance(y, datatype):
            raise TypeError("We cannot merge multiple YAML files with "
                            "differing types.")
    if datatype is dict:
        return deep_merge_dicts(*data)
    elif datatype is list:
        result = []; map(result.extend, data)
        return result
    else:
        raise TypeError("We cannot merge YAML files of types other than lists "
                        "or dicts.")
