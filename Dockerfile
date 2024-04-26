FROM --platform=linux/amd64 python:3.11-slim as base

FROM base as builder

# Install build deps
RUN apt-get update && \
    apt-get install -y curl clang git openssh-client libssl-dev make pkg-config gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/


# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#installing rust
#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add cargo to PATH
#ENV PATH="/root/.cargo/bin:${PATH}"

# Install the required python packages
RUN pip install --no-cache-dir -r ui/requirements.txt

# change the working directory
#WORKDIR /app/rust_api

# Build the rust code
#RUN cargo build --release


# change the working directory
WORKDIR /app/ui

# Expose the port
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "test_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# Run the application
#CMD streamlit run app.py