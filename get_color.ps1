Add-Type -AssemblyName System.Drawing
$imagePath = "c:\Users\Adhi\sample-loud--feature-v1\images\Logo1 copy.png"
$bmp = [System.Drawing.Bitmap]::FromFile($imagePath)
$totalR=0
$totalG=0
$totalB=0
$count=0

for($x=0; $x -lt $bmp.Width; $x+=10) {
    for($y=0; $y -lt $bmp.Height; $y+=10) {
        $p = $bmp.GetPixel($x, $y)
        if($p.A -gt 200) {
            $totalR+=$p.R
            $totalG+=$p.G
            $totalB+=$p.B
            $count++
        }
    }
}

if($count -gt 0) {
    $avgR=[Math]::Round($totalR/$count)
    $avgG=[Math]::Round($totalG/$count)
    $avgB=[Math]::Round($totalB/$count)
    Write-Output "R:$avgR G:$avgG B:$avgB"
} else {
    Write-Output "No opaque pixels found"
}

$bmp.Dispose()
