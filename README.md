# 🌟 Mood Architect

A full-stack AI-powered web application that generates personalized therapeutic affirmations using OpenAI's GPT model.

## 🔗 Live Demo

- **Frontend**: [https://your-app.vercel.app](https://your-app.vercel.app) _(Update after deployment)_
- **Backend API**: [https://your-app.onrender.com](https://your-app.onrender.com) _(Update after deployment)_

## 📋 Features

- ✨ AI-generated personalized affirmations
- 🎨 Clean, responsive UI with smooth animations
- 🛡️ Built-in safety measures (self-harm detection, no medical advice)
- ⚡ Real-time error handling with user-friendly messages
- 🔒 Secure environment variable management
- 📱 Mobile-friendly responsive design

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: Custom CSS with animations
- **Deployment**: Vercel

### Backend
- **Framework**: FastAPI (Python)
- **AI Integration**: OpenAI GPT-3.5-turbo
- **Deployment**: Render

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ ([Download](https://nodejs.org/))
- Python 3.11+ ([Download](https://www.python.org/downloads/))
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- Git ([Download](https://git-scm.com/))

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/MhereTraver/mood-architect.git
cd mood-architect
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env  # Windows
# OR
cp .env.example .env    # macOS/Linux

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-actual-api-key-here
```

#### 3. Frontend Setup

```bash
# Open a new terminal
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env file from example
copy .env.example .env  # Windows
# OR
cp .env.example .env    # macOS/Linux

# The default .env should work for local development
# VITE_API_URL=http://localhost:8000
```

#### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
python main.py
```

Backend will run on `http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Frontend will run on `http://localhost:5173`

Open your browser to `http://localhost:5173` to use the app!

## 🌐 Deployment

### Backend Deployment (Render)

1. **Create Render Account**: Go to [render.com](https://render.com) and sign up

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `mood-architect` repository

3. **Configure the Service**:
   - **Name**: `mood-architect-backend` (or your choice)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables**:
   - Click "Environment" tab
   - Add: `OPENAI_API_KEY` = `your-openai-api-key`
   - Add: `PORT` = `8000` (Render auto-sets this, but you can specify)

5. **Deploy**: Click "Create Web Service"

6. **Note Your Backend URL**: After deployment, copy your backend URL (e.g., `https://mood-architect-backend.onrender.com`)

### Frontend Deployment (Vercel)

1. **Install Vercel CLI** (optional):
```bash
npm install -g vercel
```

2. **Deploy via Vercel Website**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Configure:
     - **Framework Preset**: Vite
     - **Root Directory**: `frontend`
     - **Build Command**: `npm run build`
     - **Output Directory**: `dist`

3. **Add Environment Variable**:
   - In Vercel project settings → Environment Variables
   - Add: `VITE_API_URL` = `https://your-backend-url.onrender.com` (your Render backend URL)

4. **Deploy**: Vercel will auto-deploy

5. **Update Backend CORS**:
   - After getting your Vercel URL, go to Render
   - Update `FRONTEND_URL` environment variable to your Vercel URL
   - Redeploy the backend

### Post-Deployment

1. Test the live application
2. Update the README with your actual URLs
3. Take a screenshot of your environment variables in Render (blur the secret values)

## 📝 Required Environment Variables

### Backend (.env)
```bash
OPENAI_API_KEY=sk-your-openai-api-key-here
FRONTEND_URL=https://your-frontend-url.vercel.app
PORT=8000
```

### Frontend (.env)
```bash
VITE_API_URL=https://your-backend.onrender.com
```

## 🧪 API Documentation

Once the backend is running, visit:
- Local: `http://localhost:8000/docs`
- Production: `https://your-backend.onrender.com/docs`

### Main Endpoint

**POST** `/api/affirmation`

Request:
```json
{
  "name": "John",
  "feeling": "anxious about an upcoming presentation"
}
```

Response:
```json
{
  "affirmation": "John, it's completely natural to feel anxious before a big presentation. Your preparation and unique perspective are valuable, and you have the capability to share them effectively. Take a deep breath—you've got this."
}
```

## 🔒 Security Features

- ✅ API keys stored as environment variables (never in code)
- ✅ Input validation on both frontend and backend
- ✅ CORS properly configured
- ✅ Self-harm detection with supportive crisis messaging
- ✅ No medical/legal advice in AI responses
- ✅ Rate limiting ready (OpenAI handles this)
- ✅ Proper HTTP status codes for error handling

## 🎯 What I Would Improve With More Time

- **Enhanced Safety**: Implement more sophisticated content filtering using OpenAI's moderation API
- **User Accounts**: Add authentication to save affirmation history
- **Analytics**: Track usage patterns (anonymously) to improve prompts
- **A/B Testing**: Test different prompt variations for better affirmations
- **Accessibility**: Add ARIA labels, keyboard navigation, screen reader optimization
- **Rate Limiting**: Implement backend rate limiting to prevent abuse
- **Testing**: Add comprehensive unit tests, integration tests, and E2E tests
- **Internationalization**: Support multiple languages
- **Offline Mode**: Cache previous affirmations for offline access
- **Advanced Features**: 
  - Email/SMS delivery of daily affirmations
  - Voice input option
  - More customization (tone, length preferences)
  - Integration with mental health tracking apps

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Mhere Traver**
- GitHub: [@MhereTraver](https://github.com/MhereTraver)

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- React and FastAPI communities for excellent documentation
- Vercel and Render for free hosting tiers

---

Built with ❤️ as a technical challenge for Jr. AI Software Engineer position
