from twitter import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message():
    twitter = Twitter()
    twitter.tweet('test' * 41)
    assert twitter.tweets == ['test' * 41]
