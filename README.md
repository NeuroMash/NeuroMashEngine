# 🧠 NeuroMesh

**NeuroMesh** is an early-stage experimental software project that explores how to build a distributed AI training system powered by idle GPUs from regular people around the world.

The goal is to let people train AI models cheaper by breaking them into small tasks that are sent to unused devices — like gaming PCs, laptops, or workstations.

Right now, I'm just getting started. This project is a learning process and an exploration — not a final product (yet).

---

## ⚙️ What This Will Eventually Do

- Let developers upload AI training jobs
- Split those jobs into small pieces using Python/Julia
- Send them to devices running a lightweight client (written in Rust)
- Collect the results and reassemble them
- Return the finished model to the original user

---

## 🧰 Current Components

| Folder | What it does |
|--------|---------------|
| `neuro_core/` | Code to split/merge AI jobs (Python + Julia) |
| `job_server/` | API that sends/receives jobs (Python FastAPI) |
| `device_client/` | Rust client that runs jobs on idle devices |
| `data/` | Temporary file storage |
| `docs/` | Architecture notes and planning |

---

## 📌 Status

🟡 *Still in early development. Nothing works yet. Building piece by piece.*

This repo is mainly for:
- Learning
- Experimenting
- Documenting the journey
- Getting feedback from other developers

---

## 🔒 License

This project is currently **closed source and not for public use**.

See [LICENSE.txt](LICENSE.txt) for full terms.
