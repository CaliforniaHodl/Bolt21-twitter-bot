# Bolt21 Twitter Marketing Bot

Automated Twitter/X marketing bot for Bolt21 Lightning Wallet. Posts daily content about Bitcoin self-custody, Lightning Network, and product features.

## Features

- **365 Pre-written Tweets**: One year of daily marketing content
- **Smart Scheduling**: Posts between 7am EST - 7pm PST (peak US hours)
- **Image Support**: Automatically attaches relevant images
- **Content Categories**:
  - Product features & announcements
  - Bitcoin education
  - Lightning Network explainers
  - Self-custody advocacy
  - Mining (Ocean pool) content
  - Blog post promotions
  - Engagement & community building

## Setup

### 1. Twitter API Credentials

Create a Twitter Developer account and get API keys:
- API Key
- API Secret
- Access Token
- Access Token Secret

### 2. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Manually

```bash
python bot.py
```

### 5. Deploy with GitHub Actions

The bot runs automatically via GitHub Actions. Add these secrets to your repo:
- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`

## Content Structure

Tweets are stored in `tweets/tweets.json` with the following format:

```json
{
  "id": 1,
  "category": "product",
  "text": "Tweet content here...",
  "image": "images/feature-bolt12.png",
  "hashtags": ["Bitcoin", "Lightning"],
  "posted": false
}
```

## Customization

- Edit `tweets/tweets.json` to modify content
- Add images to `images/` folder
- Adjust posting schedule in `.github/workflows/tweet.yml`

## License

Private - Bolt21
