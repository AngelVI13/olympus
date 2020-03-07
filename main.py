import re
import os
from typing import Pattern
import matplotlib
import matplotlib.pyplot as plt


# import argparse


# parser = argparse.ArgumentParser(description="Generate your code mountain!")
input_dir = "."


def get_files_from_dir(pattern: Pattern, directory: str):
    """
    Generator that yields all filenames matching the provided pattern
    in the provided directory.
    """
    # todo need to add abspath here
    for dirpath, dirnames, filenames in os.walk(directory):
        matched_files = (f for f in filenames if re.match(pattern, f))
        yield from matched_files


def compute_elevation(text_lines):
    # todo convert tabs to spaces before performing operation
    symbol_pattern = r"^(\s*)"
    for line in text_lines:
        match = re.search(symbol_pattern, line)
        if match is None:
            yield 0
            continue

        yield match.end(1)


def get_lines_from_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        yield from f


def main():
    files = get_files_from_dir(pattern=r"boltfile\.py", directory=".")

    file_ = next(files)
    lines = get_lines_from_file(file_)

    elevation = list(compute_elevation(lines))

    fig, ax = plt.subplots()
    ax.step(range(len(elevation)), elevation, label=file_)
    ax.set_xlabel("line no")
    ax.set_ylabel("code elevation")
    ax.set_title("Code elevation")
    ax.legend()
    # fig.save("myimage.png")
    plt.savefig("myimage.png")


if __name__ == "__main__":
    main()
