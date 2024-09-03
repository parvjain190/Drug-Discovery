from chembl_webresource_client.new_client import new_client
import pandas as pd

# Initialize the ChEMBL client
molecule = new_client.molecule

# Search for molecules by a keyword (e.g., "aspirin")
results = molecule.filter(pref_name__icontains="aspirin").only(['molecule_chembl_id','pref_name','molecule_structures',
                                                                'molecule_properties'])

# Convert the results to a pandas DataFrame
df = pd.DataFrame.from_records(results)

# Display the fetched data
print(df.head())
