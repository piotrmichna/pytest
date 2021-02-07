import pytest

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
    assert twitter
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweets == []


@pytest.mark.parametrize('message, expected', (
        ('Test #first message', ['first']),
        ('#first Test message', ['first']),
        ('#FIRST Test message', ['FIRST']),
        ('Test message #FIRST', ['FIRST']),
        ('Test message #FIRST', ['first', 'second']),
))
def test_tweet_with_hashtag(message, expected):
    twitter = Twitter()
    assert twitter.find_hashtags(message) == expected


# PONIŻSZE 3 TESTY ROBIĄ TO SAMO CO 1 POWYŻSZY
def test_tweet_with_hashtag():
    twitter = Twitter()
    message = 'Test #first message'
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)


def test_tweet_hashtag_on_beginning():
    twitter = Twitter()
    message = '#first Test message'
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)


def test_tweet_hashtag_on_uppercase():
    twitter = Twitter()
    message = '#FIRST Test message'
    twitter.tweet(message)
    assert 'FIRST' in twitter.find_hashtags(message)
