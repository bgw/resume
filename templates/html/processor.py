import jinja2
import os.path
import subprocess
import sys
from lib import base_processor

def process(config, template_path, output_path, data):
    data = base_processor.preprocess(data, "html")
    base_processor.process(config, template_path, output_path, data)
    
    loader = jinja2.FileSystemLoader(os.path.join(template_path, "data"))
    environment = jinja2.Environment(loader=loader)
    
    for template in config["use_templates"]:
        with open(os.path.join(output_path, template), "w") as f:
            f.write(environment.get_template(template).render(data))
    
    for f in config["less_files"]:
        subprocess.check_call(
            [
                "lessc", os.path.join(template_path, "data", f),
                os.path.join(output_path, f.replace(".less", ".css"))
            ],
            stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
        )
    
    subprocess.check_call(
        "yui-compressor -o *.css *.css",
        stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
        cwd=output_path
    )
