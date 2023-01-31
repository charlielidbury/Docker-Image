#!/bin/python3
from os import makedirs
from os.path import dirname, exists, join, realpath
from subprocess import run

PROJ_ROOT = dirname(realpath(__file__))


def main():
    """
    List all version-controlled files and append them to a report.txt file
    """
    ls_cmd = "git ls-tree -r main --name-only"
    git_file_names = run(ls_cmd, shell=True, check=True, capture_output=True).stdout.decode("utf-8").split("\n")
    dir_name = "./out"
    out_file_name = join(dir_name, "report.txt")
    if not exists(dir_name):
        makedirs(dir_name)
    with open(out_file_name, "w") as out_file:
        divider = "=" * 80 + "\n"
        out_file.write(divider)
        for git_file in git_file_names:
            if len(git_file) == 0:
                continue
            out_file.write("{}\n".format(git_file))
            out_file.write(divider)
            with open(git_file, "r") as in_file:
                out_file.write(in_file.read())
            out_file.write(divider)


if __name__ == "__main__":
    main()
