import subprocess

def test_docs_build():
    result = subprocess.run(
        ["mkdocs", "build", "--strict"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Docs build failed: {result.stderr}"
    assert "Documentation built" in result.stdout
