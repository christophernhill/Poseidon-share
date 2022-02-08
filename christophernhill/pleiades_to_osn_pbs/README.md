Bits for transferring to OSN from a PBS job using rclone.

 - `bin/transfer_to_osn.sh` script that runs rclone with transfer
    to OSN style S3 endpoint (default mghp.osn.xsede.org).

 Script set to use rclone installed ( https://rclone.org/downloads/ ) in
 ~cnhill1/bin/rclone on Peiades.

 Pleiades nodes do not have direct internet access. For now easiects thing
 is to ssh back to front end and run rclone request that way.
