# 🔧 Troubleshooting Guide

Common issues and their solutions.

## Local Development Issues

### Backend Won't Start

**Error: "python: command not found" or "python is not recognized"**

**Solution:**
1. Python not installed or not in PATH
2. Reinstall Python, checking "Add Python to PATH"
3. On Windows, try `py` instead of `python`

**Error: "No module named 'fastapi'"**

**Solution:**
1. Virtual environment not activated
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Then: `pip install -r requirements.txt`

**Error: "OPENAI_API_KEY environment variable is required"**

**Solution:**
1. Create `.env` file in `backend/` folder
2. Add: `OPENAI_API_KEY=sk-your-key-here`
3. Restart the backend server

**Error: "Address already in use" or "Port 8000 is already allocated"**

**Solution:**
1. Another process is using port 8000
2. Find and kill it:
   - Windows: `netstat -ano | findstr :8000` then `taskkill /PID <PID> /F`
   - Mac/Linux: `lsof -ti:8000 | xargs kill -9`
3. Or change port in `main.py`: `port = int(os.getenv("PORT", 8001))`

### Frontend Won't Start

**Error: "npm: command not found"**

**Solution:**
1. Node.js not installed
2. Install from https://nodejs.org/
3. Restart your terminal

**Error: "Cannot find module 'react'"**

**Solution:**
1. Dependencies not installed
2. Run: `npm install` in the `frontend/` folder
3. Wait for installation to complete

**Error: "Port 5173 is already in use"**

**Solution:**
1. Another Vite dev server is running
2. Close other terminals
3. Or kill the process:
   - Windows: `netstat -ano | findstr :5173` then `taskkill /PID <PID> /F`
   - Mac/Linux: `lsof -ti:5173 | xargs kill -9`

### Connection Issues

**Error: "Unable to connect to service" in browser**

**Causes & Solutions:**

1. **Backend not running**
   - Check backend terminal - should show "Uvicorn running on..."
   - If not running, start it: `python main.py`

2. **Wrong backend URL**
   - Check `frontend/.env`
   - Should be: `VITE_API_URL=http://localhost:8000`
   - NO trailing slash!

3. **CORS issues**
   - Check browser console for CORS errors
   - Backend should allow `http://localhost:5173`
   - Restart backend after changing CORS settings

**Error: "Failed to fetch" or network errors**

**Solution:**
1. Check both servers are running
2. Backend: http://localhost:8000/health should return JSON
3. Frontend: http://localhost:5173 should load
4. Check firewall isn't blocking connections

### OpenAI API Issues

**Error: "API key is invalid"**

**Solution:**
1. Check your API key at https://platform.openai.com/api-keys
2. Copy the FULL key including `sk-`
3. Update `.env` file
4. Restart backend

**Error: "Insufficient credits" or "Rate limit exceeded"**

**Solution:**
1. Check your OpenAI usage: https://platform.openai.com/usage
2. Add credits to your account
3. Wait if you've hit rate limits (try again in 1 minute)

**Error: "Model not found" or "invalid model"**

**Solution:**
1. Check `main.py` - model name
2. Use `gpt-3.5-turbo` (most reliable)
3. Or `gpt-4` if you have access

## Deployment Issues

### Render (Backend) Issues

**Service won't deploy - Build fails**

**Causes & Solutions:**

1. **Wrong Python version**
   - Render uses Python 3.11 by default
   - Check your `requirements.txt` is compatible
   - Add `runtime.txt` with `python-3.11.0` if needed

2. **Dependencies won't install**
   - Check `requirements.txt` has no syntax errors
   - Verify all packages exist on PyPI
   - Try deploying with just core dependencies first

3. **Wrong build command**
   - Should be: `pip install -r requirements.txt`
   - Check Root Directory is set to `backend`

**Service deployed but shows "Service Unavailable"**

**Solution:**
1. Check Render logs for errors
2. Verify environment variables are set
3. Make sure start command is: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Service keeps sleeping/going offline**

**Solution:**
1. Free tier sleeps after 15 minutes of inactivity
2. First request after sleep takes 30-60 seconds
3. This is normal behavior - upgrade to paid tier to prevent sleeping

**Environment variables not working**

**Solution:**
1. Go to Dashboard → Environment
2. Click "Add Environment Variable"
3. Add key and value
4. Click "Save Changes"
5. **Important:** Manually redeploy after adding variables

### Vercel (Frontend) Issues

**Build fails**

**Causes & Solutions:**

1. **Wrong root directory**
   - Set Root Directory to `frontend`
   - Not the project root!

2. **Missing environment variable**
   - Add `VITE_API_URL` in Vercel dashboard
   - Settings → Environment Variables

3. **Build command error**
   - Default should be: `npm run build`
   - Output directory: `dist`

**Site deploys but shows blank page**

**Solution:**
1. Check browser console for errors
2. Verify `VITE_API_URL` is set correctly
3. Make sure you're using `import.meta.env.VITE_API_URL` in code
4. Redeploy after adding environment variables

**Getting 404 errors**

