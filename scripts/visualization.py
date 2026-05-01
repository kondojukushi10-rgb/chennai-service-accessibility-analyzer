import leafmap.foliumap as leafmap

def visualize_accessibility(zones, column, title):

    m = leafmap.Map(center=[13.08, 80.27], zoom=10)

    m.add_data(
        zones,
        column=column,
        cmap="YlGnBu",
        layer_name=title,
        legend_title=title
    )

    m.add_basemap("OpenStreetMap")
    m.add_layer_control()

    return m