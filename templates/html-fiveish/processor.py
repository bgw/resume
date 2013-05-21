import jinja2
import os.path
import subprocess
import sys
from lib import base_processor

def process(config, template_path, output_path, data):
    data = base_processor.preprocess(data, "html")
    base_processor.process(config, template_path, output_path, data)

    loader = jinja2.FileSystemLoader(os.path.join(template_path, "data"))
    environment = jinja2.Environment(loader=loader, trim_blocks=True)

    for template in config["use_templates"]:
        with open(os.path.join(output_path, template), "w") as f:
            f.write(environment.get_template(template).render(data))

    subprocess.check_call(
        [
            "compass", "compile",
            "--output-style=expanded",
            "--css-dir", output_path
        ] + config["sass_files"],
        cwd=os.path.join(template_path, "data"),
        stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
    )
