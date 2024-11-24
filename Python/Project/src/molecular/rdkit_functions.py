from rdkit import Chem

def substructure_search(molecules, substructure):
    substructure_mol = Chem.MolFromSmiles(substructure)

    if substructure_mol is None:
        raise ValueError("Invalid substructure SMILES string.")

    matching_molecules = []

    for smiles in molecules:
        molecule = Chem.MolFromSmiles(smiles)
        if molecule is None:
            continue

        if molecule.HasSubstructMatch(substructure_mol):
            matching_molecules.append(smiles)

    return matching_molecules

