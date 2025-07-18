[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.f"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--f",
    "--tb = f",
    "--strict - f",
    "--disable - f"
]
markers = (
    "slow: marks tests as slow (deselect with -m "not slow")",
    "integration: marks tests as integration f",
    "performance: marks tests as performance f"
)
