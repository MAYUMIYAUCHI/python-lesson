import builtins
builtins.print()

ranking = {
  'A':100,
  'B':85,
  'c':95
}

print(sorted(ranking, key=ranking.get,reverse=True))