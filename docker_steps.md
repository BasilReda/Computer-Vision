
## 📋 steps to run docker

```

Requirements: Docker Desktop installed (any OS).

Steps to run:
1. Clone the repository.
2. Open a terminal in the repository root folder (AI-GYM-gym.v1/).
3. Run:
      docker compose up --build
4. Open http://localhost:5173 in your browser — the full app will be running.

Health check endpoint: http://localhost:8000/api/health → returns {"status":"ok"}

Docker automatically monitors the backend health and will only start the frontend after the backend is confirmed healthy.
```

---


## Useful Commands

```bash
# Run in background (detached mode)
docker compose up --build -d

# View live logs from both services
docker compose logs -f

# View logs of one service only
docker compose logs -f backend
docker compose logs -f frontend

# Stop everything
docker compose down

# Stop and also delete the images (full reset)
docker compose down --rmi all
```

---
