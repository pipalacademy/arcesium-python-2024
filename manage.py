import click
from pathlib import Path
from dataclasses import dataclass
import re
import shutil
import json
import shelve
import tempfile
import nbformat
import yaml
from nbconvert.preprocessors import ExecutePreprocessor

@click.group()
def cli():
    pass


@dataclass
class Assignment:
    id: int
    user: str
    path: Path

    @classmethod
    def find_all(cls, id):
        pattern = f"jupyter-*/assignments/assignment-{id:02d}.ipynb"
        paths = Path("/home/").glob(pattern)
        return [cls.from_path(path) for path in paths]

    @staticmethod
    def from_path(path: Path):
        id = re.search("assignment-(\d+).ipynb", path.name).group(1)
        id = int(id)
        user = path.parent.parent.name.replace("jupyter-", "")
        return Assignment(id=id, user=user, path=path)

    def archive(self):
        root = Path("archive") / f"assignment-{self.id:02d}"
        root.mkdir(parents=True, exist_ok=True)
        path = root / f"{self.user}.ipynb"
        shutil.copy(self.path, path)
        print("cp", self.path, path)

    def __repr__(self):
        return f"<Assignment#{self.id} {self.user}>"
    
@cli.command()
@click.option("-a", "--assignment", type=int, help="Assignment number to collect (eg. 1)")
def collect(assignment):
    """Collect assignment notebook from all the users.
    """
    assignments = Assignment.find_all(assignment)
    for a in assignments:
        print(a)
        a.archive()

@cli.command()
@click.option("-a", "--assignment", type=int, help="Assignment number to collect (eg. 1)")
def grade(assignment):
    paths = Path(f"archive/assignment-{assignment:02d}").glob("*.ipynb")

    for p in paths:
        grade_file(p)

@cli.command()
@click.option("-a", "--assignment", type=int, help="Assignment number to collect (eg. 1)")
def report(assignment):
    name = f"assignment-{assignment:02d}"
    
    with shelve.open("grades.db")  as db:
        results = [x for x in db.values() if x['assignment'] == name]
        for x in results:
            print(x['assignment'], x['username'], x['score'], x['max_score'])


@cli.command()
def report_table():
        with shelve.open("grades.db")  as db:
            results = [x for x in db.values() if x['assignment'] == name]
            for x in results:
                print(x['assignment'], x['username'], x['score'], x['max_score'])


@cli.command()
@click.option("-a", "--assignment", type=int, help="Assignment number to collect (eg. 1)")
def create(assignment):
    d = yaml.safe_load(open("assignments.yml"))
    d = {item['id']: item for item in d}
    data = d[assignment]
    print(data)

pre_code = """
VERIFY_PROBLEM_GRADES = []
"""

post_code = """
import json

with open("/tmp/grades.json", "w") as f:
    json.dump(VERIFY_PROBLEM_GRADES, f)
"""

def grade_file(path):
    print("Grading", path)
    nb = nbformat.read(open(path), as_version=4)
    nb['cells'].insert(0, nbformat.v4.new_code_cell(pre_code))
    nb['cells'].append(nbformat.v4.new_code_cell(post_code))
    p = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True)

    with tempfile.TemporaryDirectory() as tmp:
        p.preprocess(nb, {'metadata': {'path': tmp}})

    save_grade(path)

def save_grade(path):
    path = Path(path)
    username = path.stem
    assignment = path.parent.name
    results = json.load(open("/tmp/grades.json"))

    correct = {p['problem'] for p in results if p['status'] == 'pass'}
    all_problems = {p['problem'] for p in results if p['status']}
    
    grade = {
        "username": username,
        "assignment": assignment,
        "score": len(correct),
        "max_score": len(all_problems),
        "results": results
    }
    key = f"{assignment}/{username}"
    
    with shelve.open("grades.db")  as db:
        db[key] = grade

    


if __name__ == "__main__":
    cli()