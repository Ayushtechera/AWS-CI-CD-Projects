# Taking base image of python 3.12
FROM python:3.12 
# Creating app folder
WORKDIR /app
# Copying all the project code into app
COPY . /app 

# This will update the packages in our image and instal AWS CLI(by using AWS CLI we can control AWS Services form our terminal)
RUN apt update -y && apt install awscli -y

# This will install the requirements that is present in requirements.txt
RUN pip install -r requirements.txt

# This is a command (python app.py) which will be automatically executed when we start the container
CMD ["python" , "app.py"]  