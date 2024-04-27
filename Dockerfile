FROM --platform=linux/amd64 python:3.11 as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    BUILD_MODE="release"

ENV PATH="/root/.cargo/bin:$POETRY_HOME/bin:$PATH"
ENV PYTHON_CONFIGURE_OPTS="--enable-shared"

FROM base as builder

# Install build deps
RUN apt-get update && \
    apt-get install -y curl clang git openssh-client libssl-dev make pkg-config gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#installing rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required python packages
RUN pip install --no-cache-dir -r ui/requirements.txt

# Build the rust code
RUN cargo build --manifest-path rust_api/Cargo.toml  --release 


# change the working directory
WORKDIR /app

# Expose the port
EXPOSE 8501

# Run the application
CMD bash start.sh

