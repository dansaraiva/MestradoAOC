int proc_mdc(int x, int y) { 
  while (x != y) { 
    if (x < y) 
      y = y - x; 
    else 
      x = x - y; 
  } 
  return x; 
}