on run {daemon_file, agent_file, user}

  set sh1 to "echo " & quoted form of daemon_file & " > /Library/LaunchDaemons/asia.redesk.ReDesk_service.plist && chown root:wheel /Library/LaunchDaemons/asia.redesk.ReDesk_service.plist;"

  set sh2 to "echo " & quoted form of agent_file & " > /Library/LaunchAgents/asia.redesk.ReDesk_server.plist && chown root:wheel /Library/LaunchAgents/asia.redesk.ReDesk_server.plist;"

  set sh3 to "cp -rf /Users/" & user & "/Library/Preferences/asia.redesk.ReDesk/RustDesk.toml /var/root/Library/Preferences/asia.redesk.ReDesk/;"

  set sh4 to "cp -rf /Users/" & user & "/Library/Preferences/asia.redesk.ReDesk/RustDesk2.toml /var/root/Library/Preferences/asia.redesk.ReDesk/;"

  set sh5 to "launchctl load -w /Library/LaunchDaemons/asia.redesk.ReDesk_service.plist;"

  set sh to sh1 & sh2 & sh3 & sh4 & sh5

  do shell script sh with prompt "ReDesk wants to install daemon and agent" with administrator privileges
end run
