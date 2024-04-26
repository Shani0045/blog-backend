import uvicorn as server
import sys
from argparse import ArgumentParser

from blog_backend.main import app

if __name__ == "__main__":
    server.run(
        "manage:app",
        reload=True,
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    )
