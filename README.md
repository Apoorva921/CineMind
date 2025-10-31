#  CineMind — Multimodal AI for Movie Intelligence

CineMind is a FAANG-level AI project that analyzes Hollywood movie scenes using **video, audio, and text** to predict **audience engagement**, **emotional arcs**, and **trailer-worthy highlights**.

This system combines **Computer Vision**, **Audio Emotion Recognition**, and **NLP** into a unified AI dashboard built with **FastAPI** and **React**.

---

##  Backend Setup

The backend is built using **FastAPI** and provides REST endpoints for CineMind’s AI predictions.

### Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
