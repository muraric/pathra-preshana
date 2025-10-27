#!/bin/bash
# Quick deployment checklist

echo "🚀 Pathra Preshana Deployment Checklist"
echo "========================================"
echo ""

echo "✅ Step 1: Update requirements.txt"
echo "   Added gunicorn for production server"
echo ""

echo "✅ Step 2: Create Procfile"
echo "   Created for Render/Railway deployment"
echo ""

echo "📋 Step 3: Choose a platform:"
echo "   🌟 Render.com (Recommended):"
echo "      • Free 750 hours/month"
echo "      • Go to: https://render.com"
echo "      • Create Web Service"
echo "      • Connect GitHub repo"
echo "      • Add environment variables"
echo ""
echo "   🚂 Railway.app:"
echo "      • Free $5 credit/month"
echo "      • Go to: https://railway.app"
echo ""
echo "   🛫 Fly.io:"
echo "      • 3 free shared VMs"
echo "      • Go to: https://fly.io"
echo ""

echo "📝 Step 4: Environment variables to add:"
echo "   GMAIL_USER=your_email@gmail.com"
echo "   GMAIL_APP_PASSWORD=your_app_password"
echo "   GOOGLE_CLIENT_ID=your_client_id"
echo "   GOOGLE_CLIENT_SECRET=your_secret"
echo "   SECRET_KEY=$(openssl rand -hex 32)"
echo "   DEBUG=False"
echo ""

echo "⚠️  Step 5: Important!"
echo "   1. Update Google Cloud Console OAuth settings"
echo "   2. Add your production URL to:"
echo "      - Authorized JavaScript origins"
echo "      - Authorized redirect URIs"
echo "   3. Wait 5-10 minutes after deploying"
echo ""

echo "✅ Ready to deploy!"
echo ""
echo "📖 Full guide: DEPLOYMENT_GUIDE.md"

