# 💻 Windows Setup Guide - Complete Walkthrough

This guide will help you set up and run Mood Architect on Windows from scratch.

## Part 1: Install Prerequisites (30 minutes)

### Step 1: Install Node.js

1. **Download Node.js:**
   - Open your browser and go to: https://nodejs.org/
   - Click the green button "Download Node.js (LTS)"
   - This downloads the Long Term Support version (recommended)

2. **Install Node.js:**
   - Find the downloaded file (likely in `Downloads` folder)
   - Double-click the installer file (`node-v20.x.x-x64.msi`)
   - Click "Next" through the installation wizard
   - **IMPORTANT**: Keep "Automatically install the necessary tools" checked
   - Click "Install"
   - Wait for installation to complete
   - Click "Finish"

3. **Verify Installation:**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter
   - In the black Command Prompt window, type:
     ```
     node --version
     ```
   - You should see something like `v20.11.0`
   - Then type:
     ```
     npm --version
     ```
   - You should see something like `10.2.4`

### Step 2: Install Python

1. **Download Python:**
   - Go to: https://www.python.org/downloads/
   - Click "Download Python 3.12.x" (or latest 3.11+)

2. **Install Python:**
   - Find the downloaded file in `Downloads`
   - Double-click the installer
   - **⚠️ CRITICAL**: Check the box "Add Python to PATH" at the bottom!
   - Click "Install Now"
   - Wait for installation
   - Click "Close"

3. **Verify Installation:**
   - Open a NEW Command Prompt (close the old one)
   - Press `Windows Key + R`, type `cmd`, press Enter
   - Type:
     ```
     python --version
     ```
   - You should see `Python 3.12.x` or `Python 3.11.x`
   - Type:
     ```
     pip --version
     ```
   - You should see `pip 24.x.x from ...`

**If Python commands don't work:**
- You forgot to check "Add Python to PATH"
- Uninstall Python (Control Panel → Programs → Uninstall)
- Reinstall and CHECK THE BOX!

### Step 3: Install Git

1. **Download Git:**
   - Go to: https://git-scm.com/download/win
   - Click "64-bit Git for Windows Setup"

2. **Install Git:**
   - Run the installer
   - Use all default settings (just click "Next" repeatedly)
   - Click "Install"
   - Click "Finish"

3. **Verify Installation:**
   - Open NEW Command Prompt
   - Type:
     ```
     git --version
     ```
   - You should see `git version 2.x.x`

### Step 4: Install VS Code (Optional but Recommended)

1. **Download:**
   - Go to: https://code.visualstudio.com/
   - Click "Download for Windows"

2. **Install:**
   - Run the installer
   - Check "Add to PATH"
   - Click through the installation

3. **Install Extensions:**
   - Open VS Code
   - Click the Extensions icon (4 squares) on the left sidebar
   - Search and install:
     - "Python" by Microsoft
     - "ESLint"
     - "Prettier - Code formatter"

## Part 2: Get the Project Code

### Step 1: Open Command Prompt

- Press `Windows Key + R`
- Type `cmd`
- Press Enter

### Step 2: Navigate to Desktop

```cmd
cd Desktop
```

### Step 3: Create Project Folder

```cmd
mkdir mood-architect
cd mood-architect
```

### Step 4: Initialize Git

```cmd
git init
git config user.name "YourGitHubUsername"
git config user.email "your-email@example.com"
```

Replace with your actual GitHub username and email.

## Part 3: Create the Project Structure

Now we'll create all the files. You can either:
- **Option A**: Use VS Code to create files (easier)
- **Option B**: Use Command Prompt

### Option A: Using VS Code

