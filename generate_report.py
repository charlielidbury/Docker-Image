#!/bin/python3
from os import makedirs
from os.path import dirname, exists, join, realpath

PROJ_ROOT = dirname(realpath(__file__))


def main():
    """
    List all version-controlled files and append them to a report.txt file
    """
    ls_cmd = "git ls-tree -r main --name-only"
    file_names = [
        "./Breakdown.txt",
        "./RustBenchmark/src/tablesaw.rs",
        "./RustBenchmark/src/tablesaw/lib.rs",
        "./RustBenchmark/src/tablesaw/selection.rs",
        "./RustBenchmark/src/tablesaw/table.rs",
        "./RustBenchmark/src/tablesaw/table_slice.rs",
        "./RustBenchmark/src/tablesaw/table_slice_group.rs",
        "./RustBenchmark/benches/split_on.rs",
        "./JavaBenchmark/src/main/java/uk/ac/ic/doc/spe/MyBenchmark.java",
        "./JavaBenchmark/src/main/java/uk/ac/ic/doc/spe/StandardTableSliceGroup.java",
        "./TargetApplication/src/main/java/uk/ac/ic/doc/spe/covidsaw/App.java",
        "./Report.txt",
    ]
    dir_name = "./out"
    out_file_name = join(dir_name, "report.txt")
    if not exists(dir_name):
        makedirs(dir_name)
    with open(out_file_name, "w") as out_file:
        divider = "=" * 80 + "\n"
        out_file.write(divider)
        for git_file in file_names:
            if not exists(git_file):
                print("WARNING: skipping file {}".format(git_file))
                continue
            out_file.write("{}\n".format(git_file))
            out_file.write(divider)
            with open(git_file, "r") as in_file:
                out_file.write(in_file.read())
            out_file.write(divider)


if __name__ == "__main__":
    main()
