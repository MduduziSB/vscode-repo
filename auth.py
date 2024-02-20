#!/usr/bin/env python3
from flask import Flask, request


class Auth:
    """
    class Auth definition
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if not path or not excluded_paths or path not in excluded_paths:
            return True
        return False
    
    def authorization_header(self, request=None) -> str:
        return None