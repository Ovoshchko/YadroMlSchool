from typing import List
from rdkit import Chem
from src.molecular.rdkit_functions import substructure_search
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://user:password@localhost/db"

Base = declarative_base()

class Molecule(Base):
    __tablename__ = 'molecules'
    id = Column(Integer, primary_key=True)
    identifier = Column(String, unique=True)
    smiles = Column(String)


class MoleculeService:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_molecule(self, smiles: str, identifier: str):
        session = self.Session()
        if session.query(Molecule).filter_by(identifier=identifier).first():
            session.close()
            raise ValueError("Molecule with this identifier already exists")
        molecule = Chem.MolFromSmiles(smiles)
        if not molecule:
            session.close()
            raise ValueError("Invalid SMILES string")
        new_molecule = Molecule(identifier=identifier, smiles=smiles)
        session.add(new_molecule)
        session.commit()
        session.close()

    def get_molecule(self, identifier: str):
        session = self.Session()
        molecule = session.query(Molecule).filter_by(identifier=identifier).first()
        session.close()
        return molecule.smiles if molecule else None

    def update_molecule(self, identifier: str, new_smiles: str):
        session = self.Session()
        molecule = session.query(Molecule).filter_by(identifier=identifier).first()
        if not molecule:
            session.close()
            raise ValueError("Molecule with this identifier does not exist")
        new_molecule = Chem.MolFromSmiles(new_smiles)
        if not new_molecule:
            session.close()
            raise ValueError("Invalid SMILES string")
        molecule.smiles = new_smiles
        session.commit()
        session.close()

    def delete_molecule(self, identifier: str):
        session = self.Session()
        molecule = session.query(Molecule).filter_by(identifier=identifier).first()
        if molecule:
            session.delete(molecule)
            session.commit()
        session.close()

    def list_molecules(self):
        session = self.Session()
        molecules = session.query(Molecule).all()
        session.close()
        return molecules

    def search_by_substructure(self, substructure: str) -> List[str]:
        smiles_list = [mol.smiles for mol in self.list_molecules()]
        identifiers = [mol.identifier for mol in self.list_molecules()]

        matching_smiles = substructure_search(smiles_list, substructure)

        return [
            identifier
            for identifier, smiles in zip(identifiers, smiles_list)
            if smiles in matching_smiles
        ]
