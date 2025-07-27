# Demo Polylith Project

## Steps to recreate this repository:

Scaffold initial project

```shell
git init
uv init --no-description --no-readme --no-pin-python --bare --build-backend=hatch
```

Add polyith configuration to hatch builder

```shell
cat << EOF >> pyproject.toml

[tool.hatch.build]
dev-mode-dirs = ["components", "bases", "development", "."]
EOF
```

Add and initialize polylith

```shell
uv add polylith-cli --dev
uv run poly create workspace --name demo --theme loose
uv sync
```

Add project dependencies

```shell
uv add fastapi "uvicorn[standard]" pydantic sqlmodel
```

Add and configure mypy

```shell
uv add mypy --dev
cat << EOF >> pyproject.toml

[tool.mypy]
strict = true
plugins = ["pydantic.mypy"]
EOF
```

Create the 3 bricks we need to develop modular code

```shell
uv run poly create base --name webserver
uv run poly create component --name product
uv run poly create component --name database
```

Draw the rest of the owl, then validate

```shell
uv run mypy .
```