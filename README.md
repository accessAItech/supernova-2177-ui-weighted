# superNova_2177/ ⚡️🌌🎶🚀🌸🔬 
STRICTLY A SOCIAL MEDIA PLATFORM  
Intellectual Property & Artistic Inspiration  
Legal & Ethical Safeguards
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BP-H/community_guidelines/blob/main/LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://opensource.org/)
[![Contributors Welcome](https://img.shields.io/badge/Contributors-Welcome-brightgreen.svg)](https://github.com/BP-H/community_guidelines/issues)
[![Stars](https://img.shields.io/github/stars/BP-H/community_guidelines?style=social)](https://github.com/BP-H/superNova_2177)

**A scientifically grounded social metaverse engine for collaborative creativity**

This repository hosts `superNova_2177.py` — an experimental protocol merging computational sociology, quantum-aware simulation logic, and creative systems engineering. It models symbolic influence, interaction entropy, and network resonance across users and content, with classical compatibility and quantum-readiness.

⚠️ This is *not* a financial product, cryptocurrency, or tradable asset. All metrics (e.g., Harmony Score, Resonance, Entropy) are symbolic — for modeling, visualization, and creative gameplay only. See legal/disclaimer sections in `superNova_2177.py`, lines 60–88.
Symbolic tokens and listings introduced in the gameplay modules have **no real-world monetary value**. They exist purely as resonance artifacts used for cooperative storytelling.

The repository includes a *patch monitor* that scans new contributions for these
required disclaimers. If added files or lines don't contain the phrases
`STRICTLY A SOCIAL MEDIA PLATFORM`, `Intellectual Property & Artistic
Inspiration`, and `Legal & Ethical Safeguards`, the commit will fail in CI and
locally if pre-commit hooks are installed.

````markdown
# superNova_2177 🧠

**AI-Powered Scientific Validation with Built-In Integrity Scoring**

A modular intelligence pipeline that evaluates hypotheses through evidence-based validation, peer review scoring, and manipulation resistance.

## 🚀 Quick Start

```bash
# create the virtual environment and install dependencies
python setup_env.py
# or install dependencies manually
pip install -r requirements.txt

# optional: launch the API immediately
# python setup_env.py --run-app

# optional: build the Transcendental Resonance frontend
# pip install nicegui  # install the NiceGUI package
# python setup_env.py --build-ui
# The NiceGUI web interface now lives in `transcendental_resonance_frontend/`.
# This folder was historically called `web_ui`.
# Launch the frontend directly with
# ```bash
# python -m transcendental_resonance_frontend
# ```
# Or explore the demo data using
# ```bash
# python -m transcendental_resonance_frontend.demo
# ```

# optional: launch the Streamlit UI
# python setup_env.py --launch-ui
# or run manually with
./start.sh       # launches ui.py on port 8888
# pass --real-backend or set USE_REAL_BACKEND=1 to sync with the backend
streamlit run app.py  # launch the Streamlit server
# or use the CLI directly

# Try demo mode
supernova-validate --demo

# Run your own validation set
supernova-validate --validations sample_validations.json
# List existing forks
supernova-federate list

# Create a new fork with custom config
supernova-federate create --creator Alice --config HARMONY_WEIGHT=0.9

# Cast a vote on a fork

supernova-federate vote <fork_id> --voter Bob --vote yes
````

The UI listens on [http://localhost:8888](http://localhost:8888) by default.
Append `?healthz=1` to the URL and you should see `ok` when the server is running.

## 🔧 Local Development

To launch the Streamlit UI:

```bash
chmod +x start.sh
./start.sh  # launches ui.py
# enable the real backend via ./start.sh --real-backend or USE_REAL_BACKEND=1
streamlit run app.py  # same as above
```

Either `start.sh` or `streamlit run app.py` will launch the dashboard from anywhere in the repo.
Run `curl http://localhost:8888/?healthz=1` to verify the server is up.

## ☁️ Launch Online

[![Run in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/BP-H/superNova_2177)
[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/BP-H/superNova_2177/HEAD) *(Binder support coming soon)*


After the workspace loads, run:
```bash
python one_click_install.py --launch-ui
```

## 📦 Installation

### Step-by-Step

1. **Install Python 3.11 or newer** from [python.org](https://www.python.org/)
   if it isn't already on your machine. This project requires Python 3.11+.
   You can check by running `python --version` in your terminal.
2. **Run the setup script** to create the virtual environment and install all
   dependencies locally. Install any missing system libraries first (see
   [System Packages](#system-packages)). You can also pass `--locked` to install packages from
   `requirements.lock` for deterministic builds. Additional flags `--run-app`
   and `--build-ui` can automatically start the API or compile the frontend. Use
   `--launch-ui` to open the Streamlit dashboard after install:
   ```bash
   python setup_env.py
   # python setup_env.py --run-app    # launch API after install
   # python setup_env.py --locked     # install from requirements.lock
    # python setup_env.py --build-ui   # build Transcendental Resonance frontend assets
   # python setup_env.py --launch-ui  # run the Streamlit UI on port 8888
   ```
  You can also let `install.py` choose the appropriate installer for your
  platform:
  ```bash
  python install.py
  ```
This project depends on libraries such as `fastapi`, `pydantic-settings`, `structlog`, `prometheus-client`, and core packages like `numpy`, `python-dateutil`, `sqlalchemy>=2.0`, and `email-validator`. The full list lives in `requirements.txt`. A pared-down `requirements-minimal.txt` installs only what is necessary to run the unit tests and now includes `requests`.
  If you prefer to manage the environment manually, install the required
  packages yourself using `requirements.txt`:
  ```bash
  pip install -r requirements.txt  # installs numpy, python-dateutil, email-validator, streamlit-ace, etc.
  ```
   A PyPI wheel is currently unavailable. Run `python setup_env.py` or use the online installer scripts:
   ```bash
   # Linux/macOS
   ./online_install.sh
   # Windows
  ./online_install.ps1
  ```
3. **Activate the environment**:
   ```bash
   # Linux/macOS
   source venv/bin/activate
   # Windows
   .\venv\Scripts\activate
   ```
4. **Install the pre-commit hooks** so linting and the patch monitor run automatically:
   ```bash
   pre-commit install
   ```
5. You're ready to run the demo commands shown in [Quick Start](#-quick-start).
6. On first launch the application seeds `harmonizers.db` with an `admin`,
   `guest`, and `demo_user` account so the UI has sample profiles ready.

### Module Search Path

Add the repository root to your `PYTHONPATH` or install the project in editable
mode so imports like `from utils.api import api_call` resolve correctly:

```bash
pip install -e .
# or
export PYTHONPATH="${PWD}"
```

### Extras

The NiceGUI-based frontend under `transcendental_resonance_frontend/` is
optional. Install `nicegui` if you'd like to build and launch that interface:

```bash
pip install nicegui
```

The Streamlit dashboard works without `nicegui`, so you can skip this package
when using the Streamlit-only UI.

### System Packages

Install these system dependencies if they're missing on your platform. If you
build the project using Docker, these packages are installed automatically:

**Ubuntu**

```bash
sudo apt-get install build-essential libsnappy-dev libsdl2-dev …
```

The Docker image installs these dependencies automatically, so you only
need them locally when running without Docker.

**macOS**

```bash
brew install snappy sdl2 …
```

### Makefile Quick Commands

For convenience, the repository includes a `Makefile` with common tasks:

```bash
make install  # set up the environment
make test     # run tests
make lint     # run mypy type checks on the main modules
```

### Pre-commit Hooks

Set up pre-commit to automatically format and lint the code. The hooks depend on
packages from **both** `requirements-minimal.txt` and
`requirements-dev.txt`, and also run the `patch-monitor` hook to enforce the
disclaimer policy:

```bash
pip install -r requirements-minimal.txt -r requirements-dev.txt
pre-commit install
```

Running `pre-commit install` ensures the patch monitor executes before each
commit so that missing disclaimer text is caught locally.

You can run all checks manually with:

```bash
pre-commit run --all-files
```

### Platform Quick Commands

**Windows PowerShell**

```powershell
./online_install.ps1
```

**macOS (bash)**

```bash
./online_install.sh
```

**Linux (bash)**

```bash
./online_install.sh
```

**Docker**

```bash
docker-compose up --build
```

**Offline Installer**

```bash
python one_click_install.py
# python one_click_install.py --launch-ui  # open the Streamlit UI on port 8888
```

This script automatically installs the `tqdm` package if it isn't available so
that progress bars work out of the box.

This project relies on features introduced in **SQLAlchemy 2.x** such as
`DeclarativeBase`. Ensure you have `sqlalchemy>=2.0` installed. The code also
requires `python-dateutil` for timestamp parsing.

## 🏁 Getting Started

Set up a Python environment and install the package and its dependencies:

```bash
pip install .
# install optional libraries used by the tests
pip install -r requirements.txt  # includes streamlit-ace
# To install the exact versions used during development,
# use the generated `requirements.lock` file instead:
# pip install -r requirements.lock
```

Run the full test suite to verify your setup:

```bash
pytest
```

## 🔧 Configuration

`SECRET_KEY` can be supplied via environment variables for JWT signing. If it is
not set, a secure random value will be generated automatically:

```bash
# optional
export SECRET_KEY="your-random-secret"
```

`METRICS_PORT` configures the Prometheus metrics server port. If unset a free port will be selected automatically. Override it if the default `8001` is unavailable:

```bash
export METRICS_PORT=9000
```

Copy `.env.example` to `.env` and set values for `SECRET_KEY` and
`BACKEND_URL`. Provide your own connection string for `DATABASE_URL` via
environment variables rather than hard-coding it. Set `DB_MODE=central` if you
want to use a shared PostgreSQL instance instead of the default local SQLite
file.

## 🐳 Docker

You can build a standalone Docker image or run the API with Postgres and Redis
via `docker-compose`.

Build the image:
```bash
docker build -t supernova-2177 .
```

To build and run the Streamlit UI inside Docker:
```bash
docker build -t supernova-ui .
docker run -p 8888:8888 supernova-ui
```

The build process installs required system libraries such as `libsnappy-dev`
and SDL dependencies, so no manual setup is needed when using Docker.

Or bring up the full stack:
```bash
cp .env.example .env  # set your own secrets
docker-compose up
```


The application will be available at [http://localhost:8000](http://localhost:8000),
and the Streamlit UI at [http://localhost:8888](http://localhost:8888).


## Authentication

Register first using `POST /users/register` then obtain a token with `POST /login`.
The login route returns a JWT and a freshly initialized `universe_id` for your account.

## 🎛️ Local Streamlit UI

To experiment with the validation analyzer locally, first build the NiceGUI
frontend found in `transcendental_resonance_frontend/` and launch the Streamlit
dashboard:

```bash
python setup_env.py --build-ui --launch-ui
```
This command compiles the UI assets and starts the app on
[http://localhost:8888](http://localhost:8888).
You can still run `make ui` from the repository root to launch the demo only.
`ui.py` provides the full dashboard and loads pages from
`transcendental_resonance_frontend/pages/`. Launch it with:

```bash
python transcendental_resonance_frontend/ui.py
# or
python -m transcendental_resonance_frontend
```

The lightweight `app.py` instead reads the thin wrappers under the top-level
`pages/` directory:

```bash
streamlit run app.py
```

Both entry points are powered by `render_modern_layout`. Common UI patterns like alerts, theme
switching and layout containers live in `streamlit_helpers.py`:

```python
from streamlit_helpers import header, alert, theme_selector, centered_container
```

Import these helpers at the top of your Streamlit files to keep the UI code
clean and consistent. Run these commands from the repository root; `ui.py`
remains the primary launcher while `app.py` offers a streamlined demo.

Exporting plots as static images requires the `kaleido` package. Install it
using `pip install -r requirements-streamlit.txt` if it isn't already available.

Open [http://localhost:8888](http://localhost:8888) in your browser to interact with the demo. Use the **Reset to Demo** button below the editor to reload `sample_validations.json` at any time. Append `?healthz=1` to the URL for a quick health check.

The CI pipeline performs a lightweight health check against the Streamlit server. It simply requests `/?healthz=1` to ensure the app boots correctly:

```bash
curl -f "http://localhost:8888/?healthz=1"
```

`ui.py` reads configuration from `st.secrets` when running under Streamlit. If
the secrets dictionary is unavailable (such as during local development), the
module falls back to a development setup equivalent to:

```python
{"SECRET_KEY": "dev", "DATABASE_URL": "sqlite:///:memory:"}
```

## 📊 Dashboard

The dashboard provides real-time integrity metrics and network graphs built with `streamlit`, `networkx`, and `matplotlib`. Upload your validations JSON or enable demo mode to populate the table. You can edit rows inline before re-running the analysis to see how scores change.

```bash
streamlit run app.py
```
By default the demo listens on port `8888`. Set `STREAMLIT_PORT` or pass
`--server.port` to use a different port.

Use the sidebar file uploader to select or update your dataset, then click **Run Analysis** to refresh the report.
Missing packages such as `tqdm` are installed automatically when you run `one_click_install.py` so progress bars work without extra setup.

A small simulation form captures interactions between nodes. Enter a source, target,
edge type and timestamp to build an in-memory `InfluenceGraph`. The graph preview and
ancestor/descendant traces update as you submit events.

Use the **Resonance Music** page to generate simple MIDI snippets and view the metrics returned by the `/resonance-summary` endpoint.

Additional pages for **Voting**, **Agents**, and **Social** features are
accessible from the navigation bar. These sections provide early scaffolding
for governance, AI insights, and community interaction.

Full implementations for these pages live in
`transcendental_resonance_frontend/tr_pages/`. The lightweight files under the
top-level `pages/` directory simply import and call those modules.


### Starting the Backend

The API must be reachable at [http://localhost:8000](http://localhost:8000). Start it with:

```bash
uvicorn superNova_2177:app --reload --port 8000
# or
python superNova_2177.py
```

The Streamlit page expects this backend by default. If you run it elsewhere, set
the `BACKEND_URL` environment variable so the UI can find the API.

### Troubleshooting the UI

- **Missing dependencies**: If the interface fails with `ModuleNotFoundError`, run
  `pip install -r requirements-streamlit.txt` to ensure all packages are available.
- **Port already in use**: Pass `--server.port` to Streamlit or set the
  `STREAMLIT_PORT` environment variable to use a different port.
- **Browser does not open**: Navigate manually to
  [http://localhost:8888](http://localhost:8888) or the port you selected.
- **Disable debug prints**: Set `UI_DEBUG_PRINTS=0` in your environment to silence
  startup logging from `ui.py`.

### CI Health Check

The continuous integration workflow starts the Streamlit UI using the
`STREAMLIT_PORT` environment variable (default `8888`). A fallback handler in
`ui.py` responds with `ok` when `/?healthz=1` is requested. Verify that your
local server is running with:

```bash
curl http://localhost:${STREAMLIT_PORT:-8888}/?healthz=1
```

You should see the plain text `ok` if the app started correctly.

### Job Queue & Polling

Long-running tasks started via the UI now run asynchronously. Use the
`queue_*` routes to start a job and `poll_*` to check its status. Example:

```python
from frontend_bridge import dispatch_route

# queue an introspection audit
job = await dispatch_route("queue_full_audit", {"hypothesis_id": "H1"})

# later poll for the result
status = await dispatch_route("poll_full_audit", {"job_id": job["job_id"]})
```

The returned status dictionary includes ``status`` and ``result`` keys. Events
are still emitted via the hook managers when a job completes.

## 🌩️ Streamlit Cloud

Deploy the demo UI online with Streamlit Cloud:

1. Fork this repository on GitHub.
2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud) and select **New app**.
3. Choose the repo and set `ui.py` as the entry point.
4. Add your `SECRET_KEY` and set a `DATABASE_URL` secret with your connection string under **Secrets** in the app settings.
5. Streamlit will install dependencies from `requirements-streamlit.txt` and launch the app.

### Secrets Configuration

Streamlit Cloud stores sensitive values in a private secrets editor. Open the
app dashboard, choose **Settings → Secrets**, and paste key/value pairs such as:

```toml
SECRET_KEY = "dev"
DATABASE_URL = "sqlite:///:memory:"
```

These defaults match the local development fallback shown above, but you should
replace them with a strong secret key and a persistent database URL for real
deployments. See Streamlit's [secrets documentation](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/app-secrets)
for more detail.

`kaleido` is bundled in `requirements.txt` so image export features work on Streamlit Cloud.


After the build completes, you'll get a shareable URL to interact with the validation demo in your browser.

## 🤝 UI Integration

The `frontend_bridge` module exposes a lightweight router for the UI. Handlers
register themselves with `register_route_once(name, func)` and are invoked through
`dispatch_route`.

A convenient read-only route `"list_routes"` returns the currently available
route names. This can help debug which backend callbacks are present:

```python
from frontend_bridge import dispatch_route

routes = await dispatch_route("list_routes", {})
print(routes["routes"])
```

For more detail, dispatch the `"help"` route to get descriptions grouped by
category:

```python
info = await dispatch_route("help", {})
``` 

During development, you can also open `/ui/debug_panel` in the NiceGUI
frontend to interactively invoke these routes. The panel lists every
registered name with a JSON payload editor and uses `dispatch_route` under
the hood.
Moderators can visit `/moderation` to review flagged posts in the new Moderation Dashboard.
 
### Frontend Bridge & Social Hooks

`frontend_bridge` now includes routes for cross-universe provenance and other
social network operations. Events emitted by these routes trigger hooks defined
in `hooks/events.py`.

Example dispatch using the router:

```python
from frontend_bridge import dispatch_route
from protocols.utils.messaging import MessageHub
from hooks import events

bus = MessageHub()
bus.subscribe(events.CROSS_REMIX_CREATED, lambda m: print(m.data))

await dispatch_route(
    "cross_universe_register_bridge",
    {
        "coin_id": "abc123",
        "source_universe": "testnet",
        "source_coin": "xyz789",
        "proof": "http://example.com/proof",
    },
)
```

The `MessageHub` message bus lets observers react to hook events in real time.
See `docs/hooks.md` for the full list of event names.

## 🎥 Voice & Video Chat

Start the backend and Streamlit UI as described above. Then open the **Video Chat** page from the sidebar to begin an interactive session.

1. Click **Start Session** to establish the WebSocket connection.
2. Enter text messages and select a target language to display live translations.
3. With `gtts` and `pygame` installed, translated speech plays automatically.

This feature is experimental and intended for demo use only.


## 🧪 Running Tests

Before invoking `pre-commit` or `pytest`, install the minimal testing
dependencies:

```bash
pip install -r requirements-minimal.txt
```

This ensures `pytest-asyncio` is available so that asynchronous test
fixtures work correctly.

You can then add the full development tools by installing
`requirements-dev.txt`:

```bash
pip install -r requirements-dev.txt
pytest
```

`requirements-dev.txt` includes `pytest` and all libraries required for
development. For a lightweight setup you can instead install only the
packages from `requirements-minimal.txt` or use
`requirements.txt`/`requirements.lock` for the complete environment.

Before running the tests, install the packages from `requirements.txt` (or the expanded minimal file) if you want the real dependencies. Otherwise, the built-in stubs will activate automatically. Use the setup script with locked versions or `pip` directly:

```bash
python setup_env.py --locked  # install from requirements.lock
pip install -r requirements.txt  # installs streamlit-ace
```

### Test Requirements

Before running `pre-commit` or `pytest`, install **both** requirement
files so that all dependencies are available:

```bash
pip install -r requirements-minimal.txt -r requirements-dev.txt
```

`requirements-minimal.txt` installs `fastapi`, `pydantic`,
`pydantic-settings`, `python-multipart`, `structlog`,
`prometheus-client`, `requests` and the core scientific packages (`numpy`,
`python-dateutil`, `sqlalchemy`, `networkx`, `pytest-asyncio`, `httpx`,
`email-validator`). `pytest-asyncio` enables the async fixtures used
throughout the test suite. With these installed, running `pytest` should
succeed (`99 passed`).

Missing packages trigger the simplified stubs in `stubs/`, which can
lead to confusing test failures.

### Real Module Dependencies

The test suite falls back to lightweight stubs when optional packages
are missing. To exercise the real authentication module, install the
actual libraries:

```bash
pip install redis passlib[bcrypt] python-jose[cryptography]
```

UI-specific tests rely on additional optional packages. Install `streamlit` and
`nicegui` if you want to exercise the full UI suite:

```bash
pip install streamlit nicegui
```

Optional splash animations use the `streamlit-lottie` package. If it is not
installed, the UI falls back to static emoji icons. Install it with:

```bash
pip install streamlit-lottie
```

Machine learning-based content scanning uses PyTorch. Install `torch` to enable
these features; otherwise they will be automatically disabled.

Installing both requirement files ensures all dependencies used in CI
are available:

```bash
pip install -r requirements-minimal.txt -r requirements-dev.txt
```

Run `pytest` after installing the packages to validate your setup.

You can also run static type checks with `mypy`:

```bash
pytest
mypy hypothesis_meta_evaluator.py \
     causal_trigger.py \
     introspection/introspection_pipeline.py
```

The provided `Makefile` exposes `make test` and `make lint` wrappers for these commands.

### Makefile Commands

For a quicker workflow you can use the provided `Makefile`:

```bash
# install project dependencies
make install

# run the full test suite
make test

# run static type checks
make lint
```

## 📦 Building an Executable

You can package the command line interface into a standalone binary using
PyInstaller. Run the helper script:

```bash
scripts/build_executable.sh
```

On Windows, use the PowerShell version:

```powershell
scripts/build_executable.ps1
```

To build installers for all supported platforms in one step, execute:

```bash
scripts/build_all_installers.sh
```

This wrapper calls `build_executable.sh`, `build_executable.ps1`,
`build_appimage.sh`, and `supernova_installer.nsi` in sequence to create the
`.msi`, `.dmg`, and `.AppImage` files inside `dist/`.

The generated executable will be placed under `dist/` as `supernova-cli` on
Unix systems or `supernova-cli.exe` on Windows.

### Running the Installer

If you're on Windows, download `supernova-cli.exe` from the [GitHub Releases page](https://github.com/BP-H/superNova_2177/releases/latest)
or build it yourself with the script above. Before launching, set the required
environment variables so the application can connect to its services. `SECRET_KEY`
is optional because a secure one will be generated if omitted:

```bash
# optional
export SECRET_KEY="your-secret"
export DATABASE_URL="postgresql+asyncpg://<username>:<password>@<hostname>/<database>"
export BACKEND_URL="http://localhost:8888"
```

To connect to a central database instead of the local file, pass
`--db-mode central` when launching the application or set `DB_MODE=central`.

After setting the variables, execute the binary directly:

```bash
./supernova-cli --demo   # on Windows use supernova-cli.exe
```

### One-Click Installers

Prebuilt installers for each platform are published under the [Releases page](https://github.com/BP-H/superNova_2177/releases).
Each installer bundles Python 3.11 and all dependencies so it works offline:

* **Windows** – download [`SuperNova_2177.msi`](dist/SuperNova_2177.msi) and run
  it to install the CLI.
* **macOS** – open [`supernova-cli.dmg`](dist/supernova-cli.dmg) and drag the app
  to `Applications`.
* **Linux** – download [`supernova-cli.AppImage`](dist/supernova-cli.AppImage),
  make it executable with `chmod +x` and run it directly.

```powershell
# Windows
./SuperNova_2177.msi
```

```bash
# macOS
open supernova-cli.dmg
```

```bash
# Linux
chmod +x supernova-cli.AppImage
./supernova-cli.AppImage
```

If you prefer to build everything locally, run:

```bash
python one_click_install.py
# python one_click_install.py --launch-ui  # open the Streamlit UI on port 8888
```

The script detects your OS, downloads Python 3.11 if necessary, bundles the
dependencies into `offline_deps/`, creates a virtual environment, and installs
the package.

## ✨ Features

* **🧠 Smart Scoring** — Combines confidence, signal strength, and NLP sentiment
* **🛡️ Manipulation Detection** — Flags collusion, bias, and temporal anomalies
* **📊 Multi-Factor Analysis** — Diversity, reputation, coordination, timing
* **📋 Actionable Reports** — Output includes flags, scores, certification level
* **🧵 Fully Modular** — Each analysis step is plug-and-play

## 📈 Example Output

```
🔬 VALIDATION REPORT — superNova_2177
=============================================

✅ CERTIFICATION: PROVISIONAL
📊 Consensus Score: 0.782
👥 Validators: 5

🛡️ INTEGRITY
Risk Level: MEDIUM
Integrity Score: 0.683
Flags: ['limited_consensus', 'low_diversity']

💡 Recommendation:
- Add more validators from diverse affiliations
- Check timestamp clustering for coordination risks
```

## 🔮 Fork Metrics

`supernova-federate create` computes an *entropy divergence* value for each new fork.
This is the mean absolute deviation between your provided configuration and the
default `Config` parameters. After harmonizers vote with `supernova-federate vote`,
the CLI recalculates a consensus score using `quantum_consensus`. When the
optional `qutip` dependency is installed, this applies a Pauli-Z expectation over
all votes; otherwise it falls back to a simple majority fraction.

Both divergence and consensus are **symbolic gameplay indicators** only — they
carry no real financial or governance weight.

## 📓 Jupyter Examples

Two notebooks in `docs/` showcase how to run the validation pipeline and plot
coordination graphs using the sample data in `sample_validations.json`.

Launch them from the repository root:

```bash
jupyter notebook docs/Validation_Pipeline.ipynb
jupyter notebook docs/Network_Graph_Visualization.ipynb
```

See `docs/hooks.md` for a catalogue of hook event names used by the
`HookManager`.

## 🏗️ Architecture (v4.6)

* `validation_integrity_pipeline.py` — Orchestrator for full validation logic
* `reputation_influence_tracker.py` — Tracks and scores validators over time
* `diversity_analyzer.py` — Detects echo chambers and affiliation bias
* `temporal_consistency_checker.py` — Tracks time-based volatility
* `network_coordination_detector.py` — Spots suspicious group behavior using
  sentence‑embedding similarity
* Planned: `vote_registry.py` with identity linking, public timelines per species, and real-time consensus graphs

## 🧪 Status

**v4.6 — Stable & Ready**

* Robust CLI
* Structured error handling
* Transparent results
* Designed for peer-reviewable output

---

*Built for scientific integrity in a world of noise.*


## 📝 Contributing RFCs

We welcome design proposals through our RFC process. Create a numbered folder under `rfcs/` with a `README.md` describing your idea and update `rfcs/README.md` to add its title. Open a pull request so the community can review.

