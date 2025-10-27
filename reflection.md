1. Which issues were the easiest to fix, and which were the hardest? Why?
•	Easiest:
•	Adding missing docstrings and renaming functions to snake_case were straightforward because they involved consistent naming and adding descriptive text only.
•	Fixing mutable default arguments was simple once identified.
•	Hardest:
•	Refactoring to remove the global keyword was more complex, requiring redesign to pass and return the stock_data dictionary explicitly.
•	Proper exception handling (removing bare except and handling specific errors) required understanding possible runtime errors and careful coding.
•	Eliminating insecure functions like eval() entailed rethinking logic and ensuring security.
2. Did the static analysis tools report any false positives?
•	Mostly, the tools were accurate and useful.
•	A minor false positive was the warning about using f-strings inside logging calls, where tools recommended lazy % formatting even when f-strings might improve readability outside logs.
3. How would you integrate static analysis tools into your software development workflow?
•	Integrate tools like Pylint, Flake8, and Bandit into CI/CD pipelines to automatically check code quality on each commit or PR.
•	Run static analysis in local development environments on save or pre-commit hooks for immediate feedback.
•	Configure tool rules and thresholds to balance quality enforcement and false positive reduction.
4. What tangible improvements did you observe after applying fixes?
•	Code readability and maintainability improved greatly with consistent style and comprehensive documentation.
•	Robustness increased by validating inputs and handling exceptions properly, reducing runtime errors.
•	Security was enhanced by removing unsafe functions and improving error handling.
•	Developers can now trust code quality as verified by automated tools.