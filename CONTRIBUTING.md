# Contributing to MLA

Thank you for considering contributing to our project! Whether you're fixing bugs, adding new features, improving documentation, or suggesting enhancements, your contributions are greatly appreciated.

## Getting Started

1. **Fork the Repository**: Use the GitHub interface to fork the repository to your account.
2. **Clone the Repository**: Clone your fork locally:

   ```bash
   git clone git clone https://github.com/MohammadLotfiA/MLA.git
   cd MLA
   ```

3. **Set Up the Development Environment**:

   - Install dependencies:

     ```bash
     pip install -r requirements.txt # Python dependencies
     npm install # Node.js dependencies
     ```

   - Install `pre-commit` hooks:

     ```bash
     pre-commit install
     ```

## How to Contribute

### 1. Reporting Issues

- Check if the issue has already been reported.
- If not, create a new issue and include:
  - A clear title and description.
  - Steps to reproduce (if applicable).
  - Relevant logs, screenshots, or code snippets.

### 2. Fixing Bugs or Adding Features

- Ensure your changes align with the project’s goals and architecture.
- Follow these steps:

  1. Create a new branch for your changes:

     ```bash
     git checkout -b feature/your-feature-name
     ```

  2. Make your changes, and ensure all tests pass.
  3. Format your code and run linters:

     ```bash
     pre-commit run --all-files
     ```

  4. Commit your changes:

     ```bash
     git commit -m "Add your descriptive commit message"
     ```

  5. Push the branch:

     ```bash
     git push origin feature/your-feature-name
     ```

### 3. Submitting a Pull Request

- Ensure your branch is up to date with the `main` branch:

  ```bash
  git pull origin main
  ```

- Open a pull request (PR) on GitHub:
  - Provide a clear title and description of your changes.
  - Link related issues (e.g., `Closes #123`).

### 4. Writing Tests

- Include tests for new features or bug fixes:
  - Use `pytest` for Python.
  - Use `jest` for JavaScript/TypeScript (if applicable).
- Run all tests before submitting:

  ```bash
  pytest
  npm test
  ```

## Code Guidelines

- **Coding Standards**:
  - Python: Follow PEP 8.
  - JavaScript/TypeScript: Follow ESLint rules.
- **Security**:
  - Avoid hardcoding sensitive information.
  - Run `gitleaks` to check for secrets before committing.

## Licensing

By contributing, you agree that your contributions will be licensed under the project's license.

---

Thank you for contributing! If you have any questions, feel free to reach out.
