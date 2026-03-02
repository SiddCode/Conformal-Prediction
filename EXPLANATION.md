# Python Project Template

A high-quality Python project template with modern tooling, type checking, linting, and automated code quality enforcement.

## Why This Template is High Quality

### 1. **Modern Dependency Management with uv**
   - Uses `uv` for fast, reliable dependency management
   - Lock file (`uv.lock`) ensures reproducible builds across environments
   - Automatic virtual environment management via Makefile

### 2. **Comprehensive Code Quality Tools**
   - **Ruff**: Ultra-fast Python linter and formatter
     - Enforces PEP 8 style guidelines
     - Catches common bugs and code smells
     - Auto-fixes many issues with `make fix`
   - **MyPy**: Static type checker
     - Catches type errors before runtime
     - Gradual typing support (configured to be permissive)
   - **PyRefly**: Additional static analysis
   - **Ty**: Type checker with flexible rules

### 3. **Automated Quality Workflow**
   The Makefile provides a unified interface:
   ```bash
   make check   # Run all quality checks
   make fix     # Auto-fix issues and format code
   make fmt     # Format code only
   make install # Set up environment and install tools
   ```

### 4. **Type Safety Configuration**
   - MyPy configured for Python 3.12 with sensible defaults
   - Type inference enabled for gradual adoption
   - Clear type hints encouraged but not enforced

### 5. **Clean Project Structure**
   ```
   .
   ├── src/           # Source code
   ├── configs/       # Configuration files (optional)
   ├── data/          # Data files (optional)
   ├── tests/         # Tests (optional - add your own)
   ├── Makefile       # Automation commands
   ├── pyproject.toml # Project metadata and dependencies
   ├── mypy.ini       # MyPy configuration
   ├── pyrefly.toml   # PyRefly configuration
   └── .python-version # Python version specification
   ```

### 6. **Python Version Pinning**
   - Explicit Python version specification (`.python-version`)
   - Ensures consistent runtime across team members
   - Prevents subtle version-related bugs

### 7. **Fast Development Loop**
   - Pre-commit-style checks via `make check`
   - Quick feedback loop for code quality
   - Automated formatting reduces code review friction

## Getting Started

### 1. Copy the Template
```bash
cp -r /path/to/Template_Project /path/to/your-new-project
cd /path/to/your-new-project
```

### 2. Customize Project Metadata
Edit `pyproject.toml`:
- Change `name` to your project name
- Update `description`
- Add your dependencies to the `dependencies` list

### 3. Install Dependencies and Tools
```bash
make install
. .venv/bin/activate
```

### 4. Start Coding
Create your source files in `src/` directory. Example:
```bash
touch src/__init__.py
touch src/main.py
```

### 5. Run Quality Checks
```bash
make check   # Verify code quality
make fix     # Auto-fix issues
make fmt     # Format code
```

## Recommended Workflow

1. Make changes to code
2. Run `make fix` to auto-format and fix issues
3. Run `make check` to verify everything passes
4. Commit only after checks pass

## Adding Tests (Optional)

Create a `tests/` directory:
```bash
mkdir tests
touch tests/__init__.py
touch tests/test_main.py
```

Install pytest and run tests:
```bash
uv pip install pytest
pytest tests/
```

## Customization Options

### Add Lint Rules
Edit `pyproject.toml` under `[tool.ruff.lint]`:
```toml
select = [
    "E", "F", "B", "C4", "SIM", "I", "UP", "PIE", "PGH", "PYI", "RUF",
]
```

### Stricter Type Checking
Edit `mypy.ini`:
```ini
[mypy]
disallow_untyped_defs = True  # Require type hints on all functions
```

### Add Custom Make Commands
Edit `Makefile` to add your own automation targets.

## Dependencies Already Configured

This template uses these excellent tools out-of-the-box:
- **ruff**: Fast linting and formatting
- **mypy**: Static type checking
- **pyrefly**: Additional static analysis
- **ty**: Type checking with flexible rules

All are automatically installed by `make install`.

## Philosophy

This template follows the principle of **"Quality by Default"**:
- Code quality is enforced, not optional
- Tools run fast to not slow development
- Gradual adoption of type safety
- Reproducible environments via lock files

Copy this template whenever you start a new Python project to maintain consistent quality across your codebase.
