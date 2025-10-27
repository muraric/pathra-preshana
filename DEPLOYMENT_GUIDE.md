# Deployment Guide - Pathra Preshana

## Free Hosting Options for Flask Apps

### 1. 🌟 **Render.com** (Recommended)
**Free Tier:**
- 750 hours/month free (enough for 24/7)
- Automatic HTTPS
- Environment variables support
- Easy Flask deployment

**Deployment Steps:**
1. Push your code to GitHub
2. Go to https://render.com
3. Create new "Web Service"
4. Connect your GitHub repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn pathra_preshana.app:app`
7. Add environment variables in Render dashboard
8. Deploy!

**Advantages:**
- ✅ Free for small apps
- ✅ Automatic SSL certificates
- ✅ Easy environment variable management
- ✅ Automatic deployments from GitHub

**Limitations:**
- Apps spin down after 15 minutes of inactivity
- Free tier has 512MB RAM

---

### 2. 🚂 **Railway.app**
**Free Tier:**
- $5 credit per month (free trial)
- Pay-as-you-go after that

**Deployment:**
1. Go to https://railway.app
2. Create new project from GitHub
3. Auto-detects Flask
4. Add environment variables
5. Deploy!

**Advantages:**
- ✅ Very easy setup
- ✅ No credit card required for small apps
- ✅ Fast deployments
- ✅ Automatic HTTPS

---

### 3. 🛫 **Fly.io**
**Free Tier:**
- 3 shared VMs free
- Good performance

**Deployment:**
```bash
# Install fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch
fly launch
fly secrets set GMAIL_USER=xxx
fly secrets set GMAIL_APP_PASSWORD=xxx
# ... add all env vars
```

**Advantages:**
- ✅ Good performance
- ✅ Global distribution
- ✅ Docker-based

---

### 4. ☁️ **PythonAnywhere**
**Free Tier:**
- Limited resources
- Python 3.x pre-installed

**Deployment:**
1. Sign up at https://www.pythonanywhere.com
2. Upload your code via web interface
3. Configure WSGI file
4. Set up environment variables
5. Run!

**Advantages:**
- ✅ Simple Python deployment
- ✅ Built-in Python environment

**Limitations:**
- ⚠️ Free tier has limited resources
- ⚠️ External URLs only

---

### 5. 🌐 **Glitch** (Not Recommended for Production)
**Free Tier:**
- Persistent hosting
- Live reload

**Best For:** Development/prototyping only

---

## Preparation Steps Before Deployment

### 1. Update Your Code

You'll need to make a few changes for production:

#### Add `gunicorn` to requirements.txt:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

#### Create a `Procfile` (for some platforms):
```
web: gunicorn pathra_preshana.app:app --bind 0.0.0.0:$PORT
```

Or a `runtime.txt` (for PythonAnywhere):
```
python-3.12.3
```

#### Update `app.py` for production:
At the bottom of `pathra_preshana/app.py`, change:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
```

To:
```python
if __name__ == '__main__':
    # Only for local development
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### 2. Update Google OAuth Settings

After deploying, update your Google Cloud Console:

1. Go to https://console.cloud.google.com
2. Navigate to: APIs & Services → Credentials
3. Edit your OAuth 2.0 Client
4. Add your production URL to:
   - **Authorized JavaScript origins:**
     - `https://your-app.onrender.com`
     - `https://your-app.railway.app` (or whichever platform)
   
   - **Authorized redirect URIs:**
     - `https://your-app.onrender.com/api/auth/google/callback`
     - `https://your-app.railway.app/api/auth/google/callback`

### 3. Set Environment Variables

On your hosting platform, add these environment variables:
- `GMAIL_USER`
- `GMAIL_APP_PASSWORD`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SECRET_KEY` (generate: `openssl rand -hex 32`)

---

## Recommended Approach

**For easiest deployment: Render.com**

Steps:
1. Add `gunicorn==21.2.0` to requirements.txt
2. Create `Procfile`:
   ```
   web: gunicorn pathra_preshana.app:app
   ```
3. Push to GitHub
4. Sign up at https://render.com
5. Create new Web Service
6. Connect GitHub repo
7. Add environment variables
8. Deploy!

---

## Troubleshooting

### Common Issues:

1. **Module not found errors:**
   - Make sure requirements.txt has all dependencies
   - Check that requirements.txt is in root directory

2. **OAuth redirect errors:**
   - Update Google Cloud Console with production URLs
   - Wait 5-10 minutes for changes to propagate

3. **Port binding errors:**
   - Use `os.environ.get('PORT', 5000)` for port
   - Gunicorn handles this automatically

4. **Database errors (if you add one later):**
   - Use SQLite for small projects (free)
   - Or use hosted databases like Supabase (free tier)

---

## Cost Comparison

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| **Render** | 750 hrs/month | ⭐ Best overall |
| **Railway** | $5 credit/month | Fast deploys |
| **Fly.io** | 3 VMs free | Performance |
| **PythonAnywhere** | Limited | Simple hosting |

---

## Next Steps After Deployment

1. **Update DNS** (if you want custom domain)
2. **Set up monitoring** (optional)
3. **Configure backups** (important!)
4. **Add analytics** (optional)
5. **Set up CI/CD** (automatic deployments)

Need help with any specific platform? Let me know!

