###############################################################################################################
# 											    Environment Directories	        							  #
###############################################################################################################
$desktop = '~/Desktop/'
$packages = '~/appdata/local/programs/python/python310/lib/site-packages/'
$startup = '~/Documents/PowerShell/'
$startup_old = '~/Documents/WindowsPowerShell/'

###############################################################################################################
# 											      Environment Files	         								  #
###############################################################################################################
$historyfile = '~/appdata/roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt'
$profile_cmd = '~/Documents/WindowsPowerShell/Microsoft.Cmd_profile.cmd'

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
function clearhistory {echo '' > $historyfile; Write-Host "Your history has been cleared." -ForegroundColor red}
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
function rewards ([int]$user_agent=0, [int]$num_words=35, [int]$wait=5) {
	cd $test; python -c "from rewards import main; main(wait=$wait, num_words=$num_words, user_agent=$user_agent)" `
	-num_words=$num_words -user_agent $user_agent -wait $wait}

#################################################################################################################
# 										  Complex Functions with Parameters									  	#
#################################################################################################################
function npp([string] $file=' ') {
	<#.Synopsis
	Starts notepad++ with or without a file to open.#>
	start notepad++ $file}

###############################################################################################################
#                                                Notepad++ Functions                                          #
###############################################################################################################
function openhistory {npp $(resolve($historyfile))}
function profile {npp $profile}

# End of file