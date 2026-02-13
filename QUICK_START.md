# ⚡ Quick Start Reference

**Save this page** - you'll use these commands every time you work on the project!

## 🎯 Most Common Commands

### Starting Development (Every Time)

**Step 1: Start Backend**
```bash
cd mood-architect/backend
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
python main.py
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8000"
🌐 Backend at: http://localhost:8000

**Step 2: Start Frontend** (New Terminal)
```bash
cd mood-architect/frontend
npm run dev
```
✅ Wait for: "Local: http://localhost:5173/"
🌐 Frontend at: http://localhost:5173

### Stopping Development

In each terminal:
```
Ctrl + C
```

## 📦 First Time Setup

### Initial Installation

**Clone/Create Project:**
```bash
cd Desktop
mkdir mood-architect
cd mood-architect
git init
```

**Backend Setup:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edit .env and add your OpenAI API key
```

**Frontend Setup:**
```bash
cd frontend
npm install
copy .env.example .env
# Default .env should work for local dev
```

## 🔑 Environment Variables

### Backend (.env file location: `backend/.env`)
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
FRONTEND_URL=http://localhost:5173
PORT=8000
```

### Frontend (.env file location: `frontend/.env`)
```bash
VITE_API_URL=http://localhost:8000
```

**Production (Render/Vercel):**
- Render: Add same backend variables
- Vercel: `VITE_API_URL=https://your-backend.onrender.com`

## 🔧 Common Tasks

### Add New Python Package
```bash
cd backend
venv\Scripts\activate
pip install package-name
pip freeze > requirements.txt
```

### Add New NPM Package
```bash
cd frontend
npm install package-name
```

### Update Dependencies
```bash
# Backend
cd backend
venv\Scripts\activate
pip install --upgrade -r requirements.txt

# Frontend
cd frontend
npm update
```

### View API Documentation
Start backend, then visit:
```
http://localhost:8000/docs
```

## 📤 Git Commands

### First Time Push
```bash
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/MhereTraver/mood-architect.git
git push -u origin main
```

### Regular Updates
```bash
git add .
git commit -m "Description of changes"
git push
```

### Check Status
```bash
git status
```

### View Commit History
```bash
git log --oneline
```

## 🚀 Deployment Commands

### Deploy to Render (Backend)
- Push to GitHub
- Render auto-deploys (if configured)
- Or: Manual Deploy button in Render dashboard

### Deploy to Vercel (Frontend)
- Push to GitHub
- Vercel auto-deploys
- Or: `vercel` command if CLI installed

## 🧪 Testing Endpoints

### Test Backend Health
```bash
# Browser or curl
http://localhost:8000/health
```

### Test Affirmation Generation
```bash
curl -X POST http://localhost:8000/api/affirmation \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test\",\"feeling\":\"happy\"}"
```

## 🐛 Quick Fixes

### Backend Won't Start
```bash
# Make sure venv is activated
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt

# Check .env file exists with API key
```

### Frontend Won't Start
```bash
# Reinstall dependencies
rm -rf node_modules
npm install

# Clear cache
npm run dev -- --force
```

### Port Already in Use
```bash
# Windows - Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID [PID_NUMBER] /F

# Or change port in backend/.env
PORT=8001
```

### CORS Errors
```bash
# Check frontend .env has correct backend URL
# Check backend main.py allows frontend URL
# Restart both servers after changes
```

## 📍 URLs Reference

### Local Development
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

### Production (Update These!)
- Frontend: https://your-app.vercel.app
- Backend: https://your-app.onrender.com
- API Docs: https://your-app.onrender.com/docs

## 🔍 Log Locations

### Local
- Backend: Terminal running `python main.py`
- Frontend: Terminal running `npm run dev`
- Browser: F12 → Console tab

### Production
- Render: Dashboard → Logs tab
- Vercel: Dashboard → Deployments → Function logs
- Browser: F12 → Console & Network tabs

## ⌨️ Keyboard Shortcuts

**Browser (Testing):**
- `F12` - Open Developer Tools
- `Ctrl + Shift + C` - Inspect Element
- `Ctrl + Shift + R` - Hard Reload (clear cache)

**Terminal:**
- `Ctrl + C` - Stop running server
- `Ctrl + L` - Clear terminal
- `↑` Arrow - Previous command

**VS Code:**
- `Ctrl + ~` - Toggle Terminal
- `Ctrl + B` - Toggle Sidebar
- `Ctrl + P` - Quick File Open
- `Ctrl + Shift + F` - Search in Files

## 📂 Project Structure

```
mood-architect/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── requirements.txt      # Python dependencies
│   ├── .env                 # Your secrets (git ignored)
│   ├── .env.example         # Example secrets
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Main component
│   │   ├── App.css          # Styles
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Global styles
│   ├── index.html           # HTML template
│   ├── package.json         # NPM config
│   ├── vite.config.js       # Vite config
│   ├── .env                 # Frontend config
│   └── .gitignore
├── README.md                # Main documentation
├── DEPLOYMENT.md            # Deployment guide
├── WINDOWS_SETUP.md         # Windows setup guide
├── TROUBLESHOOTING.md       # Common issues
└── .gitignore              # Root gitignore
```

## 🎓 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com/tutorial/
- **React**: https://react.dev/learn
- **Vite**: https://vitejs.dev/guide/
- **OpenAI API**: https://platform.openai.com/docs
- **Render**: https://render.com/docs
- **Vercel**: https://vercel.com/docs

## ✅ Daily Checklist

**Before You Start Coding:**
- [ ] Pull latest changes: `git pull`
- [ ] Start backend server
- [ ] Start frontend server
- [ ] Test in browser: http://localhost:5173

**Before You Stop:**
- [ ] Stop both servers (Ctrl+C)
- [ ] Commit changes: `git add . && git commit -m "..."`
- [ ] Push to GitHub: `git push`

**Before Submitting:**
- [ ] Test locally
- [ ] Push to GitHub
- [ ] Check deployments are live
- [ ] Test production URLs
- [ ] Review checklist in SUBMISSION_CHECKLIST.md

---

**💡 Pro Tip:** Bookmark this page! You'll reference it constantly.

**Need more help?** Check these guides:
- 🪟 Windows setup: `WINDOWS_SETUP.md`
- 🚀 Deployment: `DEPLOYMENT.md`
- 🔧 Troubleshooting: `TROUBLESHOOTING.md`
- ✅ Submission: `SUBMISSION_CHECKLIST.md`
