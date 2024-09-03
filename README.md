# Drug-Discovery

This repository contains a Python script for fetching chemical compound data from the ChEMBL database using the chembl_webresource_client library. The ChEMBL database is a large-scale bioactivity database that provides information on drug-like molecules and their interactions, making it a valuable resource for drug discovery projects.

Features
Dynamic Data Retrieval: Fetch compound data directly from the ChEMBL database without needing to manually download datasets.
Customizable Queries: Search for compounds by name, target, or other properties using flexible query options.
Easy Integration: The script converts the retrieved data into a Pandas DataFrame, facilitating further analysis or integration with other drug discovery tools.

---

## Requirements:
Python 3.6 or higher
chembl-webresource-client
pandas

---

## Usage
Fetching Compound Data
You can fetch data about chemical compounds from ChEMBL by modifying the search criteria within the script. The default script fetches information about compounds based on their name.

Here's how to use the script:

Modify the Search Criteria: Update the keyword or other criteria in the script to search for specific compounds.
Run the Script: Execute the script to retrieve data from the ChEMBL database.
View Results: The results will be displayed as a Pandas DataFrame, containing details such as the ChEMBL ID, compound name, molecular structure, and properties.
