# Bolt21 Twitter Bot - Launch Checklist

Quick guide to get the bot live when you're ready.

---

## Pre-Launch (5 minutes)

### Step 1: Get Twitter API Credentials

1. Go to [developer.twitter.com](https://developer.twitter.com/)
2. Sign in with the @Bolt21App Twitter account
3. Create a new **Project** → then create an **App** inside it
4. Under **User authentication settings**:
   - Enable **Read and Write** permissions
   - Set App Type to **Web App**
   - Add any callback URL (e.g., `https://bolt21.com`)
5. Go to **Keys and Tokens** tab
6. Copy these 4 values:

| Credential | Where to find it |
|------------|------------------|
| API Key | Under "Consumer Keys" → API Key |
| API Secret | Under "Consumer Keys" → API Key Secret |
| Access Token | Under "Authentication Tokens" → Generate |
| Access Token Secret | Under "Authentication Tokens" → Generate |

---

### Step 2: Add Secrets to GitHub

1. Go to: https://github.com/CaliforniaHodl/Bolt21-twitter-bot/settings/secrets/actions
2. Click **New repository secret**
3. Add each secret:

```
TWITTER_API_KEY         → paste your API Key
TWITTER_API_SECRET      → paste your API Secret
TWITTER_ACCESS_TOKEN    → paste your Access Token
TWITTER_ACCESS_TOKEN_SECRET → paste your Access Token Secret
```

---

### Step 3: Enable GitHub Actions

1. Go to: https://github.com/CaliforniaHodl/Bolt21-twitter-bot/actions
2. If prompted, click **"I understand my workflows, go ahead and enable them"**

---

## Launch Day

The bot is now armed. It will automatically post:
- **When**: Daily at a random time between 7am-10am EST
- **What**: One tweet from the 365-tweet library
- **With**: Attached images when specified

---

## Test Before Going Live (Optional)

Want to verify it works before waiting for the schedule?

1. Go to **Actions** tab
2. Click **Daily Tweet** workflow
3. Click **Run workflow** → **Run workflow**
4. Watch it execute (takes 1-2 minutes)
5. Check Twitter for the post

**Note**: Manual runs skip the random delay and post immediately.

---

## Post-Launch Monitoring

### Check if it's working
- **Actions tab**: Green checkmarks = success
- **Twitter**: New post each morning

### If something breaks
1. Check Actions tab for red X
2. Click the failed run to see error details
3. Common fixes in README.md

---

## Quick Links

- [Bot Repo](https://github.com/CaliforniaHodl/Bolt21-twitter-bot)
- [Actions/Runs](https://github.com/CaliforniaHodl/Bolt21-twitter-bot/actions)
- [Secrets Settings](https://github.com/CaliforniaHodl/Bolt21-twitter-bot/settings/secrets/actions)
- [Twitter Developer Portal](https://developer.twitter.com/)

---

## That's It

Once secrets are added, the bot runs itself. No maintenance needed.

365 days of content. One tweet per day. Fully automated.
