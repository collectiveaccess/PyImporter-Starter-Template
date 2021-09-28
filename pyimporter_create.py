import subprocess
from pathlib import Path
import shutil

current_path = Path.cwd()
template_files_path = current_path / "template_files"
valid_directory = False


def create_project(project_path):
    choose_clone = False
    shutil.copytree(template_files_path, project_path)
    subprocess.run(["git", "init"], cwd=project_path)

    while not choose_clone:
        print("Enter git clone method to clone PyImporter: HTTPS or SSH", end=" ")
        clone_method = input()
        if clone_method.lower() in ["https", "ssh"]:
            choose_clone = True
            if clone_method.lower() == "ssh":
                pyimporter_url = "git@github.com:collectiveaccess/PyImporter.git"
            else:
                pyimporter_url = "https://github.com/collectiveaccess/PyImporter.git"

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
    subprocess.run(["git", "add", "."], cwd=project_path)
    subprocess.run(
        ["git", "commit", '-m "Initialize PyImporter project."'], cwd=project_path
    )


while not valid_directory:
    print("Enter path of new directory:", end=" ")
    input_path = input()
    project_path = current_path / input_path

    if input_path.strip() == '':
        continue
    elif project_path.exists():
        print(f"'{input_path}' already exists. Do you want to replace it? [y/n]")
        if input().lower() in ["y", "yes"]:
            valid_directory = True
            shutil.rmtree(project_path)
            create_project(project_path)
    else:
        valid_directory = True
        create_project(project_path)

print(f"Done setting up '{input_path}'.")
