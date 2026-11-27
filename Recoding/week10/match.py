def is_match(text,pattern):
    if not text and not pattern:
        return True
    
    if not text:
        if pattern[0] == "*":
            return is_match(text,pattern[1:])
        return False
    
    if not pattern:
        return False
    
    if text[0] == pattern[0] or pattern[0]== "?":
        return is_match(text[1:],pattern[1:])
    
    if pattern == "*":
        return is_match(text[1:],pattern) or is_match(text,pattern[1:])
    
    return False

