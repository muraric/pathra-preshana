# Google OAuth Setup Guide

## Error: 401 invalid_client - How to Fix

This error occurs when Google OAuth is not configured correctly. Follow these steps:

## Step 1: Go to Google Cloud Console

Visit: https://console.cloud.google.com/

Select your project (or create a new one).

## Step 2: Configure OAuth Client

1. Navigate to: **APIs & Services** → **Credentials**
2. Find your OAuth 2.0 Client ID
3. Click **Edit** to configure it

## Step 3: Add Authorized JavaScript Origins

In the "Authorized JavaScript origins" section, add:

```
http://localhost:5001
```

## Step 4: Add Authorized Redirect URIs

In the "Authorized redirect URIs" section, add:

```
http://localhost:5001/api/auth/google/callback
http://localhost:5001
```

## Step 5: Configure OAuth Consent Screen (CRITICAL!)

1. Go to: **OAuth consent screen**
2. Choose either:
   - **External** (for public use) - requires verification
   - **Internal** (for G Suite/Workspace users only)
3. Fill in required fields:
   - App name: Pathra Preshana
   - User support email: your_email@gmail.com
   - Developer contact: your_email@gmail.com
4. **Add Test Users** (if in testing mode):
   - Add your email address as a test user
5. **Publish** the app (or keep it in testing mode)

## Step 6: Enable Required APIs

Navigate to: **APIs & Services** → **Library**

Enable these APIs:
1. **Google+ API** (or Google People API)
2. Search for "People API" and enable it

## Step 7: Save and Wait

1. Click **Save** on your OAuth client configuration
2. Wait **1-2 minutes** for changes to propagate
3. Clear your browser cache

## Step 8: Verify Your Setup

Your configuration should look like this:

**OAuth Client Settings:**
- Your Client ID (from Google Cloud Console)
- Your Client Secret (from Google Cloud Console)

**Authorized JavaScript origins:**
- http://localhost:5001

**Authorized redirect URIs:**
- http://localhost:5001/api/auth/google/callback
- http://localhost:5001

## Common Issues

### Issue 1: "Error 403: access_denied"
**Solution:** Add your email as a test user in OAuth consent screen

### Issue 2: "Redirect URI mismatch"
**Solution:** Make sure the redirect URIs match exactly (including http:// vs https://)

### Issue 3: "OAuth consent screen not configured"
**Solution:** Complete step 5 above and publish your app

### Issue 4: "Invalid client"
**Solution:** 
- Verify the Client ID matches in both .env and Google Cloud Console
- Check that you're using the correct OAuth Client (not a service account)
- Ensure the APIs are enabled

## Testing

After configuration:
1. Visit: http://localhost:5001
2. Click "Sign in with Google"
3. You should see the Google sign-in popup
4. After signing in, you'll be redirected to the email interface

## Troubleshooting

If you still get errors:

1. **Check browser console** (F12) for any JavaScript errors
2. **Check server logs**: `/tmp/pathra-server.log`
3. **Verify Client ID** in .env matches Google Cloud Console
4. **Wait longer** - changes can take up to 5 minutes to propagate

## Quick Links

- Google Cloud Console: https://console.cloud.google.com/
- OAuth Consent Screen: https://console.cloud.google.com/apis/credentials/consent
- Credentials: https://console.cloud.google.com/apis/credentials
- API Library: https://console.cloud.google.com/apis/library

