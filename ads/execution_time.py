from datetime import datetime


def execution_time(func, *args):
  time = datetime.now()
  func(*args)
  print(f"Elapsed time for {func.__name__}: {datetime.now() - time}")
  