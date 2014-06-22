if ((agent_started)); then
  echo "Killing ssh agent"
  ssh-agent -k
fi
