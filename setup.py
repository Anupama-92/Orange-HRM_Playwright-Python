from setuptools import setup, find_packages

setup(
    name="playwright-tests",  # package name (you can change)
    version="0.1.0",          # update as needed
    author="Anupama Saranu",
    author_email="anupama.saranu@gmail.com",
    description="Playwright automation tests for OrangeHRM",
    packages=find_packages(),
    install_requires=[
        "playwright",      # core dependency
        "pytest",          # test framework
        "pytest-playwright",  # pytest integration
        "allure-pytest",   # if you use allure reporting
    ],
    python_requires=">=3.8",
)
