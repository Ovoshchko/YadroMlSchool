import unittest
from src.molecular.rdkit_functions import substructure_search


class TestSubstructureSearch(unittest.TestCase):
    def test_valid_substructure(self):
        molecules = ["CCO", "CCC", "CC(C)O"]
        substructure = "CO"
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, ["CCO", "CC(C)O"])

    def test_no_matches(self):
        molecules = ["CCC", "CCCC", "CCCCC"]
        substructure = "CO"
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, [])

    def test_invalid_substructure(self):
        molecules = ["CCO", "CCC"]
        substructure = "invalid_smiles"
        with self.assertRaises(ValueError):
            substructure_search(molecules, substructure)

    def test_invalid_molecule_in_list(self):
        molecules = ["CCO", "invalid_smiles", "CCC"]
        substructure = "C"
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, ["CCO", "CCC"])

    def test_empty_molecule_list(self):
        molecules = []
        substructure = "C"
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, [])

    def test_empty_substructure(self):
        molecules = ["CCO", "CCC", "CC(C)O"]
        substructure = ""
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, [])

    def test_partial_matches(self):
        molecules = ["C", "CC", "CCC", "CCCC"]
        substructure = "C"
        result = substructure_search(molecules, substructure)
        self.assertEqual(result, ["C", "CC", "CCC", "CCCC"])
