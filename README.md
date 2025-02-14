# Django Demo Project (for University)

## 1. Installation

Run the following command to clone the repository:
```
git clone git@github.com:Mattia-Sacchi/CasaFruit-DjangoProject.git
```

## 2. Set up the virtual environment
Create and activate a virtual environment to manage project dependencies:

```
source ./.venv/bin/activate
```

# Project Overview
## Object Management
The system allows users to interact with objects in the following ways:

__Viewing:__ Users can view objects in the system.

__Selection:__ Users can select individual or multiple objects.

__Grading:__ Users can grade selected objects.

Any changes made during selection or grading must be reflected in the database.

## Functionality
The core features of the project include:

__Object Selection:__ Users can select individual objects or groups of objects.
__Grading/Selection Operations:__ Users can grade or select objects, and these actions will be saved in the database.
__Viewing Results:__ Users can view the results of their interactions (selection or grading).

# File Import and Processing
The project supports importing objects described in a CSV format. The workflow is as follows:

__CSV Import:__ Objects are imported from CSV files.
__Template:__ The system loads templates from the file system.
__Data Processing:__ A view is provided to analyze the data and insert it into the database.

The application follows a structured layout with three main HTML blocks:

__Header__
__Content__
__Footer__


## Authentication
The application supports user authentication, including:

- User Registration: New users can register by providing their information.
- User Login: Registered users can log in to the website using their credentials.

## Adding files
In the settings page it is possible to upload a zip file containing data.
The file must be names data.json and contain the data of name, price, description and image name.
The zip file must also contain the images

## Custom Functionalities
The project includes custom features designed to enhance user interaction:

Item Selection & Ordering: Users can select items they wish to purchase and place an order.
Business Contact: Users can contact the business owner to request the addition of new products to the platform.



