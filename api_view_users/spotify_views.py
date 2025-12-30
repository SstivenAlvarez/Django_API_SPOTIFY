from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
import requests

class SpotifyView(ViewSet):
    
    def get_token(self):
        """Obtiene token de Spotify"""
        CLIENT_ID = "clien id aqui"
        CLIENT_SECRET = "client secret aqui"
        
        auth = (CLIENT_ID, CLIENT_SECRET)
        data = {"grant_type": "client_credentials"}
        response = requests.post("https://accounts.spotify.com/api/token", auth=auth, data=data)
        return response.json().get("access_token")
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Busca canciones: /api/spotify/search/?q=Bad%20Bunny&type=track"""
        query = request.query_params.get('q')
        search_type = request.query_params.get('type', 'track')
        
        if not query:
            return Response({"error": "Parámetro 'q' requerido"})
        
        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        params = {"q": query, "type": search_type, "limit": 10}
        
        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        return Response(response.json())
    
    @action(detail=False, methods=['get'])
    def artist(self, request):
        """Busca artistas: /api/spotify/artist/?name=Bad%20Bunny"""
        name = request.query_params.get('name')
        if not name:
            return Response({"error": "Parámetro 'name' requerido"})
        
        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        params = {"q": name, "type": "artist", "limit": 5}
        
        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        return Response(response.json())
