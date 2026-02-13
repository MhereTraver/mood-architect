# 🚀 Deployment Guide - Step by Step

This guide will walk you through deploying Mood Architect to production.

## Prerequisites Checklist

- [ ] GitHub account with the repository pushed
- [ ] OpenAI API key ([Get one](https://platform.openai.com/api-keys))
- [ ] Render account ([Sign up](https://render.com))
- [ ] Vercel account ([Sign up](https://vercel.com))

## Part 1: Deploy Backend to Render

### Step 1: Create Render Account
1. Go to https://render.com
2. Click "Get Started" or "Sign Up"
3. Sign up with GitHub (recommended for easy deployment)

### Step 2: Create New Web Service
1. Once logged in, click the "New +" button in the top right
2. Select "Web Service"
3. Click "Connect account" if you haven't connected GitHub
4. Find and select your `mood-architect` repository
5. Click "Connect"

### Step 3: Configure the Web Service
Fill in these settings:

**Basic Settings:**
- **Name**: `mood-architect-backend` (or any name you prefer)
- **Region**: Choose the region closest to your target users
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Instance Type:**
- Select "Free" (should be pre-selected)

### Step 4: Set Environment Variables
1. Scroll to "Environment Variables" section
2. Click "Add Environment Variable"
3. Add these variables:

| Key | Value |
|-----|-------|
| `OPENAI_API_KEY` | `sk-your-actual-openai-api-key` |
| `PORT` | `8000` |

**IMPORTANT**: 
- Do NOT share your actual API key
- Keep the Render dashboard open; you'll need to update FRONTEND_URL later

### Step 5: Deploy
1. Scroll to the bottom
2. Click "Create Web Service"
3. Wait for deployment (usually 2-5 minutes)
4. Once complete, you'll see "Live" with a green indicator

### Step 6: Get Your Backend URL
1. At the top of your service page, you'll see a URL like:
   `https://mood-architect-backend.onrender.com`
2. **COPY THIS URL** - you'll need it for the frontend
3. Test it by visiting: `https://your-backend-url.onrender.com/health`
   - You should see: `{"status":"healthy",...}`

## Part 2: Deploy Frontend to Vercel

### Step 1: Create Vercel Account
1. Go to https://vercel.com
2. Click "Sign Up"
3. Sign up with GitHub (recommended)

### Step 2: Import Project
1. Click "Add New..." → "Project"
2. Find your `mood-architect` repository
3. Click "Import"

### Step 3: Configure Project
**Important**: Before clicking "Deploy", configure these:

**Framework Preset:**
- Should auto-detect as "Vite" ✅

**Root Directory:**
- Click "Edit" next to Root Directory
- Enter: `frontend`
- Click "Continue"

**Build Settings:**
- Build Command: `npm run build` (auto-filled)
- Output Directory: `dist` (auto-filled)
- Install Command: `npm install` (auto-filled)

### Step 4: Add Environment Variable
1. Click "Environment Variables" dropdown
2. Add variable:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://your-backend-url.onrender.com` (the URL from Render)
   - Make sure there's NO trailing slash
3. Click "Add"

### Step 5: Deploy
1. Click "Deploy"
2. Wait 1-2 minutes for build and deployment
3. You'll see "Congratulations!" when done

### Step 6: Get Your Frontend URL
1. You'll see your production URL like:
   `https://mood-architect.vercel.app`
2. **COPY THIS URL**
3. Click "Visit" to test it (it might not work yet - we need to update CORS)

## Part 3: Update Backend CORS Settings

### Step 1: Go Back to Render
1. Open Render dashboard
2. Go to your `mood-architect-backend` service

### Step 2: Add Frontend URL to Environment Variables
1. Click "Environment" in the left sidebar
2. Click "Add Environment Variable"
3. Add:
   - **Key**: `FRONTEND_URL`
   - **Value**: `https://your-app.vercel.app` (your Vercel URL)
4. Click "Save Changes"

### Step 3: Redeploy Backend
1. The service should auto-redeploy
2. If not, click "Manual Deploy" → "Deploy latest commit"
3. Wait for it to become "Live" again

## Part 4: Testing the Live Application

### Step 1: Test the Frontend
1. Visit your Vercel URL
2. You should see the Mood Architect interface

### Step 2: Generate an Affirmation
1. Enter a name (e.g., "Alex")
2. Select a feeling (e.g., "Anxious")
3. Click "Generate Affirmation"
4. Wait a few seconds
5. You should see a personalized affirmation!

### Step 3: Test Error Handling
1. Try submitting without a name - should show error
2. Try with network disconnected - should show connection error

### Troubleshooting

**Frontend shows "Unable to connect to service"**
- Check that VITE_API_URL is correct in Vercel environment variables
- Ensure no trailing slash in the URL
- Verify backend is "Live" on Render

**Backend shows "OPENAI_API_KEY environment variable is required"**
- Check environment variables in Render
- Make sure you clicked "Save Changes"
- Redeploy the service

**CORS errors in browser console**
- Ensure FRONTEND_URL is set in Render
- Check that the URL matches exactly (including https://)
- Redeploy backend after adding FRONTEND_URL

**Backend goes to sleep (free tier)**
- Render free tier sleeps after 15 min of inactivity
- First request after sleep takes 30-60 seconds
- Consider upgrading for production use

## Part 5: Take Screenshots for Submission

### Screenshot 1: Render Environment Variables
1. Go to Render dashboard → Your service
2. Click "Environment" tab
3. Take screenshot showing:
   - OPENAI_API_KEY (blur/hide the actual value!)
   - FRONTEND_URL (visible is fine)
   - PORT (visible is fine)

### Screenshot 2: Vercel Environment Variables
1. Go to Vercel dashboard → Your project
2. Click "Settings" → "Environment Variables"
3. Take screenshot showing:
   - VITE_API_URL with your backend URL

## Part 6: Update README

1. Open your README.md file
2. Update the "Live Demo" section with your actual URLs:
   ```markdown
   - **Frontend**: https://your-actual-frontend.vercel.app
   - **Backend API**: https://your-actual-backend.onrender.com
   ```
3. Commit and push the change

## Final Checklist

- [ ] Backend is deployed and shows "Live" on Render
- [ ] Backend health check works: `/health` endpoint returns JSON
- [ ] Frontend is deployed on Vercel
- [ ] Frontend loads without errors
- [ ] Can generate affirmations successfully
- [ ] Error handling works (try invalid inputs)
- [ ] Environment variables are set correctly (screenshots taken)
- [ ] README updated with live URLs
- [ ] Both URLs are publicly accessible

## Common Issues & Solutions

**Issue**: "This site can't be reached"
- **Solution**: Check if service is "Live" on Render. Free tier sleeps after inactivity.

**Issue**: Slow initial load
- **Solution**: Free tier cold starts take 30-60s. This is normal.

**Issue**: API calls failing
- **Solution**: 
  1. Check browser console for CORS errors
  2. Verify environment variables in both platforms
  3. Ensure backend URL in Vercel has no trailing slash

**Issue**: OpenAI errors
- **Solution**: 
  1. Verify API key is valid and has credits
  2. Check OpenAI dashboard for rate limits
  3. Try a different OpenAI model if needed

## Monitoring Your Application

**Render Logs:**
- Dashboard → Your service → "Logs" tab
- Monitor for errors, API calls, startup messages

**Vercel Logs:**
- Dashboard → Your project → "Deployments" → Click deployment → "Functions"
- Check for build errors, runtime issues

## Updating Your Application

**To update the code:**
1. Make changes locally
2. Commit and push to GitHub
3. Vercel auto-deploys on push
4. Render auto-deploys on push (if enabled)

**To manually deploy:**
- **Render**: Click "Manual Deploy" → "Deploy latest commit"
- **Vercel**: Dashboard → Deployments → "Redeploy"

---

🎉 Congratulations! Your application is now live!