1. **Open VS Code in project folder:**
   ```cmd
   code .
   ```
   (If `code` command doesn't work, open VS Code and File → Open Folder → Select `mood-architect`)

2. **Create Backend Files:**
   - In VS Code Explorer, create new folder: `backend`
   - Inside `backend`, create these files (copy content from my previous messages):
     - `main.py`
     - `requirements.txt`
     - `.env.example`
     - `.gitignore`

3. **Create Frontend Files:**
   - Create new folder: `frontend`
   - Inside `frontend`, create:
     - `package.json`
     - `vite.config.js`
     - `index.html`
     - `.env.example`
     - `.gitignore`
   - Create folder `src` inside `frontend`
   - Inside `src`, create:
     - `main.jsx`
     - `App.jsx`
     - `App.css`
     - `index.css`

### Option B: Download from Repository

If you've already pushed to GitHub:
```cmd
git clone https://github.com/MhereTraver/mood-architect.git
cd mood-architect
```

## Part 4: Setup Backend

### Step 1: Navigate to Backend

```cmd
cd backend
```

### Step 2: Create Virtual Environment

```cmd
python -m venv venv
```

Wait for this to complete (creates a `venv` folder).

### Step 3: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

You should see `(venv)` at the start of your command line.

### Step 4: Install Dependencies

```cmd
pip install -r requirements.txt
```

Wait for all packages to install (may take 2-3 minutes).

### Step 5: Create .env File

1. **Copy the example:**
   ```cmd
   copy .env.example .env
   ```

2. **Edit .env file:**
   - If using VS Code, click on `.env` file
   - If using Notepad, type:
     ```cmd
     notepad .env
     ```

3. **Get OpenAI API Key:**
   - Go to: https://platform.openai.com/api-keys
   - Sign in or create account
   - Click "Create new secret key"
   - **IMPORTANT**: Copy the key immediately (you can't see it again!)
   - Paste it in your `.env` file:
     ```
     OPENAI_API_KEY=sk-proj-your-actual-key-here
     ```

4. **Save the file** (Ctrl+S in VS Code or File → Save in Notepad)

## Part 5: Setup Frontend

### Step 1: Open NEW Command Prompt

Don't close the backend terminal! Open a new one:
- Press `Windows Key + R`
- Type `cmd`
- Press Enter

### Step 2: Navigate to Frontend

```cmd
cd Desktop\mood-architect\frontend
```

### Step 3: Install Dependencies

```cmd
npm install
```

This will take 2-5 minutes. You'll see a progress bar.

### Step 4: Create .env File

```cmd
copy .env.example .env
```

The default values should work for local development:
```
VITE_API_URL=http://localhost:8000
```

## Part 6: Run the Application

Now you need BOTH terminals running simultaneously.

### Terminal 1: Backend

1. Make sure you're in the `backend` folder
2. Make sure virtual environment is activated (you see `(venv)`)
3. Run:
   ```cmd
   python main.py
   ```

You should see:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Leave this terminal running!**

### Terminal 2: Frontend

1. Make sure you're in the `frontend` folder
2. Run:
   ```cmd
   npm run dev
   ```

You should see:
```
  VITE v5.0.11  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**Leave this terminal running!**

### Step 3: Open the App

1. Your browser should automatically open
2. If not, open browser manually and go to:
   ```
   http://localhost:5173
   ```

3. You should see the Mood Architect interface!

## Part 7: Test the Application

1. **Enter your name**: e.g., "Alex"
2. **Select a feeling**: e.g., "Anxious"
3. **Click "Generate Affirmation"**
4. **Wait 2-3 seconds**
5. **You should see a personalized affirmation!**

### Common Issues:

**"Unable to connect to service"**
- Check backend terminal is still running
- Backend should show `http://0.0.0.0:8000`
- Try restarting backend

**"OpenAI API error"**
- Check your API key in `backend/.env`
- Make sure you have credits in OpenAI account
- Visit https://platform.openai.com/usage

**Backend won't start - "ModuleNotFoundError"**
- Make sure virtual environment is activated: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt`

**Frontend won't start - "npm not found"**
- Restart Command Prompt
- If still not working, reinstall Node.js

## Part 8: Stopping the Application

### To Stop:
1. Go to backend terminal
2. Press `Ctrl + C`
3. Go to frontend terminal
4. Press `Ctrl + C`

### To Restart Later:

**Backend:**
```cmd
cd Desktop\mood-architect\backend
venv\Scripts\activate
python main.py
```

**Frontend:**
```cmd
cd Desktop\mood-architect\frontend
npm run dev
```

## Part 9: Push to GitHub

### Step 1: Create Repository on GitHub

1. Go to https://github.com/MhereTraver
2. Click "Repositories"
3. Click green "New" button
4. Name: `mood-architect`
5. Description: "AI-powered therapeutic affirmation generator"
6. Make sure "Public" is selected
7. **DO NOT** check "Add a README"
8. Click "Create repository"

### Step 2: Push Your Code

In Command Prompt (in `mood-architect` folder):

```cmd
git add .
git commit -m "Initial commit - Mood Architect app"
git branch -M main
git remote add origin https://github.com/MhereTraver/mood-architect.git
git push -u origin main
```

If asked for credentials:
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password!)
  - Get token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token

## Next Steps

✅ Local development working
✅ Code pushed to GitHub
📝 Next: Deploy to production (see DEPLOYMENT.md)

---

## Quick Reference

**Start Development:**
```cmd
# Terminal 1 - Backend
cd Desktop\mood-architect\backend
venv\Scripts\activate
python main.py

# Terminal 2 - Frontend
cd Desktop\mood-architect\frontend
npm run dev
```

**URLs:**
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Stop Servers:**
- Press `Ctrl + C` in each terminal

---

Need help? Check:
- README.md for full documentation
- DEPLOYMENT.md for deployment guide
- API documentation at http://localhost:8000/docs
