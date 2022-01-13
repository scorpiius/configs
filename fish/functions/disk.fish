function disk --wraps='sudo ncdu -x /' --description 'alias disk=sudo ncdu -x /'
  sudo ncdu -x / $argv; 
end
