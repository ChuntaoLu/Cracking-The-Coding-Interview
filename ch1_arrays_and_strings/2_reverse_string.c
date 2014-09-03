#include <stdio.h>

void reverse(char* str)
{
  char tmp;
  char* end = str;
  if (str)
  {
    while (*end) ++end;
    --end;
    while (str < end) {
      tmp = *str;
      *str++ = *end;
      *end-- = tmp;
    }
  }
}

int main(int argc, char *argv[])
{
  char *s = argv[1];
  reverse(s);
  printf("%s\n", s);
  return 0;
}
