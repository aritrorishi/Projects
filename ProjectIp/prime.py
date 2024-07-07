import folium
from jinja2 import Template
from folium import IFrame
world_map = folium.Map(location=[0, 0], zoom_start=2, tiles= 'CartoDB dark_matter', min_zoom=2)
url = "https://leafletjs.com/examples/custom-icons/{}".format
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
with open('location.txt', 'r') as f:
    data = f.read()
    if data:
        lat,long,city,ipaddr = data.split(',')
        folium.PolyLine(
            locations=[[float(lat), -180], [float(lat), 180]],
            color='orange',
            weight=0.5,
            opacity=2
        ).add_to(world_map)

        folium.PolyLine(
            locations=[[-90, float(long)], [90, float(long)]],
            color='orange',
            weight=0.5,
            opacity=2
        ).add_to(world_map)       
     
# folium.CircleMarker(
#             location=[lat, long],
#             radius=5,
#             color='yellow',
#             fill=True,
#             fill_color='yellow',
#             fill_opacity=1
#         ).add_to(world_map)

folium.Marker(
    location=[lat, long],
    icon=folium.DivIcon(html='<div style="font-family: sans-serif; color: yellow;">✧</div>'),
    popup= ipaddr + ", " +city
).add_to(world_map)

map_name = world_map.get_name()
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
world_map.get_root().html.add_child(folium.Element(script))

world_map.save('world_map.html')


