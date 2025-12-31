#!/usr/bin/env python3
"""
Bolt21 Twitter Marketing Bot
Posts daily tweets about Bitcoin, Lightning Network, and Bolt21 features.
"""

import os
import json
import random
import tweepy
from datetime import datetime
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Paths
SCRIPT_DIR = Path(__file__).parent
TWEETS_FILE = SCRIPT_DIR / 'tweets' / 'tweets.json'
IMAGES_DIR = SCRIPT_DIR / 'images'
STATE_FILE = SCRIPT_DIR / 'state.json'


def get_twitter_client():
    """Initialize Twitter API v2 client with media upload support."""
    # V1.1 auth for media upload
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api_v1 = tweepy.API(auth)

    # V2 client for tweeting
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    return client, api_v1


def load_tweets():
    """Load tweets from JSON file."""
    with open(TWEETS_FILE, 'r') as f:
        return json.load(f)


def load_state():
    """Load posting state (which tweets have been posted)."""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {'posted_ids': [], 'last_posted': None}


def save_state(state):
    """Save posting state."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_next_tweet(tweets, state):
    """Get the next unposted tweet."""
    posted_ids = set(state.get('posted_ids', []))

    # Filter unposted tweets
    unposted = [t for t in tweets if t['id'] not in posted_ids]

    if not unposted:
        # All tweets posted, reset and start over
        print("All 365 tweets posted! Resetting cycle...")
        state['posted_ids'] = []
        unposted = tweets

    # Pick a random unposted tweet (adds variety)
    return random.choice(unposted)


def format_tweet(tweet):
    """Format tweet text with hashtags."""
    text = tweet['text']

    # Add hashtags if they fit
    hashtags = tweet.get('hashtags', [])
    if hashtags:
        hashtag_str = ' ' + ' '.join(f'#{tag}' for tag in hashtags)
        if len(text) + len(hashtag_str) <= 280:
            text += hashtag_str

    return text


def post_tweet(client, api_v1, tweet):
    """Post a tweet, optionally with an image."""
    text = format_tweet(tweet)
    media_ids = None

    # Upload image if specified
    image_path = tweet.get('image')
    if image_path:
        full_path = IMAGES_DIR / image_path
        if full_path.exists():
            print(f"Uploading image: {full_path}")
            media = api_v1.media_upload(str(full_path))
            media_ids = [media.media_id]
        else:
            print(f"Warning: Image not found: {full_path}")

    # Post the tweet
    response = client.create_tweet(text=text, media_ids=media_ids)
    return response


def main():
    """Main bot execution."""
    print(f"=== Bolt21 Twitter Bot ===")
    print(f"Time: {datetime.now().isoformat()}")

    # Validate credentials
    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        print("Error: Missing Twitter API credentials!")
        print("Set TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET")
        return 1

    # Load data
    tweets = load_tweets()
    state = load_state()

    print(f"Total tweets: {len(tweets)}")
    print(f"Already posted: {len(state.get('posted_ids', []))}")

    # Get and post next tweet
    tweet = get_next_tweet(tweets, state)
    print(f"\nPosting tweet #{tweet['id']} ({tweet['category']}):")
    print(f"  {tweet['text'][:100]}...")

    try:
        client, api_v1 = get_twitter_client()
        response = post_tweet(client, api_v1, tweet)

        # Update state
        state['posted_ids'].append(tweet['id'])
        state['last_posted'] = {
            'id': tweet['id'],
            'timestamp': datetime.now().isoformat(),
            'tweet_id': response.data['id']
        }
        save_state(state)

        print(f"\nSuccess! Tweet ID: {response.data['id']}")
        print(f"Remaining tweets: {len(tweets) - len(state['posted_ids'])}")

    except tweepy.TweepyException as e:
        print(f"\nError posting tweet: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
