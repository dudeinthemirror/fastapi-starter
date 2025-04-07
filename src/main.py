from fastapi import FastAPI


# Create a new FastAPI app instance
app = FastAPI(description="FastAPI starter")


# -------------------------------
# ROUTES
# -------------------------------
@app.get("/")
def read_root():
    """
    Returns a simple "Up" status message
    """
    return {"status": "Up"}


@app.get("/list_agents")
def list_agents() -> dict:
    return {
        "agents": [
            {"name": "AG1", "description": "Agent 1"},
            {"name": "AG2", "description": "Agent 2"},
            {"name": "AG3", "description": "Agent 3"},
            {"name": "AG4", "description": "Agent 4"},
        ]
    }
