@if (@X)==(@Y) @end /* JScript comment 
       	cscript //E:JScript //nologo "%~F0"
        exit /b %errorlevel% 
@if (@X)==(@Y) @end JScript comment */ 


var sh=new ActiveXObject("WScript.Shell"); 
var title="ICaja - Google Chrome";
var keys="{ESCAPE}";

if (sh.AppActivate(title)){    
    sh.SendKeys(keys);     
 WScript.Quit(0);
} else {
 WScript.Echo("Failed to find application with title " + title);
 WScript.Quit(1);
}
 
