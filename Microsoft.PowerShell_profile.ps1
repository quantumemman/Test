###############################################################################################################
# 											    Environment Directories	        							  #
###############################################################################################################
$desktop = "$HOME/Desktop"
$packages = "$HOME/Programs Files/Python/Python311/Lib/site-packages"
$startup = "$HOME/Documents/PowerShell"
$startup_old = "$HOME/Documents/WindowsPowerShell"

###############################################################################################################
# 											      Environment Files	         								  #
###############################################################################################################
$historyfile = "$HOME/Appdata/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt"
$profile_cmd = "$HOME/Documents/WindowsPowerShell/Microsoft.Cmd_profile.cmd"
$testfile = "test.txt"
$newtestfile = "output.txt"

###############################################################################################################
# 											      Basic Aliases												  #
###############################################################################################################
set-alias alias 'set-alias'
alias grep 'findstr'
alias py 'python'
alias sed 'replace'
alias touch 'new-item'
alias wc 'measure-object'

###############################################################################################################
# 												 Basic Functions											  #
###############################################################################################################
function clearhistory {echo '' > $historyfile; Write-Host "Your history has been cleared. :)" -ForegroundColor red}
function maxhistorycount {return $MaximumHistoryCount}
function showaliases {Get-ChildItem alias:\}
function showfunctions {Get-ChildItem function:\}
function x {exit}

