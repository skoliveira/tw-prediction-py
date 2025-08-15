import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class SceneStateMachine:
    def __init__(self):
        self.state = "inIntermission"
    
    @property
    def current_state(self):
        return self.state
    
    def transition(self, game_state, win_team, team_name):
        # print(f"Current state: {self.state}, Incoming game state: {game_state}")
        
        if self.state == "inIntermission":
            if game_state == "DOTA_GAMERULES_STATE_TEAM_SHOWCASE":
                self.change_to_showcase(win_team, team_name)
            elif game_state in ["DOTA_GAMERULES_STATE_PRE_GAME", "DOTA_GAMERULES_STATE_GAME_IN_PROGRESS"]:
                self.change_to_game()
        
        elif self.state == "inShowcase":
            if game_state is None:
                self.change_to_intermission()
            elif game_state in ["DOTA_GAMERULES_STATE_PRE_GAME", "DOTA_GAMERULES_STATE_GAME_IN_PROGRESS"]:
                self.change_to_game()
        
        elif self.state == "inGame":
            if game_state is None:
                self.change_to_intermission()
            elif game_state == "DOTA_GAMERULES_STATE_POST_GAME":
                self.change_to_showcase(win_team, team_name)
    
    def change_to_intermission(self):
        self.state = "inIntermission"
        print("Changing to intermission scene...")
    
    def change_to_showcase(self, win_team, team_name):
        self.state = "inShowcase"
        print("Changing to showcase scene...")
        
        if team_name is not None:
            if win_team == "none":
                print("Creating prediction")
                # Your logic for creating a prediction
            elif win_team == team_name:
                print("Resolving victory prediction")
                # Your logic for resolving a victory
            else:
                print("Resolving defeat prediction")
                # Your logic for resolving a defeat
    
    def change_to_game(self):
        self.state = "inGame"
        print("Changing to game scene...")

# Instantiate FSM
scene_state_machine = SceneStateMachine()

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        content_length = int(self.headers.get('Content-Length', 0))
        request_body = self.rfile.read(content_length).decode('utf-8')
        
        try:
            parsed_request = json.loads(request_body)
            game_state = parsed_request.get('map', {}).get('game_state')
            win_team = parsed_request.get('map', {}).get('win_team')
            team_name = parsed_request.get('player', {}).get('team_name')
            scene_state_machine.transition(game_state, win_team, team_name)
        except json.JSONDecodeError as error:
            print(f"Failed to parse JSON: {error}")
        
        self.wfile.write(b'')
    
    def do_GET(self):
        print("Not expecting other request types...")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        html = f"<html><body>HTTP Server at http://{host}:{port}</body></html>"
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def run_server():
    server = HTTPServer((host, port), RequestHandler)
    print(f"Server running at http://{host}:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()

if __name__ == "__main__":
    port = 2322
    host = "127.0.0.1"
    run_server()