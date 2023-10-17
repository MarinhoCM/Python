import leafmap

ceara = leafmap.Map(center=[-5, -39])
PLANET_API_KEY = 'PLAK20b2cfcce7ba4390b55628d7fd46d641'

ceara.add_planet_by_quarter(year=2016, quarter=1)


set_theme = leafmap.Map(
    google_map="HYBRID",height="500px", width="800px"
    ,layers_control=True,zoom=8
)
ceara.add_osm_from_geocode("Ceará", layer_name='Ceará')


layers_dict = leafmap.planet_quarterly_tiles()
ceara.add_time_slider(layers_dict, time_interval=1)


url = (
    'https://github.com/giswqs/leafmap/ ' +
    'raw/master/examples/data/wind_global.nc'
)
filename = 'wind_global.nc'

tif = 'wind_global.tif'
leafmap.netcdf_to_tif(
    filename, tif, variables=['u_wind', 'v_wind'], shift_lon=True
)

ceara.add_velocity(
    filename, zonal_speed='u_wind',
    meridional_speed='v_wind'
)
 