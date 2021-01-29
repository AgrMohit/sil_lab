// strings that end with 000
#define NoSt 5
#define NoIn 2
#define NoFst 1

int state[NoSt] = {0, 1, 2, 3, 4};
int input[NoIn] = {0, 1};
int Rules[][NoIn] = {{1, 0}, {2, 0}, {3, 0}, {3, 0}};
int Final_st[NoFst] = {3};
int Initial_st = 0;
