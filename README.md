# 🕵️‍♂️ BlackBox Canary

A privacy-aware LLM chat logger built with FastAPI, Celery, Redis, and MongoDB — showcasing system design trade-offs and background job orchestration in modern AI-first systems.

---

## 🚀 Project Overview

`BlackBox Canary` is a backend system that captures and logs LLM interactions asynchronously, enriches them with PII detection and summarization, and persists them into MongoDB — all while demonstrating key distributed system design patterns.

---

## 🔍 Features

- ✅ FastAPI-based Chat Endpoint with OpenAI/Groq integration
- 📦 Background task processing using **Celery** and **Redis**
- 🧠 Enrichment pipeline:
  - ✅ Summarizes chats using `LLaMA3` via Groq API
  - 🔐 Detects PII (emails, phone numbers, etc.)
- 💾 Persists enriched data into **MongoDB**
- ⏱️ Celery retry patterns for reliability
- 📊 Flower dashboard for background job monitoring
- 🌐 REST API to retrieve chat history
- 🧪 Demonstrates background job orchestration, latency vs throughput tradeoffs

---

## 🧱 Tech Stack

| Component | Purpose |
|----------|---------|
| **FastAPI** | Web framework for chat API |
| **Celery** | Asynchronous task queue |
| **Redis** | Celery broker and result backend |
| **MongoDB** | Persistent chat log storage |
| **Groq API (LLaMA3)** | LLM used for chat + summarization |
