def main(argv):
   print(argv)
   program, *args = argv
   print(program, args)
   result = sum(map(int, args))
   print(f'результат: {result}')
   return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))