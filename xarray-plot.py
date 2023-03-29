import xarray as xr

store = 'https://ncsa.osn.xsede.org/Pangeo/pangeo-forge/pangeo-forge/CMIP6-PMIP-feedstock/CMIP6.PMIP.MIROC.MIROC-ES2L.past1000.r1i1p1f2.Amon.tas.gn.v20200318.zarr'
ds = xr.open_dataset(store, engine='zarr', chunks={})

ds['tas'].isel(time = 1000).plot(x='lon',y='lat',cmap='magma',vmin=0, vmax=50)