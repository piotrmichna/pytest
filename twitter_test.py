import pytest

from twitter import Twitter


@pytest.fixture
def twitter(request):
    # def twitter(scope='function') default <- cas życia indywidualnie dla każdej funkcji poniżej
    # scope=module <- czas życia instancji dla całego pliku
    # scope=session <- instancja współdzielona przez wszystkie przypadki testowe
    twitter = Twitter()

    def fin():
        twitter.delete()

    request.addfinalizer(fin)
    return twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message(twitter):
    assert twitter
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweets == []


@pytest.mark.parametrize('message, expected', (
        ('Test #first message', ['first']),
        ('#first Test message', ['first']),
        ('#FIRST Test message', ['first']),
        ('Test message #FIRST', ['first']),
        ('Test message #FIRST #second', ['first', 'second'])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.fand_tags(message) == expected

# PONIŻSZE 3 TESTY ROBIĄ TO SAMO CO 1 POWYŻSZY
# def test_tweet_with_hashtag():
#     twitter = Twitter()
#     message = 'Test #first message'
#     twitter.tweet(message)
#     assert 'first' in twitter.find_hashtags(message)
#
#
# def test_tweet_hashtag_on_beginning():
#     twitter = Twitter()
#     message = '#first Test message'
#     twitter.tweet(message)
#     assert 'first' in twitter.find_hashtags(message)
#
#
# def test_tweet_hashtag_on_uppercase():
#     twitter = Twitter()
#     message = '#FIRST Test message'
#     twitter.tweet(message)
#     assert 'FIRST' in twitter.find_hashtags(message)
