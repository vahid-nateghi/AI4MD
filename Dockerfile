FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Expose Jupyter's port to your machine
EXPOSE 8888

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --all-groups --no-install-project

# Copy the rest of your source code and tests
COPY . .

# Sync the project itself
RUN uv sync --frozen --all-groups

# Default command to run when the container starts
CMD ["uv", "run", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]