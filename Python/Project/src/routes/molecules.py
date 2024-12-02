from os import getenv

from fastapi import APIRouter, HTTPException
from models import Molecule
from services import MoleculeService

molecule_router = APIRouter()
molecule_service = MoleculeService()


@molecule_router.get("/")
def get_server():
    return {"server_id": getenv("SERVER_ID", "1")}


@molecule_router.post("/molecules/")
def add_molecule(molecule: Molecule):
    try:
        molecule_service.add_molecule(molecule.smiles, molecule.id)
        return {"message": "Molecule added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@molecule_router.get("/molecules/{identifier}")
def get_molecule(identifier: str):
    molecule = molecule_service.get_molecule(identifier)
    if not molecule:
        raise HTTPException(status_code=404, detail="Molecule not found")
    return {"identifier": identifier, "smiles": molecule}


@molecule_router.put("/molecules/{identifier}")
def update_molecule(identifier: str, smiles: str):
    try:
        molecule_service.update_molecule(identifier, smiles)
        return {"message": "Molecule updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@molecule_router.delete("/molecules/{identifier}")
def delete_molecule(identifier: str):
    molecule_service.delete_molecule(identifier)
    return {"message": "Molecule deleted successfully"}


@molecule_router.get("/molecules/")
def list_molecules():
    return molecule_service.list_molecules()


@molecule_router.get("/molecules/search/")
def search_molecules(substructure: str):
    try:
        result = molecule_service.search_by_substructure(substructure)
        return {"matching_molecules": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
