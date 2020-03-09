import sys

import bolt
import subprocess


# todo add mypy check & doctest
config = {
    "runtest": {},
    "black": {},
    "flake8": {},
    "conttest": {"task": "execute", "directory": "."},
}

if sys.platform.startswith("win32"):
    PYTHON_CMD = ["py", "-3"]
else:
    PYTHON_CMD = ["python3"]


def output_result(result, tool_name: str):
    """
    Output result of subprocess.run() for a given tool
    :type result: subprocess.CompletedProcess
    """
    stdout = result.stdout.decode("utf-8")
    if stdout:
        print(f"{tool_name} Output:\n{stdout}\n")

    stderr = result.stderr.decode("utf-8")
    if stderr and result.returncode != 0:
        print(f"{tool_name} Error:\n{stderr}")


def black_task(**_):
    result = subprocess.run(["black", "."], capture_output=True)
    output_result(result, "Black")


def flake8_task(**_):
    result = subprocess.run(
        # , "--exclude=.venv"
        [*PYTHON_CMD, "-m", "flake8", ".", "--ignore=E501,W503,W293"],
        capture_output=True,
    )
    output_result(result, "Flake8")


def runtest_task(**_):
    result = subprocess.run([*PYTHON_CMD, "-m", "pytest", "tests"], capture_output=True)
    output_result(result, "Pytest")


bolt.register_task("black", black_task)
bolt.register_task("flake8", flake8_task)
bolt.register_task("runtest", runtest_task)
bolt.register_task("execute", ["black", "flake8", "runtest"])
