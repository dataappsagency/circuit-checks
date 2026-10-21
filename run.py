"""Run one pair: install its packages, make one real call through the integration, write results/<id>.json.

    python run.py <pair-id>

The check itself is pairs/<id>.py, a function check() that raises on failure and returns a short
note on success. Installed versions are read back from the environment, not from the pair file."""
import importlib.util, json, os, platform, subprocess, sys, time, traceback
from datetime import datetime, timezone
from importlib.metadata import version, PackageNotFoundError

sys.path.insert(0, os.path.abspath("pairs"))
pid = sys.argv[1]
pair = next(p for p in json.load(open("pairs.json"))["pairs"] if p["id"] == pid)
started = time.time()
result = {"pair": pid, "a": pair["a"], "b": pair["b"], "type": pair["type"], "what": pair["what"],
          "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
          "python": platform.python_version(), "runner": os.environ.get("RUNNER_OS", "local"),
          "run_url": f"{os.environ.get('GITHUB_SERVER_URL', '')}/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '')}" if os.environ.get("GITHUB_RUN_ID") else None}
try:
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check", *pair["packages"]], check=True, timeout=900)
    spec = importlib.util.spec_from_file_location("check", f"pairs/{pid}.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    result["note"] = str(mod.check())[:300]
    result["ok"] = True
except Exception as e:  # the failure is the finding
    result["ok"] = False
    result["error"] = "".join(traceback.format_exception_only(type(e), e)).strip()[-1500:]
versions = {}
for p in pair["packages"]:
    name = p.split("[")[0]
    try: versions[name] = version(name)
    except PackageNotFoundError: versions[name] = None
result["versions"] = versions
result["seconds"] = round(time.time() - started, 1)
result["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
os.makedirs("results/runs", exist_ok=True)
json.dump(result, open(f"results/runs/{pid}.json", "w"), indent=1)
print(json.dumps(result, indent=1))
sys.exit(0)   # a failing pair is a result, not a broken job
