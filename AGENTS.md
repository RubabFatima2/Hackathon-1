# AGENTS.md — Todo App Hackathon II

## Purpose
This project uses Spec-Driven Development (SDD).
No agent may write code until a spec exists and is approved.

Pipeline: Specify → Plan → Tasks → Implement

## Rules (all agents must obey)
1. Never generate code without a referenced Task ID from speckit.tasks
2. Never modify architecture without updating specs/plan.md
3. Every code file must have a comment: # Task: T-XXX
4. If spec is missing or unclear — STOP and ask, never improvise
5. No manual coding — all implementation goes through Claude Code

## Spec File Locations
- specs/constitution.md   → WHY (principles, constraints)
- specs/specify.md        → WHAT (requirements, user stories)
- specs/plan.md           → HOW (architecture, components)
- specs/tasks.md          → BREAKDOWN (atomic task list)

## Tech Stack (Phase I)
- Python 3.13+
- UV (package manager)
- In-memory storage only (no database)
- Console/CLI interface

## Hierarchy (on conflict)
Constitution > Specify > Plan > Tasks