import subprocess
from pathlib import Path
import shutil

current_path = Path.cwd()
template_files_path = current_path / "template_files"
valid_directory = False
valid_wikidata_input = False


def create_project(project_path):
    scripts_path = project_path / 'importer_scripts'
    choose_clone = False
    # copy directories/files
    shutil.copytree(template_files_path, project_path)

    # create git repo
    subprocess.run(["git", "init"], cwd=project_path)

    # choose git clone method
    while not choose_clone:
        print("Enter git clone method to clone PyImporter: HTTPS or SSH", end=" ")
        clone_method = input()
        if clone_method.lower() in ["https", "ssh"]:
            choose_clone = True
            if clone_method.lower() == "ssh":
                pyimporter_url = "git@github.com:collectiveaccess/PyImporter.git"
                wikidata_url = (
                    "git@github.com:collectiveaccess/WikiDataIntegration.git"
                )
            else:
                pyimporter_url = "https://github.com/collectiveaccess/PyImporter.git"
                wikidata_url = (
                    "https://github.com/collectiveaccess/WikiDataIntegration.git"
                )

    # add PyImporter submodule
    subprocess.run(["git", "submodule", "add", pyimporter_url], cwd=scripts_path)
    subprocess.run(
        [
            "git",
            "config",
            "-f",
            ".gitmodules",
            "submodule.PyImporter.branch",
            "main",
        ],
        cwd=scripts_path,
    )

    # add Wikidata submodule
    if add_wikidata_submodule:
        subprocess.run(["git", "submodule", "add", wikidata_url], cwd=scripts_path)
        subprocess.run(
            [
                "git",
                "config",
                "-f",
                ".gitmodules",
                "submodule.WikiDataIntegration.branch",
                "main",
            ],
            cwd=scripts_path,
        )

    # create first commit
    subprocess.run(["git", "add", "."], cwd=project_path)
    subprocess.run(
        ["git", "commit", '-m Initialize PyImporter project.'], cwd=project_path
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

    valid_directory = True


while not valid_wikidata_input:
    print("Include Wikidata submodule [y/n]:", end=" ")
    wiki_input = input().lower()

    if wiki_input in ["y", "yes"]:
        add_wikidata_submodule = True
    elif wiki_input in ["n", "no"]:
        add_wikidata_submodule = False
    else:
        continue

    valid_wikidata_input = True

create_project(project_path)

print("\n", f"Done setting up '{project_path}'.")
