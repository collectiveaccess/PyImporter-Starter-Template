import subprocess
from pathlib import Path
import shutil

current_path = Path.cwd()
template_files_path = current_path / "template_files"
valid_directory = False


def create_project(project_path):
    choose_clone = False
    # create project basic directories/files
    shutil.copytree(template_files_path, project_path)

    # create git repo
    subprocess.run(["git", "init"], cwd=project_path)

    # add PyImporter submodules
    while not choose_clone:
        print("Enter git clone method to clone PyImporter: HTTPS or SSH", end=" ")
        clone_method = input()
        if clone_method.lower() in ["https", "ssh"]:
            choose_clone = True
            if clone_method.lower() == "ssh":
                pyimporter_url = "git@github.com:collectiveaccess/PyImporter.git"
                wikidata_url = (
                    "git@github.com:collectiveaccess/WikiData-Integration.git"
                )
            else:
                pyimporter_url = "https://github.com/collectiveaccess/PyImporter.git"
                wikidata_url = (
                    "https://github.com/collectiveaccess/WikiData-Integration.git"
                )

    subprocess.run(["git", "submodule", "add", pyimporter_url], cwd=project_path)
    subprocess.run(
        [
            "git",
            "config",
            "-f",
            ".gitmodules",
            "submodule.PyImporter.branch",
            "main",
        ],
        cwd=project_path,
    )
    subprocess.run(["git", "submodule", "add", wikidata_url], cwd=project_path)
    subprocess.run(
        [
            "git",
            "config",
            "-f",
            ".gitmodules",
            "submodule.WikiData-Integration.branch",
            "main",
        ],
        cwd=project_path,
    )

    # create first commit
    subprocess.run(["git", "add", "."], cwd=project_path)
    subprocess.run(
        ["git", "commit", '-m "Initialize PyImporter project."'], cwd=project_path
    )


while not valid_directory:
    print("Enter path of new directory:", end=" ")
    input_path = input()
    project_path = current_path / input_path

    if input_path.strip() == "":
        continue
    elif project_path.exists():
        print(f"'{project_path}' already exists.")
        continue
    else:
        valid_directory = True
        create_project(project_path)

print(f"Done setting up '{project_path}'.")