**Solution:**
1. Check Vercel deployment logs
2. Verify all files were included in build
3. Check `index.html` is at root of `frontend/` folder

### CORS Errors

**Error: "Access to fetch... has been blocked by CORS policy"**

**Symptoms:**
- Frontend loads fine
- Can see the form
- But affirmations won't generate
- Browser console shows CORS error

**Solutions:**

1. **Check backend allows your frontend URL**
   - In Render, add environment variable:
     - Key: `FRONTEND_URL`
     - Value: Your Vercel URL (e.g., `https://mood-architect.vercel.app`)
   - Redeploy backend

2. **Verify no trailing slash**
   - Frontend `.env`: `VITE_API_URL=https://your-backend.onrender.com`
   - NOT: `https://your-backend.onrender.com/`

3. **Check HTTPS vs HTTP**
   - Production should use HTTPS for both
   - Mixed content (HTTPS frontend calling HTTP backend) won't work

4. **Backend CORS configuration**
   - In `main.py`, verify CORS middleware includes your frontend URL
   - During development, `allow_origins=["*"]` is fine
   - For production, specify exact URLs

### API Calls Failing

**Error: 502 Bad Gateway or 504 Gateway Timeout**

**Causes & Solutions:**

1. **Backend is sleeping (Render free tier)**
   - Wait 30-60 seconds
   - Try again
   - First request wakes it up

2. **OpenAI API timeout**
   - Network issue between Render and OpenAI
   - Usually temporary
   - Try again in a few seconds

3. **Invalid API key in production**
   - Check Render environment variables
   - OPENAI_API_KEY should start with `sk-`
   - No extra spaces or quotes

**Error: 400 Bad Request**

**Solution:**
1. Check your input validation
2. Make sure name and feeling are being sent
3. Check backend logs in Render for specific error

## General Debugging Tips

### Check Browser Console
1. Open Developer Tools (F12)
2. Go to "Console" tab
3. Look for red errors
4. Copy error message for troubleshooting

### Check Backend Logs

**Locally:**
- Look at the terminal running `python main.py`
- Errors will appear in red

**On Render:**
1. Dashboard → Your service
2. Click "Logs" tab
3. Look for errors around the time of the issue

### Check Network Requests

1. Open Developer Tools (F12)
2. Go to "Network" tab
3. Generate an affirmation
4. Click on the `/api/affirmation` request
5. Check:
   - Request URL (correct backend?)
   - Request payload (data being sent?)
   - Response (what came back?)
   - Status code (200 = success, 4xx/5xx = error)

### Test Backend Directly

**Test health endpoint:**
```
https://your-backend.onrender.com/health
```
Should return: `{"status":"healthy",...}`

**Test with curl/Postman:**
```bash
curl -X POST https://your-backend.onrender.com/api/affirmation \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","feeling":"happy"}'
```

### Common "It worked locally but not in production"

1. **Environment variables not set in production**
   - Check Render/Vercel dashboard

2. **Using localhost URLs in production code**
   - Search for `localhost` in your code
   - Should use environment variables

3. **CORS not configured for production domain**
   - Add your production frontend URL to backend CORS

4. **API key not set in production**
   - Verify in Render environment variables

5. **Wrong backend URL in frontend**
   - Check `VITE_API_URL` in Vercel

## Still Stuck?

### Systematic Debugging:

1. **Verify basics**
   - [ ] Backend is "Live" on Render
   - [ ] Frontend deployed successfully on Vercel
   - [ ] Both URLs are accessible

2. **Test backend independently**
   - [ ] Visit `/health` endpoint
   - [ ] Use curl/Postman to test API

3. **Test frontend independently**
   - [ ] Does it load?
   - [ ] Any console errors?

4. **Test integration**
   - [ ] Can frontend reach backend?
   - [ ] Check Network tab in browser
   - [ ] Look for CORS errors

5. **Check environment**
   - [ ] All env vars set in Render
   - [ ] All env vars set in Vercel
   - [ ] Values are correct (no typos)

### Get Help

- **GitHub Issues**: Check if others have same problem
- **Render Docs**: https://render.com/docs
- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **OpenAI Docs**: https://platform.openai.com/docs

### Last Resort: Start Fresh

If everything is broken:

1. **Backend:**
   - Delete service on Render
   - Create new service
   - Set environment variables carefully
   - Redeploy

2. **Frontend:**
   - Delete project on Vercel
   - Reimport from GitHub
   - Set environment variables
   - Redeploy

## Prevention Tips

1. **Always commit and push changes**
   - Both Render and Vercel deploy from GitHub
   - If code isn't pushed, it won't deploy

2. **Test locally before deploying**
   - Make sure it works on your machine
   - Then deploy

3. **Double-check environment variables**
   - After setting them, verify they're saved
   - Redeploy if needed

4. **Keep it simple**
   - Start with basic functionality
   - Add features incrementally
   - Test after each change

5. **Monitor your deployments**
   - Check logs regularly
   - Watch for errors
   - Fix issues as they appear

---

Remember: Most issues are simple fixes!
- Check the logs
- Read the error message
- Google the exact error
- Try the solutions above

**You got this!** 💪
