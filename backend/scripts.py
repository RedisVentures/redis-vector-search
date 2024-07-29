import subprocess


def load_data():
    subprocess.run(["python", "-m", "vecsim.db.load"], check=True)


def start_app():
    # load data
    subprocess.run(["python", "-m", "vecsim.db.load"], check=True)
    # start app
    subprocess.run(["python", "-m", "vecsim.main"], check=True)


def format():
    subprocess.run(["isort", "./vecsim", "./tests/", "--profile", "black"], check=True)
    subprocess.run(["black", "./vecsim"], check=True)


def check_format():
    subprocess.run(["black", "--check", "./vecsim"], check=True)


def sort_imports():
    subprocess.run(["isort", "./vecsim", "./tests/", "--profile", "black"], check=True)


def check_sort_imports():
    subprocess.run(
        ["isort", "./vecsim", "--check-only", "--profile", "black"], check=True
    )


def check_lint():
    subprocess.run(["pylint", "--rcfile=.pylintrc", "./vecsim"], check=True)


def mypy():
    subprocess.run(["python", "-m", "mypy", "./vecsim"], check=True)


def test():
    subprocess.run(
        ["python", "-m", "pytest", "vecsim", "--log-level=CRITICAL"], check=True
    )


def test_cov():
    subprocess.run(
        [
            "python",
            "-m",
            "pytest",
            "-vv",
            "--cov=./vecsim",
            "--cov-report=xml",
            "--log-level=CRITICAL",
        ],
        check=True,
    )


def cov():
    subprocess.run(["coverage", "html"], check=True)
    print("If data was present, coverage report is in ./htmlcov/index.html")
