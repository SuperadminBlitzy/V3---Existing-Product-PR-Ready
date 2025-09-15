#!/usr/bin/env python3
"""
Flask HTTP Server Application

Complete Python 3/Flask implementation providing identical functionality to the original Node.js server.
Implements a basic HTTP server that responds with "Hello, World!\n" to all requests on all paths
and HTTP methods, maintaining exact functional parity with the Node.js http.createServer() implementation.

Key Features:
- Handles ALL HTTP methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS)
- Responds to ALL request paths uniformly
- Returns static "Hello, World!\n" response with text/plain content type
- Binds to 127.0.0.1:3000 (matching original Node.js configuration)
- Provides identical status 200 response behavior

Technology Stack:
- Python 3.12.3
- Flask 3.1.x web framework
- Werkzeug WSGI development server
"""

from flask import Flask, Response

# Create Flask application instance
# This replaces Node.js http.createServer() functionality
app = Flask(__name__)

# Configure Flask application for development
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def handle_request(path):
    """
    Universal request handler providing identical functionality to Node.js implementation.
    
    Handles all HTTP methods and all request paths uniformly, returning the same static
    response regardless of the request method, path, headers, or body content.
    
    This function replaces the Node.js callback function:
    (req, res) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello, World!\n');
    }
    
    Args:
        path (str): Request path captured by Flask's path converter
    
    Returns:
        tuple: Response data, status code, and headers matching Node.js behavior
               - Response body: "Hello, World!\n" (includes newline character)
               - Status code: 200 (HTTP OK)
               - Content-Type: text/plain (matching Node.js setHeader)
    """
    # Return response matching exact Node.js behavior:
    # - Same response body with newline character
    # - Status code 200 (HTTP OK)
    # - Content-Type: text/plain header (without charset)
    # Use Response object to prevent Flask from adding charset=utf-8
    response = Response(
        response="Hello, World!\n",
        status=200,
        headers={'Content-Type': 'text/plain'},
        mimetype=None  # Prevent Flask from inferring mimetype and adding charset
    )
    return response

if __name__ == '__main__':
    """
    Application entry point providing identical startup behavior to Node.js server.
    
    Configures Flask to bind to the same network address and port as the original
    Node.js implementation (127.0.0.1:3000), ensuring seamless migration without
    changing client connection parameters.
    
    This replaces the Node.js server.listen() call:
    server.listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`);
    });
    """
    # Network configuration matching Node.js implementation
    hostname = '127.0.0.1'
    port = 3000
    
    # Display startup message matching Node.js console.log format
    print(f"Server running at http://{hostname}:{port}/")
    
    # Start Flask development server with identical network binding
    # host='127.0.0.1' matches Node.js hostname constant
    # port=3000 matches Node.js port constant  
    # debug=True enables development mode with auto-reload
    # use_reloader=True provides file change detection
    # threaded=True enables concurrent request handling
    app.run(
        host=hostname,
        port=port,
        debug=True,
        use_reloader=True,
        threaded=True
    )