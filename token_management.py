# token_management.py

# Description:
# This file implements a token caching and reuse strategy to optimize performance
# by reducing the frequency of authentication requests. This strategy ensures that
# tokens are reused until expiration, reducing load on the authentication service
# and providing smoother operation under high concurrency scenarios, such as handling 
# multiple agents in a call center environment like Charter's.

import time

class TokenService:
    def __init__(self):
        self.token_cache = {}
    
    def get_token(self, token_key):
        # Check if token is already cached
        if token_key in self.token_cache and self.token_cache[token_key]['expiry'] > time.time():
            return self.token_cache[token_key]['token']  # Return cached token
        
        # If not cached or expired, fetch a new token
        new_token = self.fetch_new_token(token_key)
        self.token_cache[token_key] = {'token': new_token, 'expiry': time.time() + 3600}  # Cache token for 1 hour
        return new_token

    def fetch_new_token(self, token_key):
        # Simulate fetching a new token (could be from an authentication service)
        return f"new_token_for_{token_key}"

# Example usage:
token_service = TokenService()
token = token_service.get_token('user_123')
print("Token:", token)

