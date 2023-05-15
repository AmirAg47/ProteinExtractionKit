




"""

!pip install biopython
!pip install nglview
from google.colab import output
output.enable_custom_widget_manager()
import nglview as nv
import urllib.request
from Bio.PDB import PDBParser

# Get protein ID from user
protein_id = input("Enter the PDB protein ID: ")

# URL of the protein structure file on the PDB database
url = f"https://files.rcsb.org/view/{protein_id}.pdb"

# Download the protein structure file
urllib.request.urlretrieve(url, "protein.pdb")

# Parse the PDB file using biopython
parser = PDBParser()
structure = parser.get_structure(protein_id, "protein.pdb")

# Extract the coordinates of the atoms in the structure
coordinates = []
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                coordinates.append(atom.get_coord())

# Create an nglview widget and add the protein structure to it
view = nv.show_structure_file("protein.pdb")
view.add_ball_and_stick()
view.center()

# Display the nglview widget
view

