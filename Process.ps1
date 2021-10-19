$rptdate=Get-Date
$targetComputer=$env:COMPUTERNAME

$Header1 = @"
<style>
TABLE {border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
TD {border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
</style>
<p>
<b> Analisis de Procesos $rptdate </b>
<p>
Nombre de Evento: <b>Consumo Alto de CPU </b>
<p>
Nombre de la Computadora: <b> $targetComputer </b>
<p>
"@

$Header2 = @"
<style>
TABLE {border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
TD {border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
</style>
<p>
<b> Analisis de Procesos $rptdate </b>
<p>
Nombre de Evento: <b>Tiempo transcurrido en la ejecucion de un Proceso</b>
<p>
Nombre de la Computadora: <b> $targetComputer </b>
<p>
"@

$Header3 = @"
<style>
TABLE {border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
TD {border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
</style>
<p>
<b> Analisis de Procesos $rptdate </b>
<p>
Nombre de Evento: <b>Procesos que se ejecutan desde que inicia el SO</b>
<p>
Nombre de la Computadora: <b> $targetComputer </b>
<p>
"@

$ReportFile1= ".\Report-CPU.html"
$ReportFile2= ".\Report-TCPU.html"
$ReportFile3= ".\Report-PCPU.html"


Get-Process |select Name,cpu|sort cpu -Descending |
 ConvertTo-Html -Head $Header1 -Property Name, CPU |
 Out-File $ReportFile1


Get-Process | Select-Object Id,Name,TotalProcessorTime |
 ConvertTo-Html -Head $Header2 -Property Id,Name, TotalProcessorTime |
 Out-File $ReportFile2

Get-WmiObject win32_process | Sort-Object Processid | Select-Object Processid,Name,CommandLine|
 ConvertTo-Html -Head $Header3 -Property Processid,Name, CommandLine |
 Out-File $ReportFile3