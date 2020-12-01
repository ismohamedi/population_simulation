from fastapi import FastAPI
from simulation.tasks import run_simulation

app = FastAPI(title="Population Growth Simulation")

@app.post("/simulate", tags=['Run simulation'])
async def simulate():
    return run_simulation()