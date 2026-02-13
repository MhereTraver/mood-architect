# ✅ Submission Checklist

Use this checklist to ensure you've completed all requirements before submitting.

## 1. Code Repository ✓

- [ ] **Public GitHub repository created**
  - URL: https://github.com/MhereTraver/mood-architect
  - Repository is public (not private)
  - All code is committed and pushed

- [ ] **Repository contains all required files:**
  - [ ] `README.md` with all required sections
  - [ ] `backend/main.py` with FastAPI application
  - [ ] `backend/requirements.txt` with dependencies
  - [ ] `frontend/` folder with React app
  - [ ] `.gitignore` files (no secrets committed!)
  - [ ] `.env.example` files (not actual `.env` files)

## 2. Backend Requirements ✓

- [ ] **Framework & Language:**
  - [ ] Using Python
  - [ ] Using FastAPI (or Flask/Django)
  - [ ] Code is well-structured

- [ ] **API Endpoint:**
  - [ ] POST `/api/affirmation` endpoint exists
  - [ ] Accepts JSON: `{ name: string, feeling: string }`
  - [ ] Returns JSON: `{ affirmation: string }`
  - [ ] Endpoint works correctly

- [ ] **OpenAI Integration:**
  - [ ] Calls OpenAI API (no hardcoded responses)
  - [ ] Uses GPT model (gpt-3.5-turbo or gpt-4)
  - [ ] Prompt generates therapeutic affirmations
  - [ ] Affirmations are personalized to user input

- [ ] **Security:**
  - [ ] API key stored ONLY in environment variable
  - [ ] No secrets in code or Git history
  - [ ] `.env` file is in `.gitignore`

- [ ] **Error Handling:**
  - [ ] Returns meaningful HTTP status codes
  - [ ] 400 for validation errors
  - [ ] 502/504 for API failures
  - [ ] No raw stack traces exposed to frontend
  - [ ] Graceful handling of OpenAI API errors

- [ ] **Input Validation:**
  - [ ] Validates name is not empty
  - [ ] Validates feeling is not empty
  - [ ] Proper error messages for invalid input

- [ ] **Safety Measures:**
  - [ ] System prompt includes safety guidelines
  - [ ] No medical/legal advice
  - [ ] Self-harm detection with supportive response
  - [ ] Responses kept short (2-4 sentences)

## 3. Frontend Requirements ✓

- [ ] **Framework:**
  - [ ] Using React, Next.js, Vite, or Vue
  - [ ] Modern JavaScript practices
  - [ ] Clean code structure

- [ ] **UI Elements:**
  - [ ] Clean, responsive interface
  - [ ] Name input field
  - [ ] Feeling input (text or presets)
  - [ ] Generate button
  - [ ] Result display area
  - [ ] Loading state indicator

- [ ] **User Experience:**
  - [ ] Interface is intuitive
  - [ ] Mobile-friendly/responsive design
  - [ ] Visual feedback for actions
  - [ ] Smooth transitions/animations (bonus)

- [ ] **Error Handling:**
  - [ ] Displays user-friendly error messages
  - [ ] No blank screens on errors
  - [ ] No raw stack traces visible
  - [ ] Handles network failures gracefully

- [ ] **API Integration:**
  - [ ] Frontend calls deployed backend
  - [ ] Not calling localhost in production
  - [ ] Proper error handling for API calls

## 4. Deployment ✓

- [ ] **Frontend Deployed:**
  - [ ] Live URL works: ___________________________
  - [ ] Hosted on Vercel, Netlify, or similar
  - [ ] No console errors in browser
  - [ ] Interface loads correctly

- [ ] **Backend Deployed:**
  - [ ] Live URL works: ___________________________
  - [ ] Hosted on Render, Railway, or similar
  - [ ] Health endpoint accessible
  - [ ] API endpoint responds correctly

- [ ] **Integration:**
  - [ ] Frontend calls deployed backend
  - [ ] CORS configured correctly
  - [ ] Frontend URL allowed in backend CORS
  - [ ] End-to-end flow works

- [ ] **Testing:**
  - [ ] Can generate affirmations successfully
  - [ ] Error messages display correctly
  - [ ] Loading states work
  - [ ] Works on mobile browsers

## 5. Environment Variables ✓

