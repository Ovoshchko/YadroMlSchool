from pydantic import BaseModel

class Molecule(BaseModel):
    smiles: str
    id: str
