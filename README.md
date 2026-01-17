# 🎤 AI-Driven Automated Interviewer for Project Presentations

An AI system that **listens to a student presenting a project (screen + speech)**, conducts an **adaptive technical interview**, and produces a **structured evaluation report** covering technical depth, clarity, originality, and implementation understanding.

This project was built as a solution to **Challenge 1: AI-Driven Automated Interviewer for Project Presentations**.

---

## 🚀 Problem Statement

Students often struggle to articulate:
- Their technical decisions
- Architectural trade-offs
- Depth of implementation understanding

Traditional interviews are:
- Manual
- Subjective
- Not scalable

This project automates the **first-round technical interview** using **AI-driven multimodal understanding**.

---

## 🧠 Solution Overview

The system:
1. **Ingests presentation content** (screen, slides, images, PDFs)
2. **Transcribes live or uploaded speech**
3. **Understands project context**
4. **Asks adaptive, context-aware interview questions**
5. **Evaluates responses using a scoring rubric**
6. **Generates structured feedback**

---

## ✨ Key Features

### 🔍 Presentation Understanding
- OCR on images / slides
- PDF & PPT text extraction
- Code snippet detection from screen content
- Speech-to-Text (STT) transcription

### 🤖 Dynamic Interviewing
- Context-aware question generation
- Follow-up questions based on user answers
- Interview flow managed via session state

### 📊 Evaluation & Feedback
Scores the candidate on:
- **Technical Depth**
- **Clarity of Explanation**
- **Originality**
- **Understanding of Implementation**
- **Confidence & Communication (speech cadence)**

Outputs:
- Final score breakdown
- Qualitative feedback summary

### 🌐 Frontend Demo
- Browser-based UI
- Upload image / audio / PDF
- Live interview experience via WebSocket

---

## 🏗️ Architecture

