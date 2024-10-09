FROM langchain/langchain:latest 


# Update packages and install nano and curl
RUN apt-get update -y 
RUN apt-get install nano curl -y

# THIS IS SPECIFIC TO HUGGINFACE
# We create a new user named "user" with ID of 1000
RUN useradd -m -u 1000 user
# We switch from "root" (default user when creating an image) to "user" 
USER user
# We set two environmnet variables 
# so that we can give ownership to all files in there afterwards
# we also add /home/user/.local/bin in the $PATH environment variable 
# PATH environment variable sets paths to look for installed binaries
# We update it so that Linux knows where to look for binaries if we were to install them with "user".
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# We set working directory to $HOME/app (<=> /home/user/app)
WORKDIR $HOME/app

# Copy all local files to /home/user/app with "user" as owner of these files
# Always use --chown=user when using HUGGINGFACE to avoid permission errors
COPY --chown=user . $HOME/app

# Install all dependencies
RUN pip install -r requirements.txt
# make sure all packages are up to date
RUN pip install --upgrade -r requirements.txt

# Run FastAPI
CMD fastapi run app.py --port 7860