- [ ] **Backend Environment Variables:**
  - [ ] `OPENAI_API_KEY` set in hosting provider
  - [ ] `FRONTEND_URL` set for CORS
  - [ ] Screenshot taken (with secret blurred)

- [ ] **Frontend Environment Variables:**
  - [ ] `VITE_API_URL` set in hosting provider
  - [ ] Points to deployed backend URL
  - [ ] Screenshot taken

- [ ] **Security:**
  - [ ] No secrets committed to GitHub
  - [ ] `.env` files in `.gitignore`
  - [ ] `.env.example` files show format only

## 6. Documentation ✓

- [ ] **README.md includes:**
  - [ ] Project description
  - [ ] Tech stack listed
  - [ ] Live URLs (frontend and backend)
  - [ ] Local setup instructions
  - [ ] How to run frontend locally
  - [ ] How to run backend locally
  - [ ] Required environment variables (examples)
  - [ ] Deployment instructions
  - [ ] Future improvements section (2-5 bullets)

- [ ] **Code Quality:**
  - [ ] Code is readable and well-organized
  - [ ] Comments where necessary
  - [ ] Follows best practices
  - [ ] No debugging code left in

## 7. Prompt & Safety ✓

- [ ] **System Prompt:**
  - [ ] Empathetic and supportive tone
  - [ ] No medical/legal advice clause
  - [ ] No diagnosis instructions
  - [ ] Self-harm safety measures
  - [ ] Short response requirement (2-4 sentences)
  - [ ] Personalization instructions

- [ ] **Testing Safety:**
  - [ ] Tested with normal feelings - works well
  - [ ] Tested with self-harm keywords - safe response
  - [ ] Responses are appropriate and supportive
  - [ ] No harmful content generated

## 8. Submission Package ✓

- [ ] **URLs to Submit:**
  - GitHub Repository: ___________________________
  - Live Frontend: ___________________________
  - Live Backend: ___________________________

- [ ] **Screenshots:**
  - [ ] Render environment variables (secret blurred)
  - [ ] Vercel environment variables
  - [ ] Working application (optional)

- [ ] **Improvements Note:**
  - [ ] Written 2-5 bullet points
  - [ ] Thoughtful and realistic
  - [ ] Shows understanding of potential

## 9. Final Testing ✓

Before submitting, test EVERYTHING:

- [ ] **Open incognito/private window**
- [ ] **Visit your live frontend URL**
- [ ] **Test Case 1: Happy Path**
  - [ ] Enter name: "Test User"
  - [ ] Select feeling: "Anxious"
  - [ ] Click generate
  - [ ] Wait for response
  - [ ] Verify affirmation appears
  - [ ] Verify it's personalized

- [ ] **Test Case 2: Custom Feeling**
  - [ ] Select "Something else..."
  - [ ] Enter custom feeling
  - [ ] Generate
  - [ ] Verify it works

- [ ] **Test Case 3: Error Handling**
  - [ ] Try empty name
  - [ ] Try empty feeling
  - [ ] Verify error messages appear

- [ ] **Test Case 4: Mobile**
  - [ ] Test on mobile browser
  - [ ] Verify responsive design
  - [ ] Verify functionality works

## 10. Common Gotchas to Check ✓

- [ ] No trailing slash in API URL
- [ ] CORS includes your frontend domain
- [ ] Environment variables saved in hosting provider
- [ ] Both services are "Live" (not sleeping)
- [ ] HTTPS (not HTTP) for production URLs
- [ ] No localhost URLs in production code
- [ ] .env files not committed to Git
- [ ] Screenshots show environment config (secrets blurred)

## Submission Confirmation

When ALL boxes above are checked:

**I confirm that:**
- [ ] My application is live and working
- [ ] I have tested all functionality
- [ ] All code is committed to GitHub
- [ ] Environment variables are configured correctly
- [ ] I have screenshots of environment configuration
- [ ] README is complete with all required information
- [ ] My submission includes future improvements

**Ready to Submit!** 🚀

---

## What to Submit

Email or submit:
1. **GitHub Repository URL**
2. **Live Frontend URL**
3. **Live Backend URL**
4. **Screenshot(s)** of environment variable configuration
5. **Brief note** (2-5 bullets) on what you'd improve with more time

---

## After Submission

**Keep your app running!** 

The reviewer will test your live URLs, so:
- Don't delete the Render/Vercel deployments
- Keep your OpenAI API key active
- Monitor for any issues

**Good luck!** 🍀
