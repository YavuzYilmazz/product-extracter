# Product XML Parser

This project is a Python application designed to read, parse, and store product information from XML files into a MongoDB database. The primary focus is on extracting relevant product details, including pricing, measurements, and fabric information.

## Requirements

To run this project, you need to have the following installed:

- Python 3.7 or higher
- MongoDB (local or cloud instance)
- Required Python packages

## Getting Started

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/YavuzYilmazz/product-extracter.git
cd product-extracter
```

### Install Required Packages


```bash
pip install pymongo python-dotenv
```

or 

```bash
pip3 install pymongo python-dotenv
```

### Set Up Environment Variables

Copy the provided .env.dist file to a new file named .env in the root directory of the project:

```bash
cp .env.dist .env
```

Open the .env file in a text editor and update the following variables:

```bash
MONGO_URI=<your_mongo_uri>
DATABASE_NAME=<your_database_name>
COLLECTION_NAME=<your_collection_name>
```

### Place Your XML Files

Ensure you have your example XML files ready. Update the path in main.py where the XML file is referenced. Make sure the XML file is placed correctly, following the defined path in your code.

### Run the Application

Once you have set everything up, you can run the application using:


```bash
python src/main.py
```

or


```bash
python3 src/main.py
```

### File Directory Structure
```bash
product-extracter/
│
├── src/
│   ├── main.py          # Main entry point for the application
│   ├── config.py        # Database configuration and connection handling
│   └── classes/
│       ├── reader.py    # XML reading and parsing logic
│       ├── extractor.py  # Extractor classes for parsing product details
│       └── product.py    # Product class definition using dataclass
└── .env.dist            # Template for environment variables
```