###############################################################################################################
#                                           Directory Management Functions                                    #
###############################################################################################################
function cddesktop {cd $desktop}
function cdpackages {cd $packages}
function cdstartup {cd $startup}
function cdstartup_old {cd $startup_old}
function resolve([string]$path) {return $(Resolve-Path($path)).Path.Replace('\','/')}

###############################################################################################################
# 												 Python Functions  											  #
###############################################################################################################
function piplist ([string]$keyword='outdated') { python -c "from mylib import piplist; print(piplist(keyword=`'$keyword`'))" -keyword=$keyword }
function pipshow ([string]$package='', [string]$keyword='require') {python -m pip show $package | findstr -i "^$keyword" | findstr -i ":"}
function pipshow2 ([string]$package='') {python -c "from mylib import pipshow; print(pipshow(`'$package`'))" }
function pipupdate ([string]$list=$(piplist)) { 
	<#.Synopsis
	Finds any outdated Python packages that no other packages depend on and updates them using pip.#>
	if ($list.length -eq 0) { Write-Host "No outdated packages found. Exiting..." }
	else { Write-Host "python -m pip install --upgrade $list`n"; python -m pip install --upgrade $list.split(' ') } }
function rewards ([int]$user_agent=0, [int]$word_count=30, [int]$wait=30, [int]$exitbool=0, [int]$test=0, [string]$browser_agent='chrome', [int]$use_profile=1, [int]$use_cache=0, [string]$loglevel='warning') {
	python -c "from rewards import searchbot; searchbot(wait=$wait, words=$word_count, browser_agent=`'$browser_agent`', user_agent=$user_agent, test=$test, use_profile=$use_profile, use_cache=$use_cache, loglevel=`'$loglevel`')" `
	-word_count=$word_count -browser_agent=browser_agent -user_agent=$user_agent -wait=$wait -test $test -use_profile $use_profile -use_cache $use_cache -loglevel $loglevel
	if (($exitbool -eq 1) -And ($test -eq 0)) {exit} }
function rewardsall ([int]$delay=0, [int]$futurebool=0, [int]$num1=30, [int]$num2=20, [int]$bonus=0, [int]$wait2exit=15, [int]$exitbool=1, [int]$test=0, [int]$max_random_time=10, [string]$browser_agent='chrome', [int]$use_profile=1, [int]$use_cache=0, [string]$loglevel='warning', [int]$shuffle=1) {
	python -c "from rewards import searchbots; searchbots(delay=$delay, futurebool=$futurebool, num1=$num1, num2=$num2, bonus=$bonus, wait2exit=$wait2exit, test=$test, max_random_time=$max_random_time, browser_agent=`'$browser_agent`', use_profile=$use_profile, use_cache=$use_cache, loglevel=`'$loglevel`', shuffle=$shuffle)" `
	-delay=$delay -futurebool=$futurebool -num1=$num1 -num2=$num2 -bonus=$bonus -wait2exit=$wait2exit -test=$test -max_random_time=$max_random_time -browser_agent=$browser_agent -use_profile=$use_profile -use_cache=$use_cache -loglevel=$loglevel -shuffle=$shuffle
	if (($exitbool -eq 1) -And ($test -eq 0)) {exit} }
function rewardsauto ([int]$delay=0, [int]$futurebool=0, [int]$bonus=0, [int]$wait2exit=15, [int]$exitbool=1, [int]$test=0, [int]$max_random_time=10, [string]$browser_agent='chrome', [int]$use_profile=1, [int]$use_cache=0, [string]$loglevel='warning', [int]$shuffle=1) {
	python -c "from rewards import main; main(delay=$delay, futurebool=$futurebool, bonus=$bonus, wait2exit=$wait2exit, test=$test, max_random_time=$max_random_time, browser_agent=`'$browser_agent`', use_profile=$use_profile, use_cache=$use_cache, loglevel=`'$loglevel`', shuffle=$shuffle)" `
	-delay=$delay -futurebool=$futurebool -bonus=$bonus -wait2exit=$wait2exit -test=$test -max_random_time=$max_random_time -browser_agent=$browser_agent -use_profile=$use_profile -use_cache=$use_cache -loglevel=$loglevel -shuffle=$shuffle
	if (($exitbool -eq 1) -And ($test -eq 0)) {exit} }

###############################################################################################################
# 												  Rust Functions  											  #
###############################################################################################################
function build {cargo build}
function check {cargo check}
function run {cargo run --quiet}

###############################################################################################################
# 												  Git Functions  											  #
###############################################################################################################
function abort {git rebase --abort}
function add {git add .}
function amend {git commit --amend --no-edit}
function clone ([str]$link) {git clone -link $link}
function cont {git rebase --continue}
function commit ([string]$message) {git commit -m $message}
function fetch {git fetch --all}
function log ([int]$n=12) {git log -n $n --oneline --graph --decorate}
function rebase ([string]$commit=4) {
	<#.Synopsis
	Git rebase function. Pass in a number n to rebase -i HEAD~n or 'root' for --root.#>
	if ($commit.length -eq 4) {$commit = "--$commit"} else {$commit = "HEAD~$commit"}; git rebase -i $commit}
function show ([string]$commit=0) {
	<#.Synopsis
	Shows which files were affected by a commit. Accepts commit id or n for HEAD~n.#>
	if ($commit.length -lt 4) {$commit="HEAD~$commit"}; git show --pretty="" --name-status $commit}
function status {git status}
function logall ([int]$n=12) {foreach ($folder in $gitfolders) {
	cd $folder; Write-Host "`nCurrent Directory: $(resolve($folder))" -ForegroundColor green; log $n}}
function stall {foreach ($folder in $gitfolders) {
	cd $folder; Write-Host "`nCurrent Directory: $(resolve($folder))" -ForegroundColor green; fetch; status}}
function branches ([string[]]$list=$()) {foreach ($branch in $(git branch --list)) {
	$list+="$($($($branch).Replace("*",`"`")).Replace(" ",`"`"))"} return $list}
function stallbranches {
	Write-Host "`nCurrent Directory: $(resolve($(pwd)))" `
	-ForegroundColor green; git fetch --all; foreach ($branch in $(branches)) {git checkout $branch --quiet; git status}}

#################################################################################################################
# 										  Complex Functions with Parameters									  	#
#################################################################################################################
function beep ([int]$time=920, [int]$count=5, [int]$frequency=2000) {
	for ($j=0; $j -lt $count; $j++) {[console]::beep($frequency, $time)}}

function listgitrepos {
	<#.Synopsis
	Lists git repos in $gitfolders.#>
	foreach ($repo in $gitfolders) { Write-Host $(resolve($repo)) -ForegroundColor Cyan }}

function lock ([int]$test=0) {if ($test -eq 0) {rundll32.exe user32.dll,LockWorkStation} }

function lockcomputer ([int]$time=30, [int]$exit=1) {Write-Host "Sleeping for $time seconds, then locking computer..."; timer $time -lock 1 -exit $exit}

function npp([string] $file=' ') {
	<#.Synopsis
	Starts notepad++ with or without a file to open.#>
	start notepad++ $file}

function switcher ($desktop=0) {Switch-Desktop $desktop}

function timer ([int]$time=15, [int]$increment=30, [float]$h=0, [float]$m=0, [int]$s=0, [int]$beep=0, [int]$lock=0, [int]$switch=0, [int]$exit=0, [int]$test=0) {
	<#.Synopsis
	Sleeps for some time and provides updates every increment minutes.#>
	[int]$increment *= 60; if (-Not (($h -eq 0) -And ($m -eq 0) -And ($s -eq 0))) {$time = timerfun2($h, $m, $s)};
	$timearray = timerfun1($time); [int]$hours = $timearray[0]; [int]$minutes = $timearray[1]; [int]$seconds = $timearray[2];
	
	Write-Host ">> Timer set for $(timerfun3 $time)." -NoNewLine
	
	if ($beep -eq 1) {Write-Host " Then beeping." -NoNewLine}; if ($switch -eq 1) {Write-Host " Then switching." -NoNewLine};
	if ($lock -eq 1) {Write-Host " Then locking." -NoNewLine}; if ($exit -eq 1) {Write-Host " Then exiting." -NoNewLine}; Write-Host " Sleeping..."
	
	if ($hours -gt 2) {[int]$increment_now = $time%3600}
	elseif ($hours -gt 1) {[int]$increment_now = $time%3600%$(10*60)}
	elseif ($minutes -gt 20) {[int]$increment_now = $($time%3600)%$(10*60)}
	elseif ($minutes -gt 10) {[int]$increment_now = $($time%3600)%$(10*60)%60}
	elseif ($minutes -gt 2) {[int]$increment_now = $($time%3600)%$(10*60)%60}
	elseif ($minutes -gt 1) {[int]$increment_now = $($time%3600)%$(10*60)%10}
	else {[int]$increment_now = $($($time%3600)%$(10*60))%10}
	
	if ($test -ne 1) {Start-Sleep $increment_now}; $time -= $increment_now
	
	$start = ">> Now sleeping for "; $end = "..."
	
	while ($time -gt 0) {
		$timearray = timerfun1($time);  [int]$hours, [int]$minutes, [int]$seconds = $timearray; $sleep = 0;
		
		if ($hours -gt 2) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(60*60)) {$increment_now = $(60*60)} else {$increment_now = $increment} }
		
		elseif ($hours -eq 2) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(30*60)) {$increment_now = $(30*60)} else {$increment_now = $increment} }
		
		elseif (($hours -eq 1) -And ($minutes -gt 30)) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(30*60)) {$increment_now = $(30*60)} else {$increment_now = $increment} }
		
		elseif (($hours -eq 1) -And ($minutes -eq 30)) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(30*60)) {$increment_now = $(30*60)} else {$increment_now = $increment} }
		
		elseif ($hours -gt 1) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(30*60)) {$increment_now = $(30*60)} else {$increment_now = $increment} }
		
		elseif ($hours -eq 1) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(10*60)) {$increment_now = $(10*60)} else {$increment_now = $increment} }
		
		elseif ($minutes -gt 20) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(10*60)) {$increment_now = $(10*60)} else {$increment_now = $increment} }
		
		elseif ($minutes -gt 10) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt $(5*60)) {$increment_now = $(5*60)} else {$increment_now = $increment} }
		
		elseif ($minutes -gt 2) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 60) {$increment_now = 60} else {$increment_now = $increment} }
		
		elseif ($minutes -ge 1) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 10) {$increment_now = 10} else {$increment_now = $increment} }

		elseif ($seconds -gt 20) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 10) {$increment_now = 10} else {$increment_now = $increment} }
		
		elseif ($seconds -ge 15) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 5) {$increment_now = 5} else {$increment_now = $increment} }
		
		elseif ($seconds -eq 10) {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 1) {$increment_now = 1} else {$increment_now = $increment} }
		
		else {Write-Host "$(timerfun3 $time $start $end)";
			if ($increment -gt 1) {$increment_now = 1} else {$increment_now = $increment} }
		
		if ($test -ne 1) {Start-Sleep $increment_now}; $sleep += $increment_now; $time -= $sleep}
	
	Write-Host ">> Timer complete! Goodnight!! :)"; if ($beep -eq 1) {beep}; if ($switch -eq 1) {switcher 0};
	if ($lock -eq 1) {lock}; if ($exit -eq 1) {exit} }

function timer2 ([int]$time=15, [float]$h=0, [float]$m=0, [int]$s=0, [int]$beep=0, [int]$lock=0, [int]$exit=0, [int]$test=0) {
	<#.Synopsis
	Sleeps for some time and provides updates every increment minutes.#>
	if (-Not (($h -eq 0) -And ($m -eq 0) -And ($s -eq 0))) {$time = timerfun2($h, $m, $s)}; $timenow = $time;
	
	$start = ">> Timer set for "; $end = "."; Write-Host "$(timerfun3 $time $start $end)" -NoNewLine
	
	if ($beep -eq 1) {Write-Host " Then beeping." -NoNewLine}; if ($lock -eq 1) {Write-Host " Then locking." -NoNewLine};
    if ($exit -eq 1) {Write-Host " Then exiting." -NoNewLine}; Write-Host " Sleeping..."
	
	$start = ">> Now sleeping for "; $end = "..."; [int[]]$increment_array = $(timerfun6 $time);
	
	foreach ($increment in $increment_array) {
		if ($test -ne 1) {Start-Sleep $increment}; $timenow -= $increment; Write-Host "$(timerfun3 $timenow $start $end)"}
	
	Write-Host ">> Timer complete! Goodnight!! :)"; if ($beep -eq 1) {beep}; if ($lock -eq 1) {lock}; if ($exit -eq 1) {exit} }

function timerfun1 ([int]$time=0) {
	<#.Synopsis
	Converts time in seconds to (hours, minutes, seconds).#>
	[int]$h=[Math]::Floor($time/3600); [int]$m=[Math]::Floor($time%3600/60); [int]$s=[Math]::Floor($time%60); return $($h, $m, $s)}

function timerfun2 ([int[]]$timearray=$(0,0,0)) {
	<#.Synopsis
	Converts (hours, minutes, seconds) to time in seconds.#>
	[int]$h, [int]$m, [int]$s = $timearray; return [int]$($h*3600 + $m*60 + $s)}

function timerfun3 ([int]$time=0, [string]$start='',[string]$end='') {
	<#.Synopsis
	Converts time in seconds to "$start$h hours, $m minutes, and $s seconds$end" string.#>
	$timearray = timerfun1($time); [int]$h, [int]$m, [int]$s = $timearray;
	
	function fun ([int]$num) {if ($num -ne 1) {return 's'}}
	function fun1 ([int]$num, [string]$str) {if ($num -ne 0) {return "$num $str$(fun($num)), "}}
	function fun2 ([int]$h, [int]$m) {if (-Not (($h -eq 0) -And ($m -eq 0))) {return "and "}}
	
	return "$start$(fun1 $h hour)$(fun1 $m minute)$(fun2 $h $m)$s second$(fun($s))$end" }

function timetill ([int[]]$futuretime=$(08,00,00), [int[]]$adjustment=$(23,59,60), [int]$max_random_time=180,[int]$min_random_time=0) {
	$futuretime[1]=[int]$(Get-Random -Minimum $min_random_time -Maximum $max_random_time); $futuretime=timerfun1(timerfun2($futuretime))
	[int]$hour=$(Get-Date -AsUTC -Format %H); [int]$minute=$(Get-Date -AsUTC -Format %m); [int]$second=$(Get-Date -AsUTC -Format %s)
	[int]$month=$(Get-Date -AsUTC -Format %M); [int]$day=$(Get-Date -AsUTC -Format %d)
	[int[]]$now=$($hour, $minute, $second)
	
	[int]$hour_=$(Get-Date -Format %H); [int]$minute_=$(Get-Date -Format %m); [int]$second_=$(Get-Date -Format %s)
	[int]$month_=$(Get-Date -Format %M); [int]$day_=$(Get-Date -Format %d)
	[int[]]$now_=$($hour_, $minute_, $second_)
	
	[int[]]$delta=$($($($adjustment[0]+$futuretime[0]-$now[0])%24), $($adjustment[1]+$futuretime[1]-$now[1]), $($adjustment[2]+$futuretime[2]-$now[2]))
	Write-Host "UTC Time: now = $now, futuretime = $futuretime, delta = $delta.`nEDT Time: now = $now_, futuretime = $futuretime, delta = $delta."
	return $delta}

###############################################################################################################
#                                                Notepad++ Functions                                          #
###############################################################################################################
function openhistory {npp $(resolve($historyfile))}
function profile {npp $profile}

###############################################################################################################
# 												Secondary Aliases											  #
###############################################################################################################
alias aliases 'showaliases'
alias dl 'ytdl'
alias findfile 'find'
alias findgitrepos 'gitrepos'
alias functions 'showfunctions'
alias gitshow 'show'
alias listrepos 'listgitrepos'
alias pipupgrade 'pipupdate'
alias maxhistcount 'maxhistorycount'

# End of file