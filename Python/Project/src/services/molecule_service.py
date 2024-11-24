from typing import List
from rdkit import Chem

from molecular import substructure_search


class MoleculeService:
    def __init__(self):
        self.molecules = {}

    def add_molecule(self, smiles: str, identifier: str):
        if identifier in self.molecules:
            raise ValueError("Molecule with this identifier already exists")
        molecule = Chem.MolFromSmiles(smiles)
        if not molecule:
            raise ValueError("Invalid SMILES string")
        self.molecules[identifier] = smiles

    def get_molecule(self, identifier: str):
        return self.molecules.get(identifier)

    def update_molecule(self, identifier: str, new_smiles: str):
        if identifier not in self.molecules:
            raise ValueError("Molecule with this identifier does not exist")
        molecule = Chem.MolFromSmiles(new_smiles)
        if not molecule:
            raise ValueError("Invalid SMILES string")
        self.molecules[identifier] = new_smiles

    def delete_molecule(self, identifier: str):
        if identifier in self.molecules:
            del self.molecules[identifier]

    def list_molecules(self) -> List[dict]:
        return [{"identifier": id, "smiles": smiles} for id, smiles in self.molecules.items()]

    def search_by_substructure(self, substructure: str) -> List[str]:
        smiles_list = list(self.molecules.values())
        identifiers = list(self.molecules.keys())

        matching_smiles = substructure_search(smiles_list, substructure)

        return [
            identifier
            for identifier, smiles in zip(identifiers, smiles_list)
            if smiles in matching_smiles
        ]
