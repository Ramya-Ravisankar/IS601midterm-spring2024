# Project: Command Pattern and Plugins Homework 5
Incorporated the functionalities discussed in the lecture videos to the previous calculator assignment. This includes transforming the calculator program into an interactive application using the command pattern and REPL (Read, Evaluate, Print, Loop) principles.

### More information on the code changes and description
1. added four basic commands: add, subtract, multiply, and divide, making the calculator program interactive.

2. Implemented a menu command that displays available commands from the command dictionary at the application's start and when the user types "menu."

3. Tested the functionality and coverage

4. implemented the plugins - refactored the code to automatically load plugins, facilitating easy command additions without manual updates.

## References
1. [Python Loop Performance](https://www.youtube.com/watch?v=Qgevy75co8c) - Insights into loop efficiency.
2. [Habits of The Good Programmer](https://www.youtube.com/watch?v=q1qKv5TBaOA&t=2s) - Design patterns and best practices.
3. [Global Interpreter Lock and Multicore Issues in Python](https://www.youtube.com/watch?v=m4zDBk0zAUY) - Python concurrency explained by its inventor.
4. [Design Patterns Explained](https://www.youtube.com/watch?v=tv-_1er1mWI) - General programming design patterns.
5. [5 Patterns in Python](https://www.youtube.com/watch?v=YMAwgRwjEOQ) - Applying patterns in Python.
6. [InstructorVideos]
Plugins Lecture- (https://youtu.be/c2PmjazGW2w)
command pattern lecture - https://www.youtube.com/watch?v=3DVUN091T5g

## Project Setup

1. Clone the repository.
2. CD into the project folder.
3. Create and activate the virtual environment (VE).
4. Install the required libraries.

## Testing Commands

- Run all tests with `pytest`.
- To test a specific file, use `pytest tests/test_main.py`.
- For linting and coverage, `pytest --pylint --cov` commands can be used separately.

## Installed Libraries

1. [Pytest](https://docs.pytest.org/en/8.0.x/)
2. [Faker](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)

## Adding a Library

1. Ensure you're in the correct VE; if unsure, run "deactivate".
2. Activate the VE.
3. Update the requirements file with `pip freeze > requirements.txt`.
