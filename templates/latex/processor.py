import jinja2
import os.path
import subprocess
import sys
from lib import base_processor

def process(config, template_path, output_path, data):
    data = base_processor.preprocess(data, "latex2e")
    base_processor.process(config, template_path, output_path, data)
    
    loader = jinja2.FileSystemLoader(os.path.join(template_path, "data"))
    environment = jinja2.Environment("<|", "|>", "<<", ">>", "<#", "#>",
                                     loader=loader,
                                     extensions=["jinja2.ext.do"])
    
    for template in config["use_templates"]:
        with open(os.path.join(output_path, template), "w") as f:
            f.write(environment.get_template(template).render(data))
