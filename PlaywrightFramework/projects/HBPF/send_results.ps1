# This directory is where you have all your results locally, generally named as `allure-results`
$ReportPath="allure-results"
# This url is where the Allure-Test container is deployed. We are using localhost as example
$BaseUrl = "http://testmcil01:5050"
# Project ID according to existent projects in your Allure container - Check endpoint for project creation >> `[POST]/projects`
$ProjectId="hbpf"
#$ProjectId="my-project-id"

$Request = @{
  "results" = @()
}

$Files = (Get-ChildItem -File -Path "$PSScriptRoot\$ReportPath")
foreach ($Item in $Files) {
    $Content = Get-Content -Path $Item.FullName
    if ($Content){
        $Result = @{
          "file_name"= $Item.name
          "content_base64"= [Convert]::ToBase64String([IO.File]::ReadAllBytes($Item.FullName))
        }
        $Request.results += $Result;
    }
}

$json = ConvertTo-Json -InputObject $Request

Write-Output "------------------SEND-RESULTS------------------"
$SendResultsEndpoint="$BaseUrl/send-results?project_id=$ProjectId"
$result = Invoke-WebRequest -Uri $SendResultsEndpoint -ContentType 'application/json' -Method POST -Body $json -UseBasicParsing
Write-Output "Status Code:" $result.StatusCode
Write-Output "Response: " $result.Content