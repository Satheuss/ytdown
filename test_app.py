#pip install pytest
import pytest
from app import is_valid_youtube_url

# Teste 1
def test_url_youtube_valida():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert is_valid_youtube_url(url) == True

# Teste 2
def test_url_invalida_rejeitada():
    url = "https://www.google.com"
    assert is_valid_youtube_url(url) == False

# Teste 3
def test_url_shorts_valida():
    url = "https://www.youtube.com/shorts/abcdefghijk"
    assert is_valid_youtube_url(url) == True