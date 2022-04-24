function logout --wraps='pkill -KILL -u v' --description 'alias logout=pkill -KILL -u v'
  pkill -KILL -u v $argv; 
end
