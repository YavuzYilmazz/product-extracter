# Product XML Parser

This project is a Python application designed to read, parse, and store product information from XML files into a MongoDB database. The primary focus is on extracting relevant product details, including pricing, measurements, and fabric information.

## Requirements

To run this project, you need to have the following installed:

- Python 3.7 or higher
- MongoDB (local or cloud instance)
- Required Python packages

### Required Python Packages

You can install the required Python packages using pip. Here are the packages needed for the project:

```bash
pip install pymongo python-dotenv
```

or


```bash
pip3 install pymongo python-dotenv
```


### File Directory Structure

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
