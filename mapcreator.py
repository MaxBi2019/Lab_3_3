"""
This creates a map
"""
import folium


def create(dct, name):
    """
    :param dct: dict()
    :param name: str()
    :return:
    --------
    Create map
    """
    artstile = ([16, 26, "Georgia"], 8, 2, 120)
    my_map = folium.Map(location=[0, 0], zoom_start=2)
    first_layer = folium.FeatureGroup(name="Friends")
    for key in dct:
        friends = list(dct[key])
        last = len(friends)
        texts = [str(indx + 1) + ".) " + elm + (";"*bool(indx+1 != last) or ".") + "   <br>"
                 for indx, elm, in enumerate(friends)]
        len_max = max([max([len(elm) for elm in texts]), len(key[0])])
        scroll = f"<div style=\"height:{artstile[3]}px;" \
                 f"width:{len_max};" \
                 f"border:{artstile[1]}px solid red;" \
                 f"padding:{artstile[2]}%" \
                 f"font:{artstile[0][0]}px/{artstile[0][1]}px Georgia, {artstile[0][2]}, Serif;" \
                 f"overflow:auto;\">" \
                 + key[0]  + "<br>" + "Fiends: " + str(len(friends)) \
                 + "<br>" + "".join(texts)[:-5] + "</div>"
        first_layer.add_child(folium.Marker(location=key[1],
                                            popup=folium.Popup(scroll, \
                                                               max_width=(len_max + 6) * 6, \
                                                               min_width=len_max * 6), \
                                            fill_color="red", \
                                            icon=folium.Icon(color="red"), \
                                            fill_opacity=0.5))
    my_map.add_child(first_layer)
    my_map.save(name+".html")
