# Quadratic Equations Solver

This script is pre-commit hook for git. Before commit will send to repository it run the tests and if tests are done the commit is ok.

# How to use

1. If you're using `virtualenv` - change path to python interpreter inside `pre-commit` file.
2. Copy `pre-commit` to `.git/hooks` in your project directory.
3. Make pre-commit executable by running `chmod +x .git/hooks/pre-commit` (on linux system)
4. From now on every time you'll try to run `git commit` there will be execution of `pre-commit` file and it runs tests from `tests.py`
If all tests have passed - commit will be created. Otherwise it won't.

## When you try to commit bad code

```bash
$ git commit -m "test pre"
.E..
======================================================================
ERROR: test_returns_none_for_complex_solution (__main__.QuadraticEquationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 22, in test_returns_none_for_complex_solution
    root1, root2 = get_roots(1, 2, 3)
  File "/home/warner/warn_test/14_pre_commit_hook/quadratic_equation.py", line 6, in get_roots
    root1 = (-b - sqrt(discriminant)) / (2 * a)
ValueError: math domain error

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)
Tests failed
```

## When all tests are OK
```bash
$ git commit -m "fix quadratic_equation.py"
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
Tests passed
[master cdaad92] fix quadratic_equation.py
 1 file changed, 3 insertions(+), 3 deletions(-)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
