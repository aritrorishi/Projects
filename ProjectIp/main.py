import requests
import folium
import sys


url = "https://leafletjs.com/examples/custom-icons/{}".format
icon_image = url("leaf-red.png")
shadow_image = url("leaf-shadow.png")

icon = folium.CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    # shadow_image=shadow_image,
    # shadow_size=(50, 64),
    # shadow_anchor=(4, 62),
    popup_anchor=(-3, -76),
)


def create_map(ip_address):
    access_token = 'ece76bb2df618d'  # Replace with your IPinfo access token
    url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
    data = response.json()    
    if 'loc' in data:
        latitude, longitude = data['loc'].split(',')
        city = data['city']       
        m = folium.Map(location=[0, 0], zoom_start=2, tiles= 'CartoDB dark_matter', min_zoom=2)

        folium.PolyLine(
            locations=[[float(latitude), -180], [float(latitude), 180]],
            color='orange',
            weight=0.5,
            opacity=2
        ).add_to(m)

        folium.PolyLine(
            locations=[[-90, float(longitude)], [90, float(longitude)]],
            color='orange',
            weight=0.5,
            opacity=2
        ).add_to(m)        

        # folium.CircleMarker(
        #     location=[latitude, longitude],
        #     radius=8,
        #     color='yellow',
        #     fill=True,
        #     fill_color='yellow',
        #     fill_opacity=1
        # ).add_to(m)

        folium.Marker(
            location=[latitude, longitude],
            icon=folium.DivIcon(html='<div style="font-family: sans-serif; color: yellow;">✧</div>'),
            popup=ip_address +", "+ data['city']
        ).add_to(m)

        map_name = m.get_name()

        # Add JavaScript to control draggable behavior
        script = f"""
        <script>
            function disableDraggingOnMinZoom() {{
                var map = {map_name};
                function updateMapInteractivity() {{
                    if (map.getZoom() === map.getMinZoom()) {{
                        map.dragging.disable();
                        map.touchZoom.disable();
                        map.doubleClickZoom.disable();
                        map.scrollWheelZoom.disable();
                    }} else {{
                        map.dragging.enable();
                        map.touchZoom.enable();
                        map.doubleClickZoom.enable();
                        map.scrollWheelZoom.enable();
                    }}
                }}
                map.on('zoomend', updateMapInteractivity);
                map.on('load', updateMapInteractivity);
                updateMapInteractivity();
            }}
            document.addEventListener("DOMContentLoaded", function() {{
                disableDraggingOnMinZoom();
            }});
        </script>
        """
        m.get_root().html.add_child(folium.Element(script))
        m.save('world_map.html')

        with open('location.txt', 'w') as f:
            f.write(f'{latitude},{longitude},{city},{ip_address}')
    else:
        print("Location information not available.")

# create_map('78.9.1.2')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        create_map(ip_address)
    else:
        print("No IP address provided.")
        latitude = 32.8
        longitude = 90.75
        with open('location.txt', 'w') as f:
            f.write(f'{latitude},{longitude}')
    
