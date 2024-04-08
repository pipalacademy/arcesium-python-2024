import yaml
import nbformat as nbf
from pathlib import Path
from . import config


class Problem:
    def __init__(self, name, metadata):
        self.name = name
        self.metadata = metadata
        self.title = self.metadata['title']
        self.root = Path(config.PROBLEM_REPOSITORY_PATH) / name

        self.problem_type = metadata.get("problem_type")
        self.script_name = metadata.get("script_name")

    @classmethod
    def find(cls, name):
        path = Path(config.PROBLEM_REPOSITORY_PATH) / name / "problem.yml"
        metadata = yaml.safe_load(path.open())
        return cls(name, metadata)

    def open(self, path):
        return self.joinpath(path).open()

    def joinpath(self, path):
        p = self.root / path
        return p

    def get_description(self):
        return self.open("description.md").read()

    def get_initial_code(self):
        files = self.metadata['files'].get('code', [])
        if files:
            return self.open(files[0]).read()

    def get_description_html(self):
        desc = self.get_description()
        return self.markdown(desc)

    def markdown(self, text):
        return markdown.markdown(text, extensions=['fenced_code'])

