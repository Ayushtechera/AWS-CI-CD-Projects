# Taking base image of python 3.12
FROM python:3.12-slim
# Creating app folder
WORKDIR /app
# Copying all the project code into app
COPY . /app 

# AWS CLI lightweight install + cleanup ek hi layer mein
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws && \
    apt-get remove -y curl unzip && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# This will install the requirements that is present in requirements.txt
RUN pip install -r requirements.txt

# This is a command (python app.py) which will be automatically executed when we start the container
CMD ["python" , "app.py"]  