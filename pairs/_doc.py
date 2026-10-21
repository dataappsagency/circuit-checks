import os
def sample():
    path = "/tmp/circuit_check.html"
    with open(path, "w") as f:
        f.write("<html><body><h1>circuit</h1><p>circuit checks that integrations run.</p></body></html>")
    return path
