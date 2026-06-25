# Build a Product Video in 2 Hours with Claude Code & Remotion - Live Demo & Tutorial

URL: https://www.youtube.com/watch?v=2riqInPzpTU

Demo Repo: https://github.com/specstoryai/zero-to-product-video-hero

Demo Blog Post: https://www.gregceccarelli.com/writing/build-product-video-with-ai

## Overview

This workspace is set up for managing multiple video rendering projects. Each project has its own git repository with a develop/main branch workflow.

## Structure

```
.
├── projects/          # Individual video projects (each with own git repo)
│   └── example-project/
├── templates/         # Shared templates and configurations
│   └── remotion-basic/
├── CLAUDE.md          # AI agent instructions
└── README.md          # This file
```

## Creating a New Project

1. Copy a template:
   ```bash
   cp -r templates/remotion-basic projects/my-new-project
   ```

2. Initialize git:
   ```bash
   cd projects/my-new-project
   git init
   git checkout -b main
   git add .
   git commit -m "Initial commit"
   git checkout -b develop
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start development:
   ```bash
   npm start
   ```

## Workflow

- All development work happens on the `develop` branch
- Changes are reviewed and approved before merging to `main`
- Each project maintains its own independent git history
