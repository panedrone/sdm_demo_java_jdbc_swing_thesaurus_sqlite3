select * from downloads
where r_id = ?
order by d_date desc
limit ?, ?