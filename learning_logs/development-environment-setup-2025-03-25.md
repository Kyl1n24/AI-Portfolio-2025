# Development Environment Setup Guide

This guide provides detailed instructions for setting up a complete Python AI development environment with Anaconda, VS Code, and GitHub integration. It follows professional standards and best practices for AI/ML development.

## Table of Contents

- [1. Anaconda Installation](#1-anaconda-installation)
- [2. Environment Configuration](#2-environment-configuration)
- [3. VS Code Setup](#3-vs-code-setup)
- [4. Project Structure](#4-project-structure)
- [5. Git Configuration](#5-git-configuration)
- [6. GitHub Repository Setup](#6-github-repository-setup)
- [7. Environment Verification](#7-environment-verification)
- [8. Troubleshooting](#8-troubleshooting)
- [9. Best Practices](#9-best-practices)

## 1. Anaconda Installation

```bash
# Download the exact version (prevents compatibility issues)
# Official direct link: https://www.anaconda.com/download/success
```

**Installation Options:**
- Installation path: `C:\Anaconda3` (avoid spaces and non-English characters)
- ✅ Check "Add Anaconda3 to my PATH environment variable"
- ✅ Check "Register Anaconda3 as my default Python 3.9"

**Verify Installation:**
```bash
conda --version  # Should display conda 23.x+
python --version  # Should display Python 3.9.x
```

## 2. Environment Configuration

### Create Isolated Environment

```bash
# Create a dedicated environment with Python 3.9
conda create -n ai-lab python=3.9 -y

# Activate the environment
conda activate ai-lab

# Verify environment path
which python  # Should output: /c/Anaconda3/envs/ai-lab/python.exe
```

### Install Dependencies with Exact Versions

```bash
# Install core packages with conda (more stable)
conda install -y pandas=1.5.3 matplotlib=3.7.1

# Install additional packages with pip
pip install seaborn==0.12.2 requests==2.31.0

# Generate requirements.txt (best practice for reproducibility)
pip freeze > requirements.txt
```

## 3. VS Code Setup

### Essential Extensions

1. **Python** (ID: ms-python.python)
2. **Jupyter** (for .ipynb notebooks)
3. **GitLens** (ID: eamodio.gitlens)
4. **Conda Tools** (for environment detection)

### Configure Python Interpreter

1. `Ctrl+Shift+P` → "Python: Select Interpreter" → select `ai-lab` environment
2. Verify selection in the status bar (bottom left)

### Terminal Integration

1. Open Settings (JSON):
```json
{
  "python.defaultInterpreterPath": "C:/Anaconda3/envs/ai-lab/python.exe",
  "terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"],
  "python.terminal.activateEnvironment": true
}
```

### Fix PowerShell Execution Policy

1. **Run PowerShell as Administrator**
2. **Modify execution policy**:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. **Verify policy update**:
   ```powershell
   Get-ExecutionPolicy  # Should output RemoteSigned
   ```

### Initialize Conda for Shells

```bash
conda init powershell
conda init cmd.exe
```

Edit PowerShell profile at `Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`:
```powershell
# Add this line to auto-activate environment
conda activate ai-lab
```

## 4. Project Structure

### Current Structure Analysis

```
AI-Portfolio-2025/
├── daily_progress/          # Daily exercise code
│   └── YYYY-MM-DD/          # Organized by date
├── projects/                # Larger project folders
├── learning_logs/           # Documentation/notes
├── .env.example             # Template for environment variables
├── .gitignore               # Prevent sensitive data commits
└── README.md                # Project documentation
```

### Enhanced Structure (Recommended)

Execute in project root:
```bash
# Create enhanced directory structure
mkdir -p src/utilities   # Core utility functions
mkdir -p tests/unit      # Unit tests
mkdir -p data/raw        # Raw data (add to .gitignore)
mkdir -p learning_logs   # Learning documentation

# Update .gitignore
This project uses a comprehensive Python `.gitignore` file based on the [GitHub Python template](https://github.com/github/gitignore/blob/main/Python.gitignore).

Key ignored patterns include:
- `__pycache__/` and compiled Python files
- Environment directories (`.env`, `.venv`, etc.)
- Build artifacts and packaging files
- Jupyter notebook checkpoints
- Local cache and log files
- `data/raw/` - Raw data files

See the [full .gitignore file](.gitignore) in the repository root.
```

Create template for environment variables:
```bash
echo "# Environment variables example file" > .env.example
echo "# Replace with your actual API key" >> .env.example
echo "HF_API_KEY=your_huggingface_api_key_here" >> .env.example
```

## 5. Git Configuration

### Installation

1. Download and install [Git for Windows](https://git-scm.com/download/win)
2. **Important checkboxes during installation**:
   - ✅ Add Git to PATH
   - ✅ Choose your preferred code editor (VS Code, Cursor, etc.)

### Global Configuration

```bash
# Set username (match GitHub username)
git config --global user.name "YourGitHubUsername"

# Set email (match GitHub email)
git config --global user.email "your.email@example.com"

# Set your preferred editor (examples below)
# For VS Code:
git config --global core.editor "code --wait"
# For Cursor:
git config --global core.editor "cursor --wait"

# Verify configuration
git config --list  # Should show user.name and user.email
```

### SSH Key Setup

```bash
# Generate Ed25519 SSH key (more secure)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Display public key (copy output)
cat ~/.ssh/id_ed25519.pub
```

Add the key to GitHub: Profile → Settings → SSH and GPG keys → New SSH Key

## 6. GitHub Repository Setup

### Initialize Repository

Two approaches:

#### Option A: Create New Repository

```bash
# Initialize local repository
git init

# Add remote GitHub repository
git remote add origin https://github.com/yourusername/AI-Portfolio-2025.git

# Verify remote is correctly set
git remote -v
```

#### Option B: Clone Existing Repository

```bash
# If repository already exists on GitHub
git clone https://github.com/yourusername/AI-Portfolio-2025.git
cd AI-Portfolio-2025
```

### Commit Best Practices

```bash
# Check status before commits
git status

# Stage specific files (recommended)
git add daily_progress/2025-03-22/
git commit -m "feat(api): integrate Hugging Face with environment variable support"

# Stage all changes (use cautiously)
git add .
git commit -m "docs: add comprehensive environment setup guide"
```

### Branch Management Strategy

```bash
# Create feature branch for daily tasks
git checkout -b feature/daily-20250323

# After development, merge to main
git checkout main
git merge --no-ff feature/daily-20250323
git branch -d feature/daily-20250323
```

### Push to Remote Repository

```bash
# First push with branch setup
git push -u origin main

# Subsequent pushes
git push origin main

# Push feature branch
git push origin feature/daily-$(date +%Y%m%d)
```

## 7. Environment Verification

Run these commands to verify your environment is correctly set up:

```bash
# Check Python packages
conda list | grep pandas  # Should show pandas=1.5.3

# Verify Python executable
python -c "import sys; print(sys.executable)"  # Should point to ai-lab environment

# Check Git remote
git remote -v  # Should show your GitHub repository
```

## 8. Troubleshooting

### Conda Environment Issues

If environment problems occur:

```bash
# Clean reinstall of environment
conda deactivate
conda remove -n ai-lab --all -y
conda create -n ai-lab python=3.9 -y
conda activate ai-lab
pip install -r requirements.txt  # Using previously generated file
```

### VS Code Terminal Not Showing Conda Environment

1. Close VS Code completely
2. Check Conda initialization:
   ```bash
   conda init
   ```
3. Restart VS Code

### Git Authentication Problems

```bash
# Test SSH connection
ssh -T git@github.com  # Should show successful authentication

# If using HTTPS, configure credential helper
git config --global credential.helper wincred
```

## 9. Best Practices

- **Record error messages** as valuable learning material
- **Use emojis in README.md** to make it more engaging
- **Install packages through Anaconda Prompt** rather than VS Code terminal until environment is properly configured
- **Use descriptive commit messages** following [Conventional Commits](https://www.conventionalcommits.org/) format
- **Create frequent small commits** rather than infrequent large ones
- **Never commit API keys or sensitive data**
- **Check `git status` before and after adding files** to ensure appropriate changes
- **Use branches for features** and experiments
- **Include proper documentation** in learning_logs for future reference

---

*This guide was created on March 24, 2025 as part of the AI-Portfolio-2025 project initialization.*