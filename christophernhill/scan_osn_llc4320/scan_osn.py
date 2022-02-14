import s3fs
import xarray
import zarr

fs=s3fs.S3FileSystem(anon=True,client_kwargs={'endpoint_url': "https://mghp.osn.xsede.org"})
xzs_arr=[]
xzv_arr=[]
for dn in ["data%2.2d_%2.2d"%(j,i) for j in range(1,10) for i in range (1,2) ]:
 sn="cnh-bucket-1/poseidon/%s/llc4320_tests/10dayhourly/scalars"%(dn)
 print("Scanning \"%s\""%(sn))
 store=s3fs.S3Map(root=sn, s3=fs, check=False)
 xzs_arr.append( xarray.open_zarr(store) )
 sn="cnh-bucket-1/poseidon/%s/llc4320_tests/10dayhourly/velocities"%(dn)
 print("Scanning \"%s\""%(sn))
 store=s3fs.S3Map(root=sn, s3=fs, check=False)
 xzv_arr.append( xarray.open_zarr(store) )

xzs=xarray.concat(xzs_arr, dim="time")
xzv=xarray.concat(xzv_arr, dim="time")

sn="cnh-bucket-1/poseidon/data01_01/llc4320_grid"
print("Scanning \"%s\""%(sn)) 
store=s3fs.S3Map(root=sn, s3=fs, check=False)
xzg=xarray.open_zarr(store)

sn="cnh-bucket-1/poseidon/data01_01/llc4320_masks.zarr"
print("Scanning \"%s\""%(sn))
store=s3fs.S3Map(root=sn, s3=fs, check=False)
xzm=xarray.open_zarr(store)

xz=xarray.merge([xzs,xzv,xzg,xzm])

xz.info()
