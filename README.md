# Bolt21 Twitter Marketing Bot

Automated Twitter/X marketing bot that posts daily content about Bolt21, Bitcoin self-custody, and Lightning Network. One tweet per day, 365 days of content, fully automated.

## Quick Start

### 1. Get Twitter API Credentials

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new project and app
3. Enable **Read and Write** permissions
4. Generate these 4 credentials:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret

### 2. Add Secrets to GitHub

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these 4 secrets:

| Secret Name | Value |
|-------------|-------|
| `TWITTER_API_KEY` | Your API Key |
| `TWITTER_API_SECRET` | Your API Secret |
| `TWITTER_ACCESS_TOKEN` | Your Access Token |
| `TWITTER_ACCESS_TOKEN_SECRET` | Your Access Token Secret |

### 3. Enable GitHub Actions

1. Go to **Actions** tab in your repo
2. Click "I understand my workflows, go ahead and enable them"
3. The bot will now run automatically every day

That's it! The bot will post one tweet daily between 7-10am EST.

---

## How It Works

### Scheduling
- GitHub Actions triggers at **7am EST (12:00 UTC)** daily
- Bot waits a random 0-180 minutes before posting
- Result: tweets appear randomly between **7am-10am EST**

### Tweet Selection
- 365 pre-written tweets in `tweets/tweets.json`
- Bot picks a random unposted tweet each day
- Tracks which tweets have been posted in `state.json`
- After all 365 are posted, cycle restarts

### Content Categories
| Category | Count | Topics |
|----------|-------|--------|
| Product | ~60 | Bolt21 features, BOLT12, UX |
| Education | ~60 | Bitcoin basics, Lightning Network |
| Security | ~50 | Self-custody, key management |
| Mining | ~45 | Ocean pool, mining payouts |
| Hype | ~50 | Motivation, sovereignty |
| Milestones | ~10 | Day 100, 200, 300, 365 markers |

### Images
- Tweets reference images in the `images/` folder
- App screenshots, blog graphics, branding
- Bot automatically attaches images when posting

---

## Manual Operations

### Run Manually (Test)
```bash
# Clone the repo
git clone https://github.com/CaliforniaHodl/Bolt21-twitter-bot.git
cd Bolt21-twitter-bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TWITTER_API_KEY="your_key"
export TWITTER_API_SECRET="your_secret"
export TWITTER_ACCESS_TOKEN="your_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_token_secret"

# Run the bot
python bot.py
```

### Trigger via GitHub Actions
1. Go to **Actions** → **Daily Tweet**
2. Click **Run workflow**
3. Select branch and click **Run workflow**

This bypasses the random delay and posts immediately.

---

## Customization

### Edit Tweets
Modify `tweets/tweets.json`:

```json
{
  "id": 1,
  "category": "product",
  "text": "Your tweet text here (max 280 chars)",
  "image": "app-screenshot.png",
  "hashtags": ["Bitcoin", "Lightning"]
}
```

Fields:
- `id`: Unique number (1-365)
- `category`: For organization (product, education, security, mining, hype)
- `text`: Tweet content (keep under 250 chars to leave room for hashtags)
- `image`: Optional - filename in `images/` folder
- `hashtags`: Optional - added if they fit within 280 chars

### Add New Images
1. Add image to `images/` folder
2. Reference filename in tweet's `image` field
3. Commit and push

### Change Posting Time
Edit `.github/workflows/tweet.yml`:

```yaml
schedule:
  # Current: 7am EST (12:00 UTC)
  - cron: '0 12 * * *'
```

Adjust the cron schedule as needed. The random delay (0-180 min) is set in the workflow file.

### Change Random Window
Edit `.github/workflows/tweet.yml`:

```yaml
- name: Random delay
  run: |
    DELAY=$((RANDOM % 180))  # Change 180 to adjust window (in minutes)
```

---

## Monitoring

### Check Post History
The `state.json` artifact in GitHub Actions shows:
- Which tweet IDs have been posted
- Last post timestamp and tweet ID

### View Logs
1. Go to **Actions** tab
2. Click on a workflow run
3. Expand "Post tweet" step to see details

### Reset State (Start Over)
1. Go to **Actions** → find latest run with artifact
2. Delete the `tweet-state` artifact
3. Bot will start fresh from tweet pool

---

## Troubleshooting

### "Missing Twitter API credentials"
- Verify all 4 secrets are added in repo settings
- Check for typos in secret names

### "Rate limit exceeded"
- Twitter limits API calls
- Wait 15 minutes and try again
- The bot only posts once per day, so this shouldn't happen normally

### "Media upload failed"
- Check image exists in `images/` folder
- Verify image is under 5MB
- Ensure image format is PNG, JPG, or GIF

### Bot not posting
1. Check Actions tab for errors
2. Verify secrets are set correctly
3. Try manual trigger via workflow_dispatch

---

## File Structure

```
bolt21-twitter-bot/
├── .github/
│   └── workflows/
│       └── tweet.yml      # GitHub Actions schedule
├── images/
│   ├── app-screenshot.png
│   ├── blog/              # Blog post images
│   └── ...
├── tweets/
│   └── tweets.json        # All 365 tweets
├── bot.py                 # Main bot script
├── requirements.txt       # Python dependencies
├── .env.example          # Template for local testing
├── .gitignore
└── README.md
```

---

## License

Private - Bolt21

---

## Support

For issues with the bot, check the GitHub Actions logs first. For Twitter API issues, consult [Twitter Developer Documentation](https://developer.twitter.com/en/docs).
