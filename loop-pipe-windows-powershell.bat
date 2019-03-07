$indir="Documents\inlas"
$outdir="Documents\outlas"
get-childitem $indir |
foreach-object {
if ($_.extension -ne ".las") {
continue
}
$outname = $outdir + "\" + $_.name
pdal pipeline -i \path\to\proj.json $_.fullname $outname
